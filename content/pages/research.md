Title: Research


*last updated 19 December 2017*

My research mostly pertains to faulting, stress and lithospheric deformation. I 
have worked on this on a variety of spatial and temporal scales, from seconds
(looking at earthquake deformation) to millions of years (rift evolution). I do 
a lot of work on assembling fault datasets, such as the [GEM Foundation's][gem] 
Global Active Fault dataset, building off experience with previous regional 
catalogs, the [HimaTibetMap][HTM] and [Active Tectonics of the Andes][ATA].

I have a pretty multifaceted background, especially with regards to techniques,
but strongly favor field and computer work. Currently, the questions I am
investigating are best answered through computation, so I don't get out much
(sigh). But at least I'm not doing lab work!


[HTM]: https://github.com/HimaTibetMap/HimaTibetMap
[ATA]: https://github.com/ActiveTectonicsAndes/ATA 

# Projects: a perpetually-unfinished list
*(chronological-ish order)*

## GEM Global Active Faults compilation
My current day job: Putting together a comprehensive worldwide dataset of 
active fault traces and relevant attributes (geometry, kinematics, slip rate, 
etc.) for the [GEM Foundation][gem], called the GEM Global Active Faults 
project. The project is a mix of assembly and harmonization of regional 
catalogs where they exist, and new mapping (in GIS) of catalogs where they 
don't. I'll write a bit more about the GEM-GAF project soon. In the mean time, 
the data is [here][gem-gaf-gh] and you can view a webmap with nice little 
popups of the metadata at the [GEM Hazard Blog][gh_blog].


[gem]: https://www.globalquakemodel.org
[gem-gaf-gh]: https://github.com/GEMScienceTools/gem-global-active-faults
[gh_blog]: https://blogs.openquake.org/hazard/global-active-fault-viewer/


## Statistical methods in paleoseismology and neotectonics

I'm far more involved in neotectonics than my publication record would suggest. 
However, in recent years I've been pretty much bound to the computer for 
research, so the current projects are focused around statistical analysis of 
paleoseismic and neotectonic data, which is sort of like fieldwork, a little, 
kind of. 

In addition to the great tan from my monitor's glow, statistical methods on 
existing data have the benefit of going from idea to results far more quickly 
than anything involving cosmogenic nuclide processing, so it's been quite nice 
to collaborate with a few scientists and their ready-to-go data. Here's a 
little of what's stewing:

### Time-dependent earthquake likelihoods and survival analysis

Thinking of the ubiquitous media reports of 'overdue' earthquakes, I started 
wondering what that meant: in particular, if an earthquake hasn't occurred by 
its 'expected' time, how does that change the probability of when it will occur 
again? This question turns out to be similar to questions pertaining to 
lifetime probabilities, conditional on survival up to some age, in population 
demographics and engineering. In the former, it's called 'survival analysis' 
and in the latter, 'failure analysis' or 'reliability analysis'.

I've been using these methods to calculate probabilities for the time to the 
next earthquake, or to the probability of earthquake occurrence in some time. 
See this [blog post here on the San Andreas][saf_surv], or this [presentation 
on faults in western Washington State][agu_2016].


### Bayesian estimation of paleoearthquake magnitude

I'm collaborating with Brian Sherrod of the USGS to estimate the magnitudes of 
paleoearthquakes in the Puget Lowland of Washington State, incorporating both 
the offset measurements from trenches or fault scarp profile, and the length of 
ruptures. Both of these measurement types involve a lot of uncertainty, and 
there are some nuances to consider beyond simple scaling laws (particularly 
with fault offset, as that varies along the rupture trace considerably). We've 
extended previous Bayesian estimates of magnitude given offset measurements to 
incorporate length as well, which provides a much more accurate and precise 
estimate. This is being written up for BSSA, but for now look at the [AGU 2016 
presentation][agu_2016] for preliminary results.


### Monte Carlo—based slip rate histories
(coming soon).



[saf_surv]: /blog/2016/07/wrightwood-recurrence/

[agu_2016]: /blog/2016/12/agu-2016-puget-sound-seismicity/

## Tectonic stratigraphy in the Peruvian Altiplano

I spent a bit of time in spring 2015 helping my good friend and collaborator 
[Kurt Sundell][kurt] work through the Cenozoic stratigraphy of the Peruvian 
Altiplano. The goal is to understand orogenic plateau development, in 
particular when the basins between the Eastern and Western Cordilleras filled 
in, became deformed, and uplifted. Kurt is using modern basin analysis 
techniques supported by thermochronology U-Pb geochronology, and concatenating 
paleoaltimetry datasets, to investigate this. My role in the project was mostly 
field assistance, which was a nice change as I'm usually in the driver's seat.


[kurt]: https://scholar.google.com/citations?user=avSsazsAAAAJ&hl=en



## Topographic stresses and their effects on earthquakes and faulting
This is really cool and I'll write about it more in the future. Basically, we
are developing methods to calculate the stresses in the upper crust induced by
topography, and then using those stresses to get other constraints on tectonic
stresses, fault friction, etc., in the crust. We are also looking into how
those stresses interact with tectonic stresses during earthquakes. Preliminary
results from the 2008 Wenchuan and 2005 Pakistan earthquakes suggest that
topographic stresses can significantly affect the coseismic slip distribution
during the earthquakes, and in non-intuitive ways (if your intuition is like
mine). This is cool in and of itself, but also may give us more insight into
the processes and dynamics of earthquake ruptures. I presented this work at AGU
Fall 2013. The slideshow is [here][agu_2013].

Furthermore, the stresses on the fault from topography can be used to help
estimate the tectonic stresses, especially when the topographic stresses are
substantial. We (Eric Hetland and myself) developed the methods to do this
while working on the 2008 Wenchuan earthquake. We have a paper in
*Journal of Geophysical Research* about this ([pdf here][wench_pdf]; links to
the *JGR* page and formatted article will be provided as they're available).

[wench_pdf]: /pdfs/styron_hetland_2015_jgr_wenchuan_stress.pdf


I have written a lot of code to do these sorts of calculations, and am
open-sourcing things once they aren't embarrassingly messy. For example, the
code to perform the topographic stress calculations and to resolve stresses on
fault planes is [on github][halfspace_repo].

[agu_2013]: /pdfs/styron_agu2013.pdf
[halfspace_repo]: https://github.com/cossatot/halfspace

I have also decided to blog a paper that I'm looking to resubmit after a 
square-peg-round-hole experience with *Geology* on how topographic stresses can 
modulate fault kinematics in Nepal and adjacent Tibet. The blog post is 
[here](/blog/2017/12/nepal-topo-stress-fault-kinematics/) and hopefully in 2018 
it will find its way to a journal near you.


## Extensional history of the South Snake Range Detachment
I worked with Sarah Evans at UNLV doing thermochronological modeling with
Pecube of the South Snake Range Detachment in eastern Nevada. She has collected
a lot of (U-Th)/He data, which we combined with published fission track
data. The collaboration turned out quite well: we found robust evidence of 
protracted extension throughout much of the Paleogene at pretty low rates 
before the big Miocene extensional pulse, and a smaller Quaternary pulse as 
well. The Paleogene contributed about half (10-15 km) of the total 20-35 km of 
extension. Rates were low, ~0.1 mm/yr for the Paleogene pulse and ~0.5-0.75 for 
the Miocene pulse, and could be ~0.2 mm/yr today.

We published a [paper][ssr_tect] in Tectonics in 2015 ([pdf here][ev_pdf]):

[ssr_tect]: http://onlinelibrary.wiley.com/doi/10.1002/2015TC003913/full
[ev_pdf]: /pdfs/evans_et_al_2015_tectonics_ssrd_thermochron.pdf


## Low-angle normal fault earthquake likelihood
This was a fun little project that was published in Geophysical
Research Letters. In it, we (myself and Eric Hetland)
[mapped all of the known subareal low-angle normal faults][lanf_map_blog]
and then calculated the maximum likelihood of catching one in the act of
rupturing in some short time period (which we haven't really done in the modern
earthquake focal mechanism catalogs). Then, we used Bayesian methods to show
how to quantitatively adjust our beliefs about low-angle normal fault
seismicity in light of both observations of no significant low-angle normal
fault seismicity in the catalogs, and the likelihood of actually observing this
phenomenon, should it be real.

[lanf_map_blog]: /blog/2013/12/lanf-gis-repo/


## North Andean tectonics
#### Rifting and basin inversion in the Eastern Cordillera, Colombia
I did a short project with The Instituto Colombiano del Petroleo (the research
wing of Ecopetrol) doing thermochronologic modeling of a very extensive
thermochronology database in the eastern Cordillera. We were modeling mostly
Mesozoic basin development followed by Cenozoic contraction, including changes
in contraction rate through time. Cool project, but I think we pushed Pecube
(the modeling software) to much more complicated fault geometries than it is
meant for, so we didn't push to publish the results (which are already pretty
well constrained by balanced cross sections). The results are going to be used
to compare against a forthcoming modeling program by that uses 2D-Move sections
to do thermochron modeling.

### Active faults in the northern Andes and oblique convergence
This was a project headed by Gabriel Veloza. We (mostly Gabriel) made a big
[database of active faults in the northern Andes][ATA], and then he and I
compiled all of the GPS data for the region and showed how the regional fault
kinematics (shortening/thrusting to the trench, strike-slip faulting parallel
to the trench, extension where there are changes in the convergence obliquity
direction) that are seen in faults, earthquakes and GPS data are all quite
well explained by oblique convergence between the subducting Nazca plate and
the overriding South American plate. Mike Taylor and Andreas Mora contributed
a lot to the interpretation and provided guidance.


## Himalayan-Tibetan Rifting
A lot of work (most of my dissertation, plus a couple of MS theses by my
colleagues, and a bit of help from our friends) went into this. We worked on
this from a variety of perspectives. 
 
### Oblique convergence

The first was focused on Himalayan rifting. When we started the project, there
were several models seeking to explain how and why the Himalaya exhibited
arc-parallel extension. We took the four most prominent ones, developed tests
for each based on geodetic and geologic predictions made by each model, and
then tested them all by analyzing all the available published GPS data, and
geologic data where applicable (such as location and total offset of key
faults). We concluded that a model of variably-oblique convergence between
India and the Himalayan arc best described the 'modern' (late Miocene-present?)
deformation. The study was published in [Geosphere][] in 2011 ([pdf][him_pdf]).

Recently (1 December 2013), a [new paper][ngeo] by Mike Murphy, Mike Taylor (my
Ph.D. advisor) and collaborators came out in Nature Geoscience, in which they
find more field evidence for the influence of oblique convergence in faults in
central- western Nepal. This work was bolstered by numerical modeling results
by Dave Whipp and Chris Beaumont showing how increasing along-strike
convergence obliquity can explain the arc-parallel extension and translation
seen in the central-western Himalaya.

[Geosphere]: http://geosphere.gsapubs.org/content/7/2/582.short
[him_pdf]: /pdfs/styron_et_al_2011_geosphere.pdf
[ngeo]: http://www.nature.com/ngeo/journal/vaop/ncurrent/full/ngeo2017.html

I also have a project working on the late Quaternary slip rate history of the
Karakoram fault at Menci (near the southeastern end of the KF), but haven't
published anything on it yet (still waiting on the data). It was super fun
digging the cosmo pits, though. The site has multiple offset features of
different ages for some of the fault strands, and I wrote a Monte Carlo-based
Python program that takes sets of arbitrary PDFs of ages and offsets (these
don't have to be Gaussian or whatever; they can come straight from the map and
dating results), and calculates slip and slip rate histories through time,
with confidence intervals.


### South Tibetan and Himalayan long-term rift histories

South Tibet and the Himalayan hinterland is known for actively extending, and
because the area is in an active contractional orogen, is an archetype of
synconvergent extension. There are a handful of very well-developed rifts,
many of which contain metamorphic core complexes. Because the rifts are
active, and the area is pretty cold and dry and mostly unvegetated, the fault
scarps at the rangefronts are well-preserved. This makes it an ideal location
to study rifting and orogenic processes.

My colleagues and I have worked on this, mostly with the lens/tools of bedrock
mapping and thermochronology, and neotectonic mapping and cosmogenic nuclide
dating. The former gives insight into million-year timescales of deformation,
and the latter into thousands to hundreds of thousands of year timescales. The
neotectonics is still a work in progress, and it's not mostly my work.

*South Lunggar Rift*

The big half of my dissertation involved bedrock and Quaternary mapping of the
South Lunggar rift in southwestern Tibet. This was a great project; my advisor
and his buddies had done a little work in the North Lunggar rift to the north,
but the rift to the south (on the other side of some passes) was completely
unstudied, except for some InSAR and teleseismic work done on the 2008 *M*6.8
Zhongba earthquake, which occurred on the Palung Co fault in the rift.

So I got to take a basically unknown area and bring it into the 21st century,
knowledge-wise. It was a lot of work, but it was a wonderful experience. We
showed that the rift was a horst with two rift basins on either side, and the
north(west)ern part of the horst is an active metamorphic core complex, with a
well-developed mylonitic shear zone, fault scarps in moraine at the base with
over a hundred meters of cumulative offset, etc. We did zircon (U-Th)/He
dating and thermal modeling that showed that rifting initiated in the mid-
Miocene at slow rates (< 1 mm/a) and then sped up dramatically at ~8 Ma to
about 2.5-3 mm/a, when the South Lunggar detachment and core complex switched
on. We published a [paper][slr] in *Tectonics* in Oct. 2013 about it
([pdf][slr_pdf]). Good stuff!


[slr]: http://onlinelibrary.wiley.com/doi/10.1002/tect.20053/abstract
[slr_pdf]: /pdfs/styron_et_al_2013_tectonics_south_lunggar.pdf/


*North Lunggar Rift*

My good friend and colleague Kurt Sundell headed up a similar project to my
South Lunggar Rift in the North Lunggar Rift, to the north.  There was a little
more mapping done previously in the range, so Kurt really focused on
thermochronology. We published the [work][nlr] in *Tectonics* in 2013
([pdf][nlr_pdf]).

[nlr]: http://onlinelibrary.wiley.com/doi/10.1002/tect.20086/abstract
[nlr_pdf]: /pdfs/sundell_et_al_2013_tectonics_n_lunggar.pdf

*Lunggar Rifting and Indian underthrusting*

One of the cooler things to come out of the Lunggar Rift work was that
extension in the rifts clearly accelerated well after rifting initiated (by
millions of years). This was evident in both my modeling with Pecube and with
Kurt's 1.5-ish-dimensional modeling. But because we used different techniques,
we weren't able to directly compare our results.  Therefore, I went through
and re-modeled all of the North Lunggar thermochronological data with Pecube.
When combined with results from the south, it became evident that the timing
of acceleration propagates north; so basically, there is a wave of rapid
extension that is moving northward. This wave tracks in front of the northern
tip of India, and our interpretation is that crustal thickening at depth is
causing crustal extension near the surface as the orogen maintains an
equilibrium between horizontal, tectonic forces and vertical, gravitational
ones.  We [published this work][lng] in *Nature Geoscience* in February 2015
([pdf][lng_pdf]).

[lng]: http://www.nature.com/ngeo/journal/vaop/ncurrent/full/ngeo2336.html
[lng_pdf]: /pdfs/styron_et_al_2015_nat_geo_lunggar_accel.pdf



## 2010 Sierra El Mayor - Cucapah earthquake fault scarp LiDAR measurement
This was a fairly short project for me. I helped do LiDAR scans of a segment
of the Cucapah rupture, and some data management. Colleagues at UC Davis
(mostly Austin Elliott and Peter Gold) have done most of the analysis, which is
differencing the yearly scans of the fault to quantify fault scarp degradation
patterns and rates.


## Nicaraguan Geodesy and Tectonics
My MS thesis at University of Arkansas, with Glen Mattioli. We knew that the
Nicaraguan forearc was translating quite rapidly (>10 mm/yr) relative to the
rest of the country, but it wasn't clear where the faults that accommodated
this motion were. I set up several transects of arc-perpendicular GPS sites
over several tens of km to demarcate the shear zone (one or several faults)
and get a better estimate of the slip rates. Turns out that the fault is
right under the volcanic arc, which is why even though it's mega fast (14-17 mm
/yr) it's not visible.


## Montserrat syn-eruptive ground deformation
Spent about a year attempting to model huge and rapid surface deformations on
Montserrat during the 2003 eruption and dome collapse. Did a lot of work with
vertically stacked Mogi sources, but nothing really fit quite right. Turns out
that the deformation wasn't real but was caused by the volcanic plume
disturbing the atmosphere enough to really screw up the GPS signals. Learned
a lot about modeling, though.




