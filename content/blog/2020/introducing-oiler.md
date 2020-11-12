---
title: Introducing *Oiler*, a joint geologic-geodetic block modeler
author: Richard Styron
date: 2020-06-03
slug: introducing-oiler
status: draft
---

In March of 2019, I was trekking in the Annapurna foothills, during a vacation
preceeding a field campaign on the Western Nepal Fault System. It was the
longest time off of work that I had taken in quite a while, and I had submitted
a tranch of papers before getting on the plane. I was able to zoom out a bit and
think about what I wanted to accomplish over the next several years.

The great goal that I could not dissuade myself from setting was to make a
complete and internally-consistent estimation of slip rates for all of the
faults in the [GEM Global Active Faults Database], for immediate use in seismic
hazard modeling as well as for tectonic research. This is obviously a major
challenge, requiring two components: 1) Making a system that can calculate the
slip rates on a network of faults considering certain requirements that I have
(more on these below), and 2) actually having a global database of active faults
to work with.  Well, I had just completed the second component, at least as a
first pass. This meant I could focus on the first component.

I had about a week of working remotely from Kathmandu in between the vacation
and the arrival of my colleagues for the field campaign. I posted up in coffee
shops in Thamel and started coding on my little field computer.

Now, a little over a year later, I have the system that I need built and
debugged enough to start writing about it, at least informally.  *Oiler* is
ready for the public.

# Oiler design overview

*Oiler* is a tectonic block modeling program that incorporates both faults (and
geologic slip rates) and GNSS geodetic velocities. *Oiler* estimates fault slip
rates by modeling the relative motion of tectonic blocks in the model domain,
and considering that relative motion to be accommodated on faults.

*Oiler* is written in the [Julia] computer language, which is fast, powerful,
free, and open-source.

The mathematics and general solution strategy of *Oiler* are not new; they were
modified a bit from *Meade and Loveless (2009)*, with additional influence and
explanation from *Chase (1972)* and *Cox and Hart (1986)*. These sources are
very thorough, clear and detailed; I am extremely grateful to the authors for
their work. Some additional effort on my part has been put into incorporating
plate closure constraints into the linear solution, which may not be
necessary for pure GNSS solutions, as all the velocities share a common
reference frame, but is absolutely necessary with faults included.

What makes *Oiler* different is the intention of incorporating faults as mapped
in regional fault catalogs, rather than very simplified representations that are
more common in block models. *Oiler* treats fault slip rate measurements (or
estimates) as measurements of relative velocities between two blocks, just as
GNSS measurements are relative velocities between two blocks. This allows for a
finer discretization of deforming regions into smaller blocks, and the solution
to relative block motions in areas where little to no GNSS data is present.

## Fundamental mathematical framework
*Oiler* solves for the instantaneous rotation parameters (i.e., the Euler vector)
of blocks separated by faults. The core input data are velocities $\vec{V}$
describing the relative motions of blocks. The problem is linearized in the
manner of *Meade and Loveless (2009)*, so that the solution can be found through
a direct linear least-squares solution.

The fundamental (forward) equation for the velocity of a given point is 
$$ \vec{V}_B = \vec{\Omega}_B \times \vec{X}_P$$
where $\vec{V}_B$ is the velocity vector of point $P$ on block $B$,
$\vec{\Omega}_B$ is the Euler pole for $B$ relative to some reference frame or
other block, $\vec{X}_P$ is the location of $P$ in Cartesian coordinates, and
$\times$ is the cross product. (I can't yet find the exact origin of this
formulation; it is present as far back as *McKenzie and Sclater (1971)*, and
they credit *Goldstein (1950)*, a physics text; it is perhaps implicit in
earlier papers such as *Le Pichon (1968)*. If I find the first reference, I will
update this post.)

Brendan Meade (and perhaps others?) began to reformulate the problem so that it
can be solved through a direct inversion (e.g., *Meade and Hager, 2001*). This 
involves rewriting the previous equation with linear operators rather than the
cross product. As explained in *Meade and Loveless (2009)*, but using slightly
adapted terminology and an (east, north, up) coordinate system:

$$\vec{V}_B = \mathbf{P}_V \mathbf{G}_B \vec{\Omega}_P = \begin{bmatrix}
-\sin \lambda & \cos \lambda & 0 \\
-\sin \phi \cos \lambda & -\sin \phi \sin \lambda & \cos \phi \\
-\cos \phi \cos \lambda & \cos \phi \sin \lambda & \sin \phi
\end{bmatrix} \begin{bmatrix}
0 & \mathbf{R} \sin \phi & - \mathbf{R} \cos \phi \sin \lambda \\
- \mathbf{R} \sin \phi & 0 & \mathbf{R} \cos \phi \cos \lambda \\
\mathbf{R} \cos \phi \sin \lambda & -\mathbf{R} \cos \phi \cos \lambda & 0  \\
\end{bmatrix}$$

Note that $\lambda$ is the longitude and $\phi$ is the latitude, and
$$\vec{V}_B = \begin{bmatrix}V_E \\ V_N \\ V_U \\ \end{bmatrix} \, ,
\vec{\Omega}_B = \begin{bmatrix}X_B \\ Y_B \\ Z_B \\ \end{bmatrix} \; .$$

This allows for a least-squares solution for $\vec{\Omega}_B$, which is not
readily observable, as 
$$ \vec{\Omega}_B = \mathbf{P}_V \mathbf{G}_B \setminus \vec{V}_B \; .$$
where $\setminus$ represents the matrix solution, i.e. the `\` operator in
Matlab or Julia.  

$\mathbf{P}_V \mathbf{G}_B$ is a 3x3 matrix for each velocity
observation. The columns relate to the XYZ coordinates of $\vec{\Omega}_B$, and
the rows to the velocity components of $\vec{V}_B$.


For now on, we'll refer to the matrix containing any number of 
$\mathbf{P}_V \mathbf{G}_B$ sub-matrices as $\mathbf{G}$, the velocity observations as
$\mathbf{V}$, and the resulting vector of Euler rotation parameters as
$\mathbf{\Omega}$.  Then the inversion can be descriebd as 
$\mathbf{G} \setminus \mathbf{V} = \mathbf{\Omega}$.

### Multiple velocity observations and blocks

Although a numerical solution may sometimes be found when there is a single
velocity observation constraining each block, it is much better to have multiple
observations for each block, from both geophysical accuracy and numerical
stability perspectives.

As stated above, the columns of the matrix $\mathbf{P}_V \mathbf{G}_B$
correspond to the Cartesian coordinates of $\vec{\Omega}_B$. Therefore, if two
or more velocity observations for the same block relative to the same reference
frame are present, they can simply be stacked, as can their observations
$\mathbf{V}$:

$$\mathbf{G} = \begin{bmatrix}
\mathbf{P}_V \mathbf{G}_B 1 \\
\mathbf{P}_V \mathbf{G}_B 2 \\
\mathbf{P}_V \mathbf{G}_B 3 \\
\end{bmatrix}, \;
\mathbf{V} = \begin{bmatrix}
V_E 1 \\
V_N 1 \\
V_U 1 \\
V_E 2 \\
V_N 2 \\
V_U 2 \\
V_E 3 \\
V_N 3 \\
V_U 3 \\
\end{bmatrix}
$$





### Block circuits

$$\begin{bmatrix}
\mathbf{P}_V \mathbf{G}_B 1 & 0 & 0 \\
\mathbf{P}_V \mathbf{G}_B 2 & 0 & 0 \\
0 & \mathbf{P}_V \mathbf{G}_B 3 & 0 \\
0 & 0 & \mathbf{P}_V \mathbf{G}_B 4 \\
0 & 0 & \mathbf{P}_V \mathbf{G}_B 5 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & -1 &  0 &  0 & 1 & 0 & 0 \\
1 & 1 & 0 &  0 & -1 &  0 & 0 & 1 & 0 \\
1 & 0 & 1 &  0 &  0 & -1 & 0 & 0 & 1 \\
\end{bmatrix}$$