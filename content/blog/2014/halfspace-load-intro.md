Title: Halfspace: a Python package for elastic halfspace calculations
Date: 2014-09-18
slug: halfspace-load-intro
tags: tectonics, research, python, active faults, earthquakes, stress, halfspace

*(edited 4 October 2014)*

## Part 1: Introduction

I've been working the past year and a half on calculating topographic and
tectonic stresses. This work has relied heavily on using elastic halfspace
approximations, which are quite commonly used in the crustal deformation
communities, particularly by geodesists. To this end, I have written a [Python module][halfspace] for calculating the topographic stresses in a region, and
for doing Bayesian inversions for tectonic stresses that lead to earthquakes.
This blog post is an introduction to the use of the Python module. I am
finishing up a series of [IPython Notebooks](http://ipython.org/notebook.html)
that compose a tutorial of a topographic and tectonic stress inversion, using
the [2013 Balochistan, Pakistan earthquake](http://comcat.cr.usgs.gov/earthquakes/eventpage/usb000jyiv) as an
example. The notebooks are downloadable and executable. They are available
[here](https://github.com/cossatot/halfspace_user_guide/tree/master/topo_loads/notebooks). But if you want to work through the examples, please clone/download
the [whole repo on github][gh_repo], which has the necessary files (DEM, slip
model, and some other stuff).

![Topographic stresses in the halfspace below topography][topo_stress_image]
[topo_stress_image]: /images/topo_stress_image.png

[gh_repo]: https://github.com/cossatot/halfspace_user_guide

The [halfspace][halfspace] module aims to be eventually a fairly complete and
modular open-source module for use by anyone, particularly by those who are not
interested in coding up their own solutions (i.e. people who are not overly
invested in halfspace techniques, but want to use them for a short project).
Currently, though, it only has solutions for stresses resulting from surface
loads (as well as a lot of utilities for dealing with stress projections and
rotations, as well as other goodies). Additional solutions for strain from
surface loads, as well as stress and strain from dislocations ([Okada], 
[Meade triangles][mt], [Mogi]) and pressure sources ([Mogi]) will be added.

[halfspace]: https://github.com/cossatot/halfspace
[Okada]: http://www.bssaonline.org/content/82/2/1018.short
[mt]: http://www.sciencedirect.com/science/article/pii/S0098300407000593
[Mogi]: http://repository.dl.itc.u-tokyo.ac.jp/dspace/bitstream/2261/11909/1/ji0362002.pdf?origin=publicationDetail

### Introduction to the introduction
An elastic halfspace is a 'semi-infinite' elastic body; for our purposes, this
means that it is infinite in the $\pm x$, $\pm y$, and $+z$ directions (where 
$+z$ is down). It's like an infinitely wide, infinitely deep ocean. With a flat
(not spherical) surface. But elastic, not fluid.

Ok, so it's not really like an ocean. Never mind.

In any case, the 'elastic' designation basically implies all that comes with
[elasticity](http://en.wikipedia.org/wiki/Elasticity_(physics)) (which is less
complicated than conditional or directional infinities): basically, the
material instantly deforms when any stresses are applied, in a perfect Hooke's
law type manner, and instantly undeforms when stress is released, so there is
no time dependence here. Additionally, the material's rheologic parameters are
fully specified using any two of the [elastic moduli](http://en.wikipedia.org/wiki/Elastic_modulus), which is convenient.

Elastic halfspaces are frequently used by geodesists and other deformation
modelers because there are well-defined and usually simple mathematical
formulae describing the stresses and strains that result from particular
loading conditions. In the tectonics realm, this is most typically shear
dislocations on a plane, simulating slip on a fault. In the volcanology realm,
this is most often the opening or closing of an ellipsoidal or planar volume,
simulating fluid (magma or water) movement into or out of a reservoir.

### Topographic loading in a halfspace
Here, we approximate stresses resulting from topography by treating the
topography as basically an array of vertical point loads and then correcting
for the irregular surface boundary condition, and for the shear stresses that
result from slopes, by using arrays of horizontal point loads.

Stresses from vertical point loads are represented using Boussinesq's
solutions, which prescribe the six components of the stress tensor at an
arbitrary point from an arbitrary point load, for example:

![point load diagram](/images/point_load_diagram.png)

A DEM, or digital elevation model, is basically an array of point elevations.
We can use a DEM as such an array, and approximate the topographic loads by
adding up the individual point load contributions:

![DEM loading a halfspace](/images/topo_point_load.png)

As will be explained in the 
[Calculating the topographic stress field](../topo-stress-calcs/) section,
this is done efficiently using a time-domain convolution. We'll describe that
a bit more when we get there. In the mean time, we've got to get our software
installed and get the data (DEM and fault coseismic slip model) prepared.


## Table of contents for the rest of the guide
(Note that these may not be uploaded yet. The guides are procedurally complete,
but I want to add some of the math/theory explaining what is going on as well.)

- [Installation and configuration](../halfspace-installation/)
- [Preparing a Digital Elevation Model file](../halfspace-dem-prep/)
- [Preparing the coseismic slip model](../../10/fault-model-prep/)
- [Calculating the topographic stress field](../../10/topo-stress-calcs/)
- [Calculating the topographic stresses on the fault](../../10/fault-topo-stress-calcs/)
- [Bayesian inversion of tectonic stress pt. 1: Rake inversion](../tect-stress-rake/)
- [Bayesian inversion of tectonic stress pt. 2: Conditions at failure](../tect-stress-fail/)
