---
Title: Mapping active faults for fault databases and seismic hazard analysis
Author: Richard Styron
Date: 2018-07-18
Tags: tectonics, research, active faults, PSHA, GIS, GEM, open science
...

*cross-posted from the GEM Hazard Blog*


I've had several conversations with geologists recently who are considering 
creating new active fault databases (or datasets). These geologists are all 
government scientists who are interested in both tectonics research and seismic 
hazard, and would like to make maintainable databases that suit both purposes 
and can easily interface with other regional or larger-scale databases.

This is a domain that I've worked in extensively over the past two years as I 
have constructed the [GEM Global Active Fault Database][gaf] (GAF). The GAF is 
a synthesis of existing datasets, as well as new datasets that I have mapped in 
regions where no suitable public fault databases exist: [Central America and 
the Caribbean][ccaf], [North Africa], and [Northeastern Asia].

Here, I offer some guidelines for the construction of these types of databases, 
based on this mapping and database construction experience, as well as previous 
work on the [HimaTibetMap] and [Active Tectonics of the Andes][ata] databases 
(which were oriented more towards tectonic research than seismic hazard). These 
guidelines are general, and shouldn't be applied dogmatically. Geology is rife 
with exceptions, and many individual cases will call for decisions other than 
the ones promoted here. Use your judgement.

# Mapping active faults

Active fault maps are generally vector (line) GIS data representing the fault 
trace, with additional (i.e., subsurface) information contained as attributes. 
The most common are the dip direction and angle. Kinematic information (either 
numerical rake values, kinematic categories such as reverse, sinistral, etc., 
or both) and other important informtion are similarly included, and will be 
covered below.

## Active fault representation and trace continuity

*__Fault traces should be mapped to best characterize the fault at depth.__*

### Fault trace continuity

Fault should be mapped as continuous traces that represent the surface 
expression of the bedrock fault plane at depth. The trace should define an 
independent seismic source[^1], such that a full rupture of the fault plane 
represented by this trace will host the maximum magnitude earthquake on the 
fault (discounting the contribution from other segments in multi-segment or 
multi-fault ruptures). If the fault is very long, possibly with real geometric 
complexity, but there is most likely a continuous fault plane at depth, map it 
as such regardless of putative rupture segmentation of the fault. 

The canonical example of a fault with these sorts of complications is the 
Wasatch Fault in Utah. In my professional opinion it should be mapped as a 
single, continuous structure, as there has to be a continuous (not necessarily 
unique) fault plane at depth that has accommodated kilometers of slip. Though 
it is not a planar fault, and surely has many anastomosing strands and other 
complications, ruptures in all likelihood can float along it, breaching segment 
boundaries.

[![Ruby Mountains fault representations][ruby_svg]][ruby_svg]
*__Figure 1__: Different representations of faulting in the Ruby Mountains, NV 
USA. __a__: Faults from the USGS Quaternary Faults and Folds ([Qfaults]) 
database. Individual fault traces represent surface deformation, not the trace 
of the major seismogenic bedrock structures. __b__: Example of mapped fault 
traces that represent continuous traces indicating fault continuity at depth, 
capable of supporting floating ruptures all along the structure. Mapping by me 
(R. Styron) as an example for this post; no field investigation was performed.*


For another example, see Figure 1, which is a map of the Ruby Mountains, 
Nevada. In subfigure a, the USGS [Qfaults] data is shown. In subfigure b, I 
have drawn traces on 30m SRTM imagery that represent what I'm interpreting as 
continuous faults at depth that characterize the fault surfaces along which the 
mountains rose, and which are capable of hosting hazardous earthquakes. Please 
note this was done quickly for this work and doesn't represent professional 
fault or hazard characterization of north-central Nevada.

For very large faults (hundreds or thousands of kilometers in length), the 
maximum magnitude of an earthquake on the fault may be much smaller than a 
full-length rupture. In this case, the maximum magnitude for seismic hazard 
assessment should be set independently instead of through the automated use of 
a scaling relationship.

Breaking continuous traces into separate, contiguous segments (i.e. separate 
features in the GIS file) may be justifiable in some instances. The most 
obvious is when major attributes such as kinematics, dip, or slip rate change. 
Again, use your judgement.

### Secondary faults and other deformation

Small splays, discontinuous scarps, and similar signs of off-fault or 
hanging-wall deformation or rupture complexity should not be mapped in an 
active fault map, as these small features don't represent individual seismic 
sources. For certain types of study or hazard analysis (fault displacement 
hazards, or high-resolution site assessment) this may be appropriate but in 
general this is an improper characterization of the causative faults. 
Additionally this kind of mapping may be important for earthquake research 
purposes, ground motion studies, etc. There is certainly value in making 
high-resolution maps of ground deformation but this is a separate type of data 
than an active fault map as understood (and required) by many in the tectonics 
and seismic hazard communities. Unfortunately many of the maps by the USGS, 
GNS, etc. are really this sort of fault scarp or surface deformation map. 
Though the mapping itself is of high quality, the data can't be used directly 
to accurately characterize bedrock faults at depth for seismic hazard, 
structural or tectonic analysis; instead, simplified representations need to be 
created later for use in seismic hazard models.

Hanging-wall splays are a little bit trickier. Particularly for gently-dipping 
faults, hanging-wall splays can be quite common and are the norm for thrust 
wedges. However, it's not always clear which is the active (or most active) 
strand at the surface, which trace corresponds to the primary fault or basal 
detachment, or whether apparent hanging-wall faults may actually cross-cut the 
shallower fault, which is then inactive.

For thrust belts, the most forelandward trace is the most likely to be active 
given typical thrust belt evolution (i.e., this is the active in-sequence 
structure). The more hinterlandward traces may be considered inactive unless 
there is good evidence for out-of-sequence thrusting. The other traces may 
nonetheless merit inclusion based on structure- or project-specific criteria: 
If substantial seismic risk is posed by the structures, or the frontal trace is 
very undeveloped (discontinuous or simply small anticlines, etc.), then they 
can be included. If a 3d seismic source model is being made directly from the 
data, then having multiple faults can be a little tricky: Hanging-wall splays 
must have a lower seismogenic depth that represents the intersection of the two 
faults. It's also not straightforward to either distribute slip rate, or 
individual ruptures, between the branches of a fault and the main fault at 
depth.

These issues are less of a concern with normal faults. Hanging-wall splays are 
not uncommon above low(er) angle normal faults, but they are often in 
unconsolidated sediments so they may not radiate much seismic energy when they 
slip, and they may simply result from shallow slip deficits on the main fault. 
They often merge with the main fault at depths of less than 2 km.
Given this, they rarely merit inclusion in an active fault database intended 
for hazard work.

[^1]: The science on what, if anything, constitutes an independent seismic 
source is far from settled. The same can be said for what a 'fault segment' is, 
and the degree to which faults can have persistent, independently-rupturing 
contiguous segments. But if you, as a fault mapper, ever want to get your job 
done, don't get caught up in these sorts of issues. I don't think these 
questions will be satisfactorally resolved in my lifetime. Just map the fault 
and if issues arise, deal with them on a case-by-case basis.

### Map resolution

Fault traces should be mapped at the highest resolution possible given the 
scope of the project, the quality of the underlying datasets, and the time 
available. Though I advocated above for continuity of structures, this isn't 
the same as low-resolution mapping.

Variable-resolution mapping is fundamental to GIS-based mapping, unlike paper 
mapping. I commonly map faults at 1:20,000—1:200,000 scale, based primarily on 
the resolution of the topography and the clarity of the fault trace in the 
topographic data. It is very easy in some instances to map at 1:5,000 scale in 
Google Earth. If you can get away with this, great. The downsides to mapping 
like this are primarily that the length measurements of a fault trace are 
partially a function of map resolution (high-resolution mapping of curvy fault 
traces will yield longer lengths than low-resolution mapping), 3D projections 
(extrusions, basically) of the traces may not be as planar as in reality, and 
the datasets will be a little larger because of storage of more coordinates. I 
don't think that any of these concerns outweigh the case for precisely locating 
the fault trace by mapping at high resolution. It is much easier to create 
simplified geometries from the original dataset, if need be, than the other way 
around.


# Attributes and GIS format

*__Start simple, and add complexity as needed.__*

Fault data have much more information than just the coordinates of the trace. 
Additional characterization of a fault's geometry, kinematics, slip rate, 
earthquake history, the state of knowledge (and uncertainty) of these 
parameters, and any references for academic or other focused study of the fault 
are all important. 

However, it can be difficult to decide what information to include, and how to 
best format this. These difficulties are compounded by the amount and quality 
of information available, which depends quite a bit on the region of study and 
the relative importance of individual structures in a region. Consequently, a 
range of approaches from quite minimal (e.g., just fault traces, hopefuly with 
kinematics) to maximal (e.g., separate fields for geodetic slip rates and 
neotectonic slip rates) exists in different datasets; certainly different 
project goals and the project manager's preferences have influence as well.

At GEM, the previous [Faulted 
Earth](https://docs.wixstatic.com/ugd/1dcea4_e741a0e20e2c43a4aca1a94d77a8e3f6.pdf) 
project chose a very maximal representation, in order to capture all the 
information that a field geologist could record. This codified and presented a 
comprehensive framework for a huge amount of information, but in practice was 
unwieldy: entering data was very tough because there were so many fields, and 
the data tables took a huge amount of disk space to record the many `NULL` 
values for all of the missing data, as the vast majority of fields were unknown 
or inapplicable for most structures.

Consequently, for the [GAF][gaf] project, I chose a much more compact schema 
that still holds the minimal amount of information to build a seismic source 
(aside from a few project-level defaults), and characterize the relevant 
uncertainties as well. This is presented in the data table below:


Attribute            | Data Type | Description                  | Example
---------------------|-----------|------------------------------|------------
dip                  | tuple     | Dip                           | (40,30,50)
dip_dir             | string    | Dip direction                 |         W 
downthrown_side_id | string    | direction of downthrown side  |        NE 
average_rake        | tuple     | Slip rake of fault            | (45,25,55)
slip_type           | string    | Kinematic type                | Sinistral  
strike_slip_rate   | tuple     | Strike slip rate on fault   |(1.5,0.5,2.5)
dip_slip_rate      | tuple     | Dip slip rate               |(1.5,0.5,2.5)
vert_slip_rate     | tuple     | Vertial slip rate           |(1.5,0.5,2.5)
shortening_rate     | tuple     | Horizontal shortening rate  |(1.5,0.5,2.5)
upper_seis_depth    | tuple   | Upper depth of sesmic release |(0.,,)
lower_seis_depth    | tuple   | Lower depth of sesmic release |(12.,,)
accuracy            | integer   | Denominator of map scale    |       40000
activity_confidence | integer   | Certainty of neotectonic activity |     1 
exposure_quality    | integer   | How well exposed (visible) fault is |   2 
epistemic_quality   | integer   | Certainty that fault exists here |      1 
last_movement       | string    | Date of last earthquake       |     1865  
name                 | string    | Name of fault zone            | Polochic  
fz_name             | string    | Name of fault zone    | Motagua-Polochic   
reference            | string    | Paper used        | Rogers and Mann, 2007 
notes                | string    | Any relevant info | May be creeping
ogc_fid              | integer   | ID used by GIS    |                    8
catalog_id           | string    | Global ID         |               CCARA_8


### Data types

There are a few data types given here:

  - `tuple`: This data type represents *continuous random variables*[^2] in a 
    tuple (ordered sequence) format. In the GEM databases, tuples are given 
    values for the `(most likely, minimum, maximum)` for each variable, which 
    more or less represent a triangular probability distribution. If no 
    variability is necessary, the tuple is represented as `(most likely,,)`. 
    The use of a tuple instead of a single field for each parameter lets us 
    keep the number of fields in the database down, which reduces file size and 
    makes data entry faster. It does mean that some additional parsing 
    functions have to be written to perform quantitative analysis. Individuals 
    or organizations with different needs can choose a format that suits their 
    needs.

  - `string`: Strings (i.e. a sequence of characters in computer science terms) 
    represent textual data of any sort.

  - `integer`: Integers in the GEM fault datasets are for categorical variables 
    or indices. The categorical variables define levels of uncertainty: `0` is 
    well known, `1` less so, and `2` very poorly known.

[^2]: A *continuous random variable* is a number that may take any value 
between some minimum and maximum including negative and positive infinity. This 
may be due to either a lack of firm knowledge (epistemic uncertainty) or 
natural variability (aleatoric variability). A *discrete random variable* is a 
random variable that may take a value from some discrete (non-continuous) set 
of values, but no values in between (if they exist). A dice roll, for example, 
is a discrete random variable. Categorical random variables are as well; an 
example is the day of the week I was born on—I don't know this off-hand but it 
was almost certainly one of the seven days I learned in school.


## File formats

Active fault databases are almost always given as GIS vector files. The type 
tends to be `line`, representing the fault trace, although often there are 
`polylines` that represent multiple segments of the same trace. Occasionally 
there will also be 3-dimensional representations of the fault planes, such as 
the [SCEC Community Fault Model](https://www.scec.org/research/cfm). Consistent 
with the mapping advice provided above, we don't recommend the use of 
`polyline` types; a single fault feature should have a continuous trace and set 
of attributes. The same applies to 3D fault surfaces.

Of the GIS vector formats, several are appropriate and several others less so. 
Unfortunately, the vector format most commonly used by GIS users is the ESRI 
ShapeFile, which is an outdated binary format with a host of limitations (the 
10-character limit on attribute names is the most glaring, though the large 
number of files for each ShapeFile is also a pain).

At GEM, we use the [GeoJSON](http://geojson.org) format, which is 
plain-text—based and very flexible, and able to be edited as a native format in 
[QGIS](qgis.org) which is our GIS platform of choice. The plain-text nature is 
quite beneficial: You can open a GeoJSON file with a text editor to inspect or 
modify values (no need to load it into a big application), it's easy to load 
into a programming environment such as Python or MATLAB, and it can be put 
under version control with [git](git-scm.com) to track and coordinate edits. 
Additionally, it's the native format of web mapping and is widely supported, 
though ArcMap doesn't support it (which is pathetic).

Another great format is the GeoPackage format, which is a SQLite-based 
geodatabase format. It is a bit more structured than GeoJSON (columns are have 
defined data types, for example) because it's a real database instead of a flat 
file format, but it's widely supported and often results in much smaller file 
sizes than other formats. Theoretically it can be converted into ESRI file and 
personal geodatabases although I haven't tried. I am pretty sure ESRI supports 
it natively, and because it's SQLite, any programming environment should be 
able to work with it quite easily. A single GeoPackage database can also hold 
raster layers, which means that you can have everything you need for a small 
project in a single file, which is nice.

A blank GeoPackage database with an empty layer, but with the data schema given 
above, can be downloaded [here][gpkg_db].

Other vector formats, such as KML or GMT, aren't really suitable for editing 
and data access but are great for their visualizations in Google Earth and GMT. 
It's extremely easy to export the 'main' format to these after editing.

Some organizations choose to host their databases in more complicated setups, 
including PostgreSQL or other configurations with multiple tables, 
client-server roles, etc.; this may be done over a web server as well. There is 
certainly nothing wrong with this if it suits the archival data delivery needs 
of an institution, but it's really overkill for the purposes of mapping and 
seismic hazard work. There are very few places that have many people who may be 
editing the data simultaneously. Even in this instance, by mapping in GeoJSON 
with QGIS and with the data tracked using git or mercurial and hosted on a 
server somewhere, it's possible to deal with multiple users creating and 
editing data quickly and easily, using pull requests, branches, etc. Fault data 
aren't instrumental data where events are recorded and automatically put into a 
table by computers. The datasets also take up a few MB, not GB (or more).

## Version control

As mentioned above, a text-based format such as GeoJSON allows the editors to 
track revisions using git or mercurial. Then, any git/hg server can be used to 
coordinate edits among many mappers, especially if good software development 
practices are involved, such as using topic branches and pull requests to 
review and merge changes. Furthermore, that server can be used to disseminate 
the data to the community as well, if it's public-facing. I find it very useful 
to host the fault databases I maintain on GitHub, so that it is very easy for 
anyone to access the data, we have automatic offsite backup, and I can edit 
from many different computers without having to pass around a file on a flash 
drive or whatever. Currently, no one else is actively making and submitting 
edits to the datasets, but this platform seamlessly integrates this 
functionality as well. But because of this, I tend to just make commits to the 
master branch and not use topic branches or pull requests.



# Summary and conclusions

Active fault databases for use in seismic hazard, geological research and 
education can be built quickly in a GIS platform. Two basic principles apply:

 1. *Fault traces should be mapped to best characterize the fault at depth.*

 2. *Start simple, and add complexity as needed.*

 By following these principles (and breaking them only as needed), it's easy 
 for an organization to maintain a useful and modular fault database.




[gaf]: https://github.com/GEMScienceTools/gem-global-active-faults
[ccaf]: https://github.com/GEMScienceTools/central_am_carib_faults
[North Africa]: https://github.com/GEMScienceTools/n_africa_active_faults
[Northeastern Asia]: https://github.com/GEMScienceTools/ne-asia-active-faults
[ata]: https://github.com/ActiveTectonicsAndes/ATA
[HimaTibetMap]: https://github.com/HimaTibetMap/HimaTibetMap
[ruby_svg]: {filename}/images/2018/ruby_compare_big.svg
[Qfaults]: https://earthquake.usgs.gov/hazards/qfaults/
[gpkg_db]: {filename}/uploads/master_df_schema.gpkg
