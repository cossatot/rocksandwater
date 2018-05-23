Title: Slip partitioning part I: Earthquake slip obliqiuty across the globe
Date: 2011-3-14
slug: slip-partitioning-part-i-earthquake-slip-obliquity-across-the-globe
---

<!-- Pelican_Begin_Summary -->

*This post originally appeared 14 March 2011 on my [old blog][]. The text and
figures are shown here unedited.  Presently, I think a lot of this can be
explained by Mohr-Coulomb mechanics and rheologic heterogeneities in the 
crust.  I also cringe a little at the way I did the statistics...  Also, I
don't know right now how to format the figure captions in Markdown.*

One of my favorite problems in tectonics is earthquake slip obliquity and 
partitioning, particularly where dip-slip and strike-slip motion are 
accommodated on separate faults (vs. similar slip on several adjacent 
structures) when stress is transtensional or transpressional with respect 
to the faults.  Though motion at plate boundaries is almost never truly 
parallel or perpendicular to the plate boundaries, much of the time earthquake 
or fault slip is; a prime example of this is mid-ocean ridges, which are 
partitioned into roughly orthogonal normal fault segments and transform fault 
segments.

[old blog]: http://rocksandwaterdotnet.wordpress.com/2011/03/14/slip-partitioning-part-i-earthquake-slip-obliquity-across-the-globe/

<!-- Pelican_End_Summary -->

This is an interesting problem because it’s a global phenomenon, happens on a 
variety of scales (from plate boundaries to at least field mapping scale; I 
don’t know about outcrop to microstructure scale), and has considerable 
implications for fault loading and seismic hazards.  And I don’t consider it 
to be sufficiently explained.  It does crop out in the literature now and 
again, and someone will throw out a new theory, and maybe look at a couple of 
different seismic events, and call it good, but we are awaiting a rigorous, 
global study.

I’ve poked at this problem a bit over the past couple of years, and though I 
have not arrived at a solution, I have had some fun with it.  I have approached 
it from two different standpoints.  One of them is an observational approach: 
considering the global earthquake focal mechanism and plate boundary catalogs, 
and doing basic analysis (stats, etc.) on those data.  The other is a 
theoretical approach: basic modeling of friction during oblique slip on a 
dipping fault vs. dip slip on a dipping fault and strike-slip on a vertical 
fault.  For this post, I’ll stick with the observations; the modeling is 
interesting as well, but I need to rethink some of it before posting.

![Alt Text](/images/slip_partitioning_map.png)

Several things are evident from this figure.  The first is that, in general, 
earthquake slip is not very oblique: most of the events are yellow (less than 
15 degree rake).  Secondly, it is obvious that there is considerable spatial 
variation to the amount of slip obliquity.  We can see that some plate 
boundaries, such as the Sumatran trench, tend to have a lot of low-obliquity 
events, whereas others, such as the Mid-Atlantic Ridge, are fairly oblique.

To see if certain plate boundary types have more partitioning than others, I 
joined all of the events to the nearest plate boundary segment (events more 
than 1 degree from a boundary are considered intraplate events) and compared 
the earthquake obliquity distribution for each boundary type to the general 
plate motion obliquity for each boundary type calculated from the Bird (2003) 
dataset:

![Alt Text](/images/pb_stats.png)

This figure shows that slip partitioning is especially complete at subduction 
zones, fairly complete at rift margins, and not a big deal at transform 
boundaries.  However, earthquake slip obliquity is very similar in all tectonic 
settings, suggesting there are some very fundamental controls on potential slip 
obliquity that may have to do with fault mechanics.  Now, I have to admit that 
these two datasets are not completely comparable, in that the earthquake slip 
obliquity is calculated directly from the rake while the plate motion vectors 
are purely horizontal, and there are some simplifying assumptions I had to make 
when dealing with earthquake nodal planes, etc., so this could be more 
rigorous, but I think that the gross observations here are solid.

What I find striking, though, is in a comparison of these two figures, and how 
in the same tectonic setting, different plate margins can show very different 
amounts of partitioning.  Take the subduction zones of Sumatra and Chile, for 
example: though Sumatra is overall a much more oblique system, its earthquakes 
appear less oblique than Chile’s.  It’d be interesting to look at each of the 
plate margins on earth, and compare their geology to the earthquakes and see 
what trends become apparent.  Maybe I’ll start on this when the semester is 
over.

In the mean time, I’ll take another look at the frictional modeling I started, 
and post that as well.
