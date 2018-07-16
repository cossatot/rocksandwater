Title: Mapping active faults for fault databases and seismic hazard analysis
Author: Richard Styron
Date: 2018-07-14
Status: draft

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

*Fault traces should be mapped to best characterize the fault at depth.*

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

For very large faults (hundreds or thousands of kilometers in length), the 
maximum magnitude of an earthquake on the fault may not actually be a 
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
and seismic hazard communities. Unfortunately much of the mapping by the USGS, 
GNS, etc. are really this sort of fault scarp map. Though the mapping itself is 
of high quality, the data can't be used to accurately characterize bedrock 
faults at depth for seismic hazard, structural or tectonic analysis.

Hanging-wall splays are a little bit trickier. Particularly for gently-dipping 
faults, hanging-wall splays can be quite common and are the norm for thrust 
wedges. However, it's not always clear which is the active (or most active) 
strand at the surface, which trace corresponds to the primary fault or basal 
detachment, or whether apparent hanging-wall faults may actually cross-cut the 
shallower fault, which is then inactive.

For thrust belts, the most foreland trace is the most likely to be active given 
typical thrust belt evolution (i.e., this is the active in-sequence structure). 
The more hinterlandward traces may be considered inactive unless there is good 
evidence for out-of-sequence thrusting. The other traces may nonetheless merit 
inclusion based on structure- or project-specific criteria: If substantial 
seismic risk is posed by the structures, or the frontal trace is very 
undeveloped (discontinuous or simply small anticlines, etc.), then they can be 
included. If a 3d seismic source model is being made directly from the data, 
then having multiple faults can be a little tricky: Hanging-wall splays must 
have a lower seismogenic depth that represents the intersection of the two 
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
available. Though I above advocated for continuity of structures, this isn't 
the same as low-resolution mapping.

Variable-resolution mapping is fundamental to GIS-based mapping, unlike paper 
mapping. I commonly map faults at 1:20,000--1:200,000 scale based primarily on 
the resolution of the topography and the clarity of the fault trace in the 
topographic data. It is very easy in some instances to map at 1:5,000 scale in 
Google Earth. If you can get away with this, great. The downsides to mapping 
like this are primarily that the length measurements of a fault trace are 
partially a function of map resolution (high-resolution mapping of curvy fault 
traces will yield longer lengths than low-resolution mapping), 3d projections 
(extrusions, basically) of the traces may not be as planar as in reality, and 
the datasets will be a little larger because of storage of more coordinates. I 
don't think that any of these concerns outweight the case for precisely 
locating the fault trace by mapping at high resolution. It is much easier to 
create simplified geometries if need be from the original dataset than the 
other way around.


# Attributes and GIS format




### Data Table
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


[gaf]: https://github.com/GEMScienceTools/gem-global-active-faults
[ccaf]: https://github.com/GEMScienceTools/central_am_carib_faults
[North Africa]: https://github.com/GEMScienceTools/n_africa_active_faults
[Northeastern Asia]: https://github.com/GEMScienceTools/ne-asia-active-faults
[ata]: https://github.com/ActiveTectonicsAndes/ATA
[HimaTibetMap]: https://github.com/HimaTibetMap/HimaTibetMap
