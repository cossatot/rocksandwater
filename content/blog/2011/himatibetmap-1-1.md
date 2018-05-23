Title: HimaTibetMap-1.1: An expanded and updated version of the Database of Active Faults from the Indo-Asian Collision Zone- for ArcGIS, GMT, and Google Earth
Date: 2011-07-28
slug: himatibetmap-1-1
tags: active faults, GIS, Tibet

*This was a post that originally appeared on my 
[old blog](http://rocksandwaterdotnet.wordpress.com).  Please note that I have
left the post the way it was in 2011, except for the GitHub announcement I
made in May 2013; however, please get the HimaTibetMap database from GitHub
instead of the KU Hawkdrive, as that older version is no longer maintained.*

**Edit 2 May 2013:** [HimaTibetMap is now in GitHub!][gh_post]

I am pleased to announce the updated version of [HimaTibetMap-1.1][htmku].
HimaTibetMap is a database of active faults from the Indo-Asian collision zone,
spanning from Iran to Myanmar, and India to Siberia, and contains over 1000
structures.  The area covered is approximately the same size as the contiguous
US.  It was originally compiled by Mike Taylor and An Yin based on their field
observations, remote sensing analysis, and reviews of the literature, as
described in [Taylor and Yin (2009)][ty09]. It was since updated slightly by
Mike and myself, and released to the public as outlined in our [Eos article
from May 2010][eos].

[![Alt Text][bigmap]][bigmap]
*Map showing the extent of HimaTibetMap-1.1 made in ArcMap with topography from SRTM.*

The database is available for ArcGIS, GMT, and Google Earth.  The Shapefile
version (for ArcGIS; but it’s compatible with Quantum GIS, Grass, and many
other programs) is the original version and contains the most information, due
to the nature and capability of that file type.  Kinematics for each structure
are easily displayed using the GPSec.style file that is included in the .zip.

[![Alt Text][zoom]][zoom]
*Structures of the Tibetan plateau*

I have used all quite frequently in my work, though I imagine the Google Earth
(kml) version would be the one most favored by those not doing academic
research in the region. It is incredibly fun to cruise around the orogen and
see all the faults on top of the topography!  The structures in Google Earth
contain much of the metadata of the Shapefiles, as well, so you can click on
the structures and see the type of structure, references (if any), etc.

[![Alt Text][kml]][kml] 
*Oblique view of the Nepal Himalaya and southwestern
Tibetan plateau in Google Earth. Normal faults are shown in red, strike slip
faults in blue, and thrust faults in white.*

The new version, 1.1, is largely similar to 1.0, except for the addition of
20-30 new structures. Most of these are rifts in southern Tibet and the
Himalaya. The most (structurally) significant of these are the Leo Pargil and
Ama Drime metamorphic core complexes, accommodating arc-parallel extension of
the Himalaya.  There are also quite a few smaller rifts on the Tibetan plateau
(mostly in south Tibet near my field area) that have been added, and minor
changes have been made to several others.

Some other, less geologic changes are that the suture zones and borders of
Cenozoic volcanics have been given their own Shapefile, for the Arc users. This
allows them to have different symbology than that specified by the .style file.
The .style file intended for this database has also been included in the zip
file as well, as it’s no longer readily available on the Internet as it was
when the Eos article was submitted.

HimaTibetMap-1.1 can be found on the KU Hawkdrive, which is here:
[https://documents.ku.edu/collaboration/Geologic%20Data%20in%20Tibet/HimaTibetMap-1.1][htmku]

**Edit 3 May 2013:** The maintained version is [now on GitHub][gh]

Other potential improvements to the database are making the volcanic
distributions into polygon shapefiles, having information on slip rate,
initiation age, and other similar information for structures (although
currently this data is sparse and hotly contested…) and maybe expanding to the
northeast (Baikal region) and the west (into Iran).

If you have any requests for this database, such as certain structures,
regions, file types, etc., please let me know!  I will be happy to accommodate.
Also, any comments are also welcome.

And although this database is open to the public, if you use it in a scientific
publication (including posters and oral presentations at talks), please cite
us!  The proper citation is the Eos paper:

Styron, R., Taylor, M., & Okoronkwo, K. (2010). Database of active structures
from the Indo-Asian Collision. *Eos Trans. AGU, 91*(20), 0-1. doi:
10.1029/2010EO200001

although citing Taylor and Yin (2009) is also recommended.

Enjoy!




[gh]: https://github.com/HimaTibetMap/HimaTibetMap
[gh_post]: http://rocksandwater.net/2013/05/03/himatibetmap-now-on-github/
[htmku]: https://documents.ku.edu/collaboration/Geologic%20Data%20in%20Tibet/HimaTibetMap-1.1
[ty09]: http://geosphere.geoscienceworld.org/cgi/content/abstract/5/3/199
[eos]: http://www.agu.org/journals/eo/eo1020/2010EO200001.pdf
[bigmap]: /images/himatibetmap111.png
[zoom]: /images/himatibetmap11_zoom1.png
[kml]: /images/s_tibet_himatibetmap_kml.jpg
