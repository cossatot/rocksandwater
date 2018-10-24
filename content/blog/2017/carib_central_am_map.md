Title: New GEM dataset of active faults in the Caribbean and Central America
Date: 2017-05-31
Slug: c-am-car-faults
Author: Richard Styron
Tags: GIS, active faults, Caribbean, Central America, GEM, PSHA, tectonics, earthquakes

*cross-posted from the [GEM Hazards blog](https://blogs.openquake.org/hazard/)*

The [Global Active Faults][gem-gaf] project of the [GEM Foundation][gem] aims 
to produce a globally complete, reasonably homogeneous dataset of active faults 
on the Earth's surface for seismic hazard assessment. While most deforming 
regions of the world have some publicly available active fault datasets that I 
can stitch together, there are a few significant data gaps. The Central 
American and Caribbean region is one of these regions, despite the great number 
of rapidly-slipping faults and large vulnerable population. 

With help from my colleague Julio Garcia, I have put together a dataset of
active faults in the region, as my contribution to the 
[Caribbean-Central American Risk Assessment (CCARA)][ccara] program. 
The dataset is hosted on 
[GEM's github page][gem-gh] and is publicly available with a Creative Common 
attribution license. There are currently over 200 fault traces in the database. 
These faults span the range from distributed, *relatively* slow intraplate 
deformation to major plate boundary faults. The diversity of faulting here 
reflects the highly variable style of tectonic deformation in the region: many 
styles of deformation are present, with the only consistent theme being that 
these faults slip quite fast.

Today marks the release of [version 1.0][car1.0] of the database.

Check out the interactive web map below showing the most up-to-date version of
the fault database! You can click on the faults to see all the available
information about them.


<script src='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.js'></script>
<link href='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.css' rel='stylesheet' />


<div id="mapid" style="width: 800px; height: 500px;"></div>
<script>

  var mymap = L.map('mapid').setView([15., -75.], 4.5);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);


  var faultColors = {
    "Normal": "red",
    "Sinistral-Normal": "#b936ff",
    "Normal-Sinistral": "red",
    "Reverse": "black",
    "Anticline": "grey",
    "Sinistral-Reverse": "#b936ff",
    "Blind Thrust": "black",
    "Sinistral": "#b936ff",
    "Reverse-Sinistral": "black",
    "Dextral-Reverse": "blue",
    "Dextral": "blue",
    "Dextral-Normal": "blue",
    "Thrust": "black",
    "Dextral Normal": "blue",
    "Sinistral Normal": "#b936ff",
    "Strike-Slip": "yellow",
    "Reverse strike-slip": "black",
    "Thrust strike-slip": "black",
    "Sinistral-reverse": "#b936ff",
    "Strike-slip": "yellow",
    "Strike-slip thrust": "yellow",
    "Strike-slip reverse": "yellow",
    "Dextral-reverse": "blue",
    "Syncline": "grey",
    "Strike-Slip-Normal": "yellow",
    "Normal-Dextral": "red",
    "Reverse-Dextral": "black",
    "Strike-Slip-Reverse": "yellow",
    "Strike Slip": "yellow",
    "Reverse-Strike-Slip": "black",
    "": "green"
  };

  var faults = L.mapbox.featureLayer()
    .loadURL("https://raw.githubusercontent.com/cossatot/central_am_carib_faults/master/geojson/central_am_caribbean_faults.geojson")
    .on('ready', function() {
      faults.eachLayer(function(layer) {
        var out = [];
        for(key in layer.feature.properties){
          // get tooltip
          if (layer.feature.properties[key] != null){
            out.push(key+": "+layer.feature.properties[key]);
            }
          }
        layer.bindPopup(out.join("<br />"));
        });
      })
    .on('ready', function() {
      faults.eachLayer(function(layer) {
        if (layer.feature.properties.slip_type != null){
        //  layer.feature["marker-color"] = "blue";
        //console.log("slip type \n");
          layer.setStyle({"color": faultColors[layer.feature.properties.slip_type]});
        } else {
        // console.log("no slip type \n")
          //layer.feature["marker-color"] = "green";
          layer.setStyle({"color": "green"});
        };
      });
    })
    .addTo(mymap);


</script>
*GEM Central American and Caribbean active fault data. Faults are colored by 
kinematics: blue = dextral, purple = sinistral, black = reverse, red = normal, 
and green = unclassified.*

## Faulting in Central America and the Caribbean

Faulting in the region is largely caused by the interaction between the 
Caribbean plate and the surrounding North American, South American, Cocos and 
Rivera plates. As such, the majority of faults are located within plate 
boundary zones extending up to a few hundred kilometers from the major plate 
boundary faults. For the most part, the majority of strain is taken up on the 
major plate boundary faults (the subduction zone megathrusts and the transform 
faults) but the smaller crustal faults in the distributed deformation zones 
buffering the plate boundaries are still very important to the system, and many 
have quite rapid slip rates despite their short length and/or geomorphic 
obscurity.

The distribution of faults within the crustal deforming zones is very 
influenced by changes in the style (i.e. the rate or kinematics) of plate 
boundary interaction. 

### Faulting and plate convergence obliquity

Faulting in the central Lesser Antilles seems to be dominantly normal faulting 
reflecting arc-parallel extension and the breakup of the forearc into blocks 
that translate along the arc with different velocities [e.g., [*López et al., 
2005*][lopez]]. Near the center of the arc, subduction is relatively orthogonal 
to the trench, but with increasing distance along the arc, subduction becomes 
more oblique (i.e., there is an increasing amount of the strike-slip component) 
due to the curvature of the arc. 

Basic geometric considerations indicate that the amount of arc-parallel 
extension and normal faulting is related to the *rate of change* of obliquity 
along the arc, not the obliquity itself, so arc-parallel extension is highest 
where obliquity is lowest but most rapidly changing, i.e. in the center of the 
arc. However, the amount of arc-parallel translation of forearc blocks is 
directly related to the degree of convergence obliquity.

Mathematically, the amount of arc-parallel translation is the sine of the 
convergence angle (from orthogonal) while the amount of arc-parallel extension 
is the cosine of that angle, i.e. the first derivative of the sine.

This is often difficult to see in subduction zone settings, where the forearcs 
are often mostly underwater and covered by messy volcanoes. However, it is 
pretty clear in the Himalaya, where the entire upper plate (a 
[geometrically-perfect volcano-less 'arc' [*Bendick and Bilham, 2001*]][bend]) 
is subaerial and the faults are more obvious [e.g. [*McCaffrey and Nabelek, 1998*][mcn], [*Styron et al., 2011*][him]].

The rate of change of obliquity in the northern Lesser Antilles is also quite 
high where the plate boundary makes a sharp turn near Puerto Rico, resulting in 
extensional systems bounding rigid blocks with different translation velocities 
such as the Anegada and Mona Rifts [[*López et al., 2005*][lopez], [*Symithe et  al., 2015*][symithe]]. 

This same principal of distributed deformation plays out throughout the Greater 
Antilles as well: where there is a geometric change in the plate boundary, the 
kinematics and distribution of faulting change to reflect this. The islands of 
Hispaniola and Jamaica are both transpressive stepovers along the 
Caribbean-North American transform boundary, and consequently show some 
contractional structures (reverse faults) throughout.

On the western side of the Caribbean plate, the Middle America Trench (where 
the Cocos and Caribbean plates converge) is a bit more linear than the Lesser 
Antilles trench, so changes in Cocos-Caribbean convergence obliquity are less 
pronounced. However, the convergence velocity is quite high, so the 
arc-parallel convergence *rate* changes along strike, and becomes high as well: 
It may reach ~20 mm/yr in Nicaragua. In general it seems to increase to the 
southeast from the North American-Caribbean-Cocos triple junction 'zone' (there 
seems to be no real triple junction point) in Guatemala. Consequently, 
arc-parallel strike-slip faulting increases to the southeast as well [e.g., 
[*Turner et al., 2007*][turner]].

There is a broad zone of extension in between the strike-slip faults separating 
the North American and Caribbean plates, and the Central American and Caribbean 
forearc. This is manifest as an array of normal faults in the highlands of 
southern Guatemala and Honduras. Much of the region's population lives in the 
grabens of these faults, including Guatemala City.


### Central America's missing triple junction

One of the most fascinating aspects of the regional tectonics is the triple 
junction zone between the Caribbean, Cocos and North American plates. The NA-CA 
boundary is defined mostly by the Motagua-Polochic Fault Zone, which dies out 
near the Pacific coast and may merge with the Tonalá fault in Chiapas.

[![Active faults of northern Central 
America]({filename}/images/2017/c_am_fault_map_lo.png)]({filename}/images/2017/c_am_fault_map.png)

Christine Authemayou has written a few papers on this, summarizing the 
possibilities for how the pieces fit together here [[*Authemayou et al., 
2011*][auth11], [*Authemayou et al., 2012*][auth12]]. The gist of it seems to 
be that the NA-CA boundary in the region is diffuse and there may not be much 
relative motion between the northern Central American forearc and the North 
American plate. The alternative, that the Motagua-Polochic fault zone cuts all 
the way to the trench, would potentially offset the trench after a few million 
years, which would be fascinating but this isn't evident in the data.

My pet view of this is that the entire Central American forearc is basically 
transitional between the North American and Caribbean plates, even as far south 
as southern Nicaragua, and may move more with North America than with the 
Caribbean. In a Caribbean-relative reference frame, interseismic GPS vectors in 
the Nicaraguan forearc move westward (towards the trench) rather than eastward, 
as one would näively expect from a somewhat locked, seismogenic subduction zone 
[[*Turner et al., 2007*][turner]]. As far as I know, there hasn't been 
systematic study of this hypothesis as it relates to geodetic or long-term 
block motion, possible slab rollback, etc. but I may find time to work on it in 
the coming year.

It would also be quite interesting to catalog triple junctions globally and see 
how many of them are phantoms, when one looks at them closely.


## About the GEM Central American and Caribbean fault database

The GEM Central American and Caribbean fault database was created with the 
immediate goal of providing data for a fault source model for [Probabilistic 
Seismic Hazard Analysis (PSHA)][psha], as well as serving as a resource for 
characterizing local or regional tectonics for research, education and general 
interest. As such, a minimal set of geologic attributes for the faults in the 
dataset are included that are important in PSHA modeling. These attributes 
primarily describe the fault geometry, kinematics and slip rates of the faults, 
with some additional information such as the primary data source and the 
paleoseismic history of the fault. Though fascinating, the region is 
chronically understudied and much of this information is unavailable for most 
structures, particularly the slip rates and earthquake histories of the faults.

Fault coverage is reasonably good. The bounds of the map area are from Chiapas, 
Mexico through Panama in the west, across the North American-Caribbean plate 
boundary in the north to Cuba, Hispaniola and Puerto Rico, and then south 
through the Lesser Antilles. The southern margin of the region, the South 
American-Caribbean plate boundary, is covered by a few other datasets including 
the [South American Risk Assessment (SARA)][SARA] project and the [Active 
Tectonics of the Andes (ATA)][ata] fault maps, which are included in the GEM 
Global Active Faults dataset.

A few areas need additional mapping. Southern Costa Rica is a hard area to 
work, given the rugged terrain, dense tropical vegetation, and polyphase 
deformation history; mapping here is somewhat incomplete and it's very 
difficult to tell which structures may be active in the current tectonic 
regime. The southern Lesser Antilles have yet to receive sufficient attention, 
in part because many of the probable active structures are offshore. Both of 
these areas are priority areas for GEM, however, so expect more progress on 
this front in the coming months.

Nonetheless, the dataset is definitely usable, for purposes ranging from 
seismic hazard to testing of tectonic hypotheses.

## Contributing

While the Central American and Caribbean active fault dataset has been 
developed by GEM, we welcome contributions from users, whether it is actively 
contributing fault mapping, discussing potential changes to particular 
structures or regions, or providing feedback in terms of what we can do to make 
the data more useful.

The best way to contribute is through the [github page][gem-gh]; simply go to 
the ['Issues'][cam-issues] page and file one (see [here][gh-issues] for an 
explanation of issues). If this isn't an option (for example, you don't have a 
GitHub account), you can reach me by email at 
richard.styron[at]globalquakemodel.org

*This study is made possible by the support of the American People through the
United States Agency for International Development (USAID.) The contents of
this study are the sole responsibility of the GEM Foundation and do not
necessarily reflect the views of USAID or the United States Government.*

[![USAID]({filename}/images/pages/usaid-logo.png)](https://www.usaid.gov)

[gem]: https://www.globalquakemodel.org
[gem-gh]: https://github.com/GEMScienceTools/central_am_carib_faults
[psha]: http://www.earthquakes.bgs.ac.uk/hazard/haz_guide/psha.html
[gem-gaf]: https://www.globalquakemodel.org/what/seismic-hazard/active-faults-database/
[car1.0]: https://github.com/GEMScienceTools/central_am_carib_faults/releases/tag/v1.0

[lopez]: http://onlinelibrary.wiley.com/doi/10.1029/2005GL025293/full
[bend]: http://hs.umt.edu/geosciences/faculty/bendick/documents/pdf/Bendick_Bilham_arc.pdf
[mcn]: https://www.researchgate.net/profile/Rob_Mccaffrey/publication/238313081_Role_of_oblique_convergence_in_the_active_deformation_of_the_Himalayas_and_Southern_Tibet_plateau/links/55d3b67f08ae0a3417226cb8.pdf
[him]: http://rocksandwater.net/pdfs/styron_et_al_2011_geosphere.pdf
[turner]: http://onlinelibrary.wiley.com/doi/10.1029/2006GL027586/full
[symithe]: http://onlinelibrary.wiley.com/doi/10.1002/2014JB011779/full
[auth11]: http://onlinelibrary.wiley.com/doi/10.1029/2010TC002814/full
[auth12]: http://onlinelibrary.wiley.com/doi/10.1029/2012JB009444/full

[SARA]: https://www.globalquakemodel.org/what/regions/south-america/
[ata]: https://github.com/ActiveTectonicsAndes/ATA
[ccara]: https://www.globalquakemodel.org/what/regions/caribbean_c_america/
[gh-issues]: https://guides.github.com/features/issues/
[cam-issues]: https://github.com/GEMScienceTools/central_am_carib_faults/issues
