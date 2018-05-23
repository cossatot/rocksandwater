Title: Topographic and tectonic stress inversions with halfspace: Calculating the topographic stress field
Date: 2014-10-6
slug: halfspace-topo-stress-calcs
tags: tectonics, research, python, active faults, earthquakes, stress, GIS, halfspace

*edited 22 Feb 2015: Equations $G_{xx}^B$ and $G_{yy}^B$ corrected*

## Background of the topographic stress field calculations

The weight of mountains (or other high topography) induces stresses in the
earth below the topography. Unlike many other types of stress in the crust,
topographic stresses are expected to have very significant spatial variation.
Therefore, in regions with high topography, it is important to include
topographic stresses into the overall stress budgets of the regions.

But because of this spatial variation in topographic stresses, calculating them
is not as straightforward as for some other stress components (such as
lithostatic stress, which is basically $\rho g z$). As explained in the
[introduction][intro], we use some techniques based on treating the earth as an
elastic halfspace to calculate the stresses. Elastic halfspaces do a good job
of representing appropriate (time-invariant) stresses and strains in the earth
due to forcing of various sorts. They also typically have simple and
well-defined solutions for how the stresses and strains from simple,
well-defined perturbations (i.e. other stresses and strains) propagate
throughout the halfspace. 

When we calculate stresses with `halfspace`, we use a set of these solutions
relating how a point load (force) of some known magnitude on the surface of the
halfspace induces stresses throughout the halfspace. First, we approximate
topography as a regularly-spaced array of vertical point loads 
([the Digital Elevation Model we prepared a couple steps back][dem_prep]), 
and use [Boussinesq][bouss]'s solutions for the stresses in the halfspace
resulting from the vertical point loads. 


### First step: Vertical topographic forces
Boussinesq's solutions are [Green's functions][gf] describing how the
stresses radiate throughout a halfspace from a single, vertical point load on
the surface (called $F_v$, which is equal to $-\rho g z$).  The equations
describe separate results for each of the six components of the stress tensor
at any point in the halfspace. We will call the stresses from the vertical
point sources $G^B_{ij}$, where $ij$ is the stress component of interest.

$$ G_{xx}^B = \frac{ F_v }{ 2\pi } \left[ \frac{ 3x^2 z}{ r^5 } \right. + \frac{\mu (y^2 + z^2)}{(\lambda + \mu) r^3 (z + r)}
- \frac{\mu z}{(\lambda + \mu) r^3} \left. - \frac{\mu x^2}{ (\lambda + \mu) r^2 (z + r)^2 }\right ] $$

$$ G_{yy}^B = \frac{F_v}{2\pi } \left [ \frac{3y^2 z}{r^5} \right.
+ \frac{\mu (x^{2} + z^{2})}{(\lambda + \mu) r^{3}(z + r)}
- \frac{\mu z}{(\lambda + \mu) r ^{3}} \left. - \frac{\mu y^{2}}{(\lambda + \mu ) r^2 (z +r)^2} \right] $$

$$ G_{xy}^{B} = \frac{F _{v}}{2\pi} \left[ \frac{3xyz}{r^{5}} - \frac{\mu x y (z + 2r)}{(\lambda + \mu) r^{3} (z + r)^{2}} \right] $$

$$ G_{zz}^{B} = 3 F _{v} z^{3} / 2 \pi r^{5} $$

$$ G_{xz}^{B} = 3 F _{v} xz^{2} / 2 \pi r^{5} $$

$$ G_{yz}^{B} = 3 F _{v} yz^{2} / 2 \pi r^{5} $$


![topo point load][point_load_image]
*Stress components produced by a single point load*

Next, we need to go from a single point load to an array of point loads. One of
the nice things about small stresses and strains in elastic halfspaces is that
they are addative, so the stress field from topography is basically the sum of
the stresses from the individual point loads. We could go through point by
point and calculate the stress field, but there is a much better way to do it.
Because of the [superposition principle][sp], we can take the sort of general
solution to the Boussinesq's solution above, i.e. when $F_v=1$, and
[convolve][convolve] this with the field of vertical forces $F_v(x,y)$, which
is the DEM times density $\rho$ and gravitational force $g$, yielding the
stress tensor field $M^B(x,y,z)$ (M stands for Mountain):

$$ M^B(x,y,z) = G^B(x,y,z) * F_v(x,y)$$

where $*$ is the convolution operator.

![topo array load][array_load_image]
*Stress componentes from an array of point loads representing topography*

This calculation can be sped up tremendously (for large arrays) because of the
[convolution theorem][conv_theor] which states that in cases like this, a 
convolution in the space domain is equivalent to a multiplication in the time
domain. This means that we can take the Fourier transforms of both the Green's
functions ($G^B$) calculated over some area, and the $F_v$ array, and then
multiply those and transform the product back, instead of doing a space-domain
convolution. This is great because both the Fourier transforms and the
multiplication are much faster operations than the space-domain convolution.

### Next step: Horizontal topographic forces

Up to this point, the methods as described have been thought up by many
scientists back to at least [Harold Jeffreys][hj]. However, the result isn't
quite complete. [Liu and Zoback (1992)][lz92] took these calculations a step
further and accounted for the effects of the irregular surface above (but
connected to) the halfspace into account. This includes both a correction for
the horizontal shear stress induced by the effects of slope on the halfspace,
and for how the irregular surface affects the propagation of stresses.

This step takes the topography and the uppermost stresses from the previous
result, and yields a field of horizontal loads $F_h(x,y)$ at the surface
of the halfspace. Then, it uses Cerruti's solutions for stresses in a halfspace
from a *horizontal* point load on the surface to propagate those stresses. The
steps are exactly the same as previously, except that the process has to be done
for horizontal loads in both the $x$ and $y$ directions. This produces a stress
field $M^C(x,y,z)$ that will be added to $M^B(x,y,z)$ to produce the final
topographic stress field $M(x,y,z)$.

The horizontal loading functions are

$$ F_{h, \, x}(x,y) = ( \rho g h(x,y) + M_{xx}^B(x,y,0) + T^0_{xx} )\, \frac{\partial h}{ \partial x} + (M_{xy}^{B}(x,y,0) + T^0_{xy}) \frac{\partial h}{ \partial y} $$

and 

$$ F_{h, \, yz}(x,y) = ( \rho g h(x,y) + \sigma_{yy}^B(x,y,0) + T^0_{yy} )\, \frac{\partial h}{ \partial y} + (M_{xy}^{B}(x,y,0) + T^0_{xy}) \frac{\partial h}{ \partial x}\; . $$

Cerruti's solutions are as follows (assuming a point source loading in the $+x$ 
direction:

$$ G_{xx}^{C_x} = \frac{ F_{h,x} x }{2 \pi r^3} \left[ \frac{ 3x^2}{r^2} \right. - \frac{\mu}{(\lambda + \mu)(z+r)^2} \left. (r^2 - y^2 - \frac{2ry^2}{r+z}) \right] $$

$$ G_{yy}^{C_x} = \frac{ F_{h,x} x }{2 \pi r^3} \left[ \frac{ 3y^2}{r^2} \right. - \frac{\mu}{(\lambda + \mu)(z+r)^2} \left. (3r^2 - x^2 - \frac{2rx^2}{r+z}) \right] $$

$$ G_{xy}^{C_x} = \frac{ F_{h,x} x }{2 \pi r^3} \left[ \frac{ 3x^2}{r^2} \right. - \frac{\mu}{(\lambda + \mu)(z+r)^2} \left. \cdot (r^2 - x^2 - \frac{2rx^2}{r+z}) \right] $$

$$G_{zz}^{C_x} = \frac{ 3 F_{h,x} x z^2 }{2 \pi r^5}$$

$$G_{xz}^{C_x} = \frac{ 3 F_{h,x} z x^2 }{2 \pi r^5}$$

$$G_{yz}^{C_x} = \frac{ 3 F_{h,x} x y z }{2 \pi r^5}$$

These equations are then re-used, with $x$ and $y$ switched, to calculate the
stresses from loads in the $y$ direction.

[intro]: ../halfspace-load-intro/
[point_load_image]: /images/point_load_diagram.png
[dem_prep]: ../halfspace-dem-prep/
[bouss]: http://en.wikipedia.org/wiki/Joseph_Valentin_Boussinesq
[gf]: http://en.wikipedia.org/wiki/Green's_function
[sp]: http://en.wikipedia.org/wiki/Superposition_principle
[convolve]: http://en.wikipedia.org/wiki/Convolution
[array_load_image]: /images/topo_point_load.png
[lz92]: http://engr.uconn.edu/~lanbo/1992JGR.pdf
[hj]: http://en.wikipedia.org/wiki/Harold_Jeffreys

Here is the code to do all of this:

{% notebook notebooks/halfspace_topo_stress_field_calcs.ipynb cells[1:]%}

## Table of Contents for the `halfspace` tutorial

- [Installation and configuration](../../09/halfspace-installation/)
- [Preparing a Digital Elevation Model file](../../09/halfspace-dem-prep/)
- [Preparing the coseismic slip model](../halfspace-fault-model-prep/)
- [Calculating the topographic stress field](../halfspace-topo-stress-calcs/)
- [Calculating the topographic stresses on the fault](../halfspace-fault-topo-stress-calcs/)
- [Bayesian inversion of tectonic stress pt. 1: Rake inversion](../halfspace-tect-stress-rake/)
- [Bayesian inversion of tectonic stress pt. 2: Conditions at failure](../halfspace-tect-stress-fail/)


