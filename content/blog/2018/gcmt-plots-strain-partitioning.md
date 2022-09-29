---
title: A statistical picture of strain partitioning
author: Richard Styron
date: 2018-06-05
slug: gcmt-earthquakes-strain-partitioning
tags: tectonics, research, earthquakes, seismology, statistical seismology
---

Strain partitioning has interested me since I first heard about it. The basic 
idea is that in some regions, the strain field is not aligned exactly with the 
dominant fault system, so that fault system can't act as a 'pure' strike-slip 
or dip-slip fault system and relieve all of the accumulating interseismic 
strain. But instead of slipping obliquely, a second fault system comes online 
(forms or reactivates) and each of the systems work in tandem to accommodate 
the regional strain field through 'pure' faulting.

I don't know when the first phenomenological observations were made, but T.J. 
Fitch did a bit of pioneering work when plate tectonics was still in diapers-- 
[his 1972 paper in 
JGR](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/JB077i023p04432) 
is a classic on the matter in subduction zones, where strain partitioning is 
readily observed, as convergence is taken up on the megathrusts while 
transcurrent motion is taken up on upper-plate strike-slip faults located near 
the volcanic arc. Richard Jarrard and Rob McCaffrey worked on the problem in 
the 1980s and 1990s at the plate-boundary scale, and Basil Tikoff and 
collaborators worked on the structural aspects a bit more. (Many other 
scientists have done important work on this; these names are the first that 
come to mind. I might update this post with more references if I get a chance.)

Physical explanations for strain partitioning (also called slip partitioning) 
generally invoke the argument that it is frictionally favorable for dip slip on 
the dipping plane with a long down-dip width and strike slip on a vertical 
fault with a much shorter down-dip width (as the lower locking depth will be 
the same or even less; a vertical fault gets to a fixed depth with the minimum 
of fault area). There may also be arguments relating to shear stress vs. normal 
stress ratios as the stress tensor will be resolved differently on planes of 
different orientations--I've had seminar/water cooler conversations where this 
has been brought up, but I haven't seen the math and it might work out to 
actually be the same thing. (It also seems to be much less common in mylonites 
than in the brittle faults that lie up-dip, even on the same plane. I've seen 
this in my own work on [Tibetan core 
complexes](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/tect.20053).)

Strain partitioning is usually observed in fault traces and focal mechanisms in 
map view. The ridge-transform-ridge pattern of mid-ocean ridges is perhaps the 
clearest view of this--no oblique slip or non-orthogonal faults anywhere. It's 
not always apparent in geodetic fields which record interseismic strain 
accumulation unless there happens to be a big earthquake over the recording 
period, which does happen occasionally. This gives rise to the idea that *the 
patterns of interseismic strain accumulation are different than those of 
coseismic strain release* which I generally believe and will work on eventually 
(feel free to get a head start!).

But a quick look through the [Global CMT](http://www.globalcmt.org/) catalog 
shows the patterns as well. To be clear (I don't have a quick plot on hand but 
did the analysis years ago) the principal strain axes of a region are not 
preferentially aligned with plate margins or other major structures; 
convergence and divergence are frequently oblique. Nonetheless, when we plot 
rakes and dips of the entire GCMT catalog, it's obvious that 'pure' slip is 
favored:

[![GCMT dips and rakes][gcmt_1]][gcmt_1]
*__Figure 1__: Scatterplot of dips (on the radial axis) and rakes (on the 
circular axis) for all the events in the GCMT catalot; both nodal planes are 
included.  90° rake is reverse, 0° is sinistral, 270° is normal, and 180° is 
dextral.*

This plot shows several interesting things: 

First, there is a clear association between dip and rake, which is what is 
expected given strain partitioning. Strike-slip events, with rakes near 0° and 
180, are on steep faults (above 70°). Normal events, with rakes around 270°, 
have dips between 30° and 180°, are on steep faults (above 70°). Normal events, 
with rakes around 270°, have dips between 30° and 60°. Reverse events, with 
rakes around 90°, plot in two groups: one with dips between ~10° and 40°, and 
the other between about 60° and 80°. This bimodal distribution of reverse fault 
dips is because I plotted both nodal planes. The majority of real slip planes 
for the reverse events are in the shallower-dipping group.

Second, there are very few oblique-slip events--those with rakes near 45°, 
135°, 225°, or 315°, regardless of the dip.

The latter observation becomes more interesting when we incorporate depth:
[![GCMT dips and rakes with depth][gcmt_2]][gcmt_2]
*__Figure 2__: Scatterplot of dips and rakes for all events in the GCMT 
catalog. Plot is the same as Figure 1, except the dots are colored by 
log(depth). 10 km depth is dark purple, while 700 km depth is yellow. Crustal 
events are generally purple, blue are megathrust events, and green to yellow 
are in-slab events.*

We can see from this plot that many of the oblique-slip events are greenish to 
yellowish, meaning that they are deep (>100 km) slab earthquakes. And a lot of 
the moderate-angle reverse events (those dipping around 45°) are about 50 km 
deep, where megathrusts are about this steep. The pattern of obvious shallow 
slip partitioning and oblique slip at depth is consistent with Andersonian 
fault mechanics, which predicts that near the surface of the earth, principal 
stress axes will be either near-horizontal or near-vertical because the earth's 
surface is a free surface that can't support the shear stresses that would 
result from other stress tensor orientations. However, this boundary condition 
fades with depth and seems to be irrelevant in slabs penetrating the mantle, 
which is no real surprise. It also looks like there are far fewer deep 
strike-slip events, which may tell us that slabs deform because they stretch or 
are compressed down-dip as they pass through different densities of mantle, but 
aren't torqued or twisted sideways.

[gcmt_1]: {static}/images/2018/gcmt_rake_dip_1.png
[gcmt_2]: {static}/images/2018/gcmt_rake_dip_2.png


