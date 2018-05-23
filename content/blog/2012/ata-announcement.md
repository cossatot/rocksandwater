Title: Active Tectonics of the Andes (ATA-1.0): A new open-source active fault database, and interpretation
Date: 2012-10-1
slug: ata-announcement
tags: research, active faults, GIS, Andes, tectonics

*This post originally appeared on my [old blog](http://rocksandwaterdotnet.wordpress.com).  Please note that the [ATA database is now located at GitHub][atagh].*

The 1 October 2012 issue of [GSA Today][gsat] (a science and news magazine by the Geological Society of America) features a [new article][na] from our research group, primarily written by my friend and colleague Gabriel Veloza.  There are two contributions in this paper: the first is an 
[open-source active fault database called Active Tectonics of the Andes, or ATA-1.0][ata], and the second is an overview of northern Andean tectonics and an interpretation of the overall fault kinematics as resulting from variably-oblique subduction.

[gsat]: http://www.geosociety.org/gsatoday/
[atagh]: https://github.com/ActiveTectonicsAndes/ATA
[na]: http://www.geosociety.org/gsatoday/archive/22/10/pdf/i1052-5173-22-10-4.pdf
[ata]: http://www.geosociety.org/gsatoday/archive/22/10/pdf/i1052-5173-22-10-4.pdf
[n_andes]: /images/n_andes_arc_par.png
[htm]: http://rocksandwater.net/blog/2011/07/himatibetmap-1-1/
[andes_kin]: /images/andes_kinematics1.png

[![Alt Text][n_andes]][n_andes]
*Arc-parallel component of the northern Andean GPS velocity field, with faults
from ATA-1.0.  Arrow in ocean is 2 cm/yr.*

Similar to our [HimaTibetMap][htm] database, ATA-1.0 is available in a ArcGIS vector
.shp file, as a Google Earth .kml file, and as a text file (called .gmt, but
it’s ascii) for GMT.  Our hope is that this database is useful not just to
researchers, but to the broader community as well, especially those really
making a difference in education and hazard management.  One of the sobering
things about the database is seeing how many major South American cities are
close to active faults.

Currently it only covers the northern half of the orogen, which is where our
research is focused, but over time we will expand it southward.  And if you’re
knowledgeable about active tectonics in the central and southern Andes, please
contribute!  This is intended to be an open-source project, and we’d love to
have more collaboration.

The second contribution in the paper is the interpretation of the orientation
and kinematics of active faulting, as well as the GPS geodetic velocity field,
as the result of variably-oblique subduction along the western margin of
northern South America.  Basically, because of the convex shape of the margin,
there is a strong oblique component to convergence north and south of the
westward-most point on the trench, where convergence is mostly normal to the
trench.  This results in dextral arc-parallel faulting in northern Ecuador and
Colombia, along the Guaiyaquil-Algeciras fault system, and left-lateral
arc-parallel faulting on various smaller faults in Peru.  Because the
arc-parallel movement is divergent, arc-parallel extension is prevalent where
convergence is arc-normal, in the Gulf of Guayaquil.

[![Alt Text][andes_kin]][andes_kin] 
*Cartoon showing kinematics of oblique convergence and strain partitioning in
the northern Andes. Modified from Veloza et al., 2012*

This is all more fully detailed in the GSA Today article.  Go read it!
