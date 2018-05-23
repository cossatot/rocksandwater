Title: Topographic and tectonic stress inversions with halfspace: Calculating topographic stresses on a fault
Date: 2014-10-06
slug: halfspace-fault-topo-stress-calcs
tags: tectonics, research, python, active faults, earthquakes, stress, GIS, halfspace

In order to complete the tutorial, please first clone/download the 
[github repo] [gh_repo] which comes with the DEM, coseismic slip model, and
some auxiliary files, all with the correct pathnames. 

[gh_repo]: https://github.com/cossatot/halfspace_user_guide

([Or just download this notebook](https://github.com/cossatot/halfspace_user_guide/blob/master/topo_loads/notebooks/calc_fault_topo_stresses.ipynb))

This part is pretty easy.  It's just an interpolation of the topographic stress
field $M(x,y,z)$ onto the fault, as represented by a coseismic slip model.

{% notebook notebooks/halfspace_calc_fault_topo_stress.ipynb cells[1:]%}

- [Installation and configuration](../../09/halfspace-installation/)
- [Preparing a Digital Elevation Model file](../../09/halfspace-dem-prep/)
- [Preparing the coseismic slip model](../halfspace-fault-model-prep/)
- [Calculating the topographic stress field](../halfspace-topo-stress-calcs/)
- [Calculating the topographic stresses on the fault](../halfspace-fault-topo-stress-calcs/)
- [Bayesian inversion of tectonic stress pt. 1: Rake inversion](../halfspace-tect-stress-rake/)
- [Bayesian inversion of tectonic stress pt. 2: Conditions at failure](../halfspace-tect-stress-fail/)

