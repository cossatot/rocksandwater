---
Title: The GEM Global Active Faults Database (and Webmap)
author: Richard Styron
date: 2018-10-12
include: leaflet
---

Over the past two years, I have been working for the [Global Earthquake Model 
Foundation (GEM)](globalquakemodel.org). My main task has been building the 
Global Active Faults Database (GEM GAF-DB), which is just what it sounds like—a 
database that contains all of the world's active faults. This work is nearing 
completion; I am doing a few small tweaks to the datasets that compose the 
GAF-DB, as well as the process that assembles the database from the underlying 
datasets, and we are waiting on permissions from some of our collaborators to 
publish the data with the open, permissive licensing that is important to us at 
GEM. These issues should be dealt with soon, and publications presenting the 
database are in progress.


In the mean time, here is an interactive webmap showing the most recent release 
of the data (which is available on GitHub 
[here](https://github.com/GEMScienceTools/gem-global-active-faults/)). You can 
zoom around, click on faults, etc.


<div id="mapid" style="width: 1000px; height: 800px;"></div>

<script>
        var map = L.map("mapid").setView([31.1, 83.3], 4);
        
        map.createPane("labels");
        map.getPane("labels").style.zIndex = 650;
        map.getPane("labels").style.pointerEvents = "none";

        // basemap stuff

        var basemaps = {
            GMRT: L.tileLayer.wms("https://www.gmrt.org/services/mapserver/wms_merc?request=GetCapabilities&service=WMS&version=1.3.0", {
              layers: 'topo',
              attribution: '©GRMT'
            }),
            
            
            OpenMapSurfer_Roads : L.tileLayer('https://korona.geog.uni-heidelberg.de/tiles/roads/x={x}&y={y}&z={z}', {
            	maxZoom: 20,
            	attribution: 'Imagery from <a href="http://giscience.uni-hd.de/">GIScience Research Group @ University of Heidelberg</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }),
        };

        var human_basemaps = {
            "CartoDB OSM": L.tileLayer("http://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png", {
                attribution: '©OpenStreetMap, ©CartoDB',
                opacity: 0.7
            }),

            cartoLabels: L.tileLayer("http://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}.png", {
                attribution: '©OpenStreetMap, ©CartoDB',
                pane: "labels"
            })
        };


        // ISC-GEM Catalog
        var iscGemGjUrl = "https://gist.githubusercontent.com/cossatot/3904da668425cdd8534b7e287d0e1b04/raw/efcf80c6a32fc9b8f7aa3e129ae8c643d1536ac3/ISC-GEM_compact_6+.geojson"
        var eqRenderer = L.canvas({padding: 0.5});




        // faults
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
            "Subduction Thrust": "black",
            "": "green"
        };

        var gafUrl = "https://raw.githubusercontent.com/GEMScienceTools/gem-global-active-faults/master/geojson/gem_active_faults_harmonized.geojson";

        // util functions
        function loadJSON(json_url, callback) {
            var xobj = new XMLHttpRequest();
                xobj.overrideMimeType("application/json");
            xobj.open('GET', json_url, true);
            xobj.onreadystatechange = function () {
                if (xobj.readyState == 4 && xobj.status == "200") {
                    callback(xobj.responseText);
                }
            };
            xobj.send(null);
        }



        loadJSON(gafUrl, function(response) {
            var gafJSON = JSON.parse(response);
            var faults = L.geoJSON(gafJSON, {
                style: function(feature) {
                    if (feature.properties.slip_type != null){
                        return {"color": faultColors[feature.properties.slip_type]};
                    } else {
                        return {"color": "green"};
                    }
                },
                onEachFeature: function(feature, layer) {
                    var attrs = [];
                    for(key in feature.properties) {
                        if (feature.properties[key] != null){
                            attrs.push(key + ": " + feature.properties[key]);
                        }
                    }
                    layer.bindPopup(attrs.join("<br />"))
                }

            })
            .addTo(map);
            
        });


        const iscJson = fetch(iscGemGjUrl);

        iscJson
            .then(iscData => iscData.json())
            .then(data => {
                var eqLayer = L.geoJSON(data, {
                    pointToLayer: function(feature, latlng) {
                        return L.circleMarker(latlng, {
                            renderer: eqRenderer,
                            radius: eqSize(feature.properties.mw),
                            color: feature.properties.color
                        });
                    },
                    
                    onEachFeature: function(feature, layer) {
                    var attrs = [];
                    
                    attrs.push("Event ID: "+feature.properties.eventid);
                    attrs.push("Mw: "+feature.properties.mw);
                    attrs.push("Depth: "+feature.properties.depth+" km");
                    attrs.push("Date: "+feature.properties.date);

                    layer.bindPopup(attrs.join("<br />"))
                    }
                })
                var eq_overlays
                //.addTo(map);
                var eq_overlay = {'Earthquakes (ISC-GEM v.4)': eqLayer}
                var overlays = {"CartoDB OSM": human_basemaps["CartoDB OSM"]}
                L.control.layers(basemaps, 
                                 //human_basemaps.cartoLabels, 
                                 eq_overlay)
                    .addTo(map);
                basemaps.GMRT.addTo(map);
                human_basemaps.cartoLabels.addTo(map);
            })
            .catch(err => console.log(err));


        function eqSize(mw){
            return  0.01 * mw ** 4;
        }


</script>

*The faults are colored by kinematics: blue faults are dextral, red faults are
normal, purple faults are sinistral, black faults are reverse, and grey lines
are contractional structures (i.e. folds) that are not mapped as faults. Green
faults are of unknown kinematics.*


The work itself has been quite enjoyable: a great blend of mapping (in GIS) and
data management. I've made new active fault maps of [Central America and the
Caribbean][ccara], [North Africa][naf], [Northeastern Asia][nea], and modified
existing mapping of [South America][sam] and the Philippines (link coming soon,
hopefully). 

The data management stuff has been interesting as well, in a more limited sort
of way (it's data management, after all). I've been given more or less complete
latitude in deciding how project should be managed, what datasets should be
included, [how faults should be mapped][mapstyle], and how the data should be
combined. It has been fun to assess the state of the data, make a plan, and then
execute on that. I chose to keep the project as simple as possible, adding
complexity only where needed, and to make as much of the project as possible
automated, scripted, and therefore repeatable and reversible. This means that
the many constituent datasets aren't modified unless absolutely necessary, so
information that isn't used or should be used differently won't be lost; it
means that newer versions of individual datasets may be used as they become
available with as little effort as possible, and that datasets may be replaced
with better datasets if those are made available. There is a final 'data
harmonization' step where spatial conflicts between faults of different
datasets are handled (for example, competing representations of a structure or
of an area). This is also done algorithmically, based on a hierarchy of
datasets, and is as mutable as anything else in the process. I've done a fair
amount of programming in ways that are quite unlike the numerical simulations
that I typically do.

Though I did get to map a few orogens, the vast majority of the work was done by
many previous workers. The sources of the datasets we use are below. Please note
that as a fluidly changing project, the references below may be out of date as
new datasets are made available that can supersede those here.

Regardless, I extend my deepest gratitude to the workers in the references below
(and the references used by those references) that have made this possible.


Coverage Region |  Reference  |  Dataset Name (if any)
----------------|-------------|-----------------------
New Zealand     | [*Litchfield et al., 2014*][l14] | *none*
East Africa     | [*Macgregor, 2015*][m15]  | *none*
Middle East     | [*Danciu et al., 2017*][d17] | EMME
South America   | [SARA Faults][sam]     | SARA
Europe          | [*Woessner et al., 2015*][w15] | SHARE
Northern Andes  | [*Veloza et al., 2012*][v12] | Active Tectonics of the Andes
Indo-Asian Collision Zone | [*Styron et al., 2010*][s10] | HimaTibetMap
Philippines     | PHIVOLCS/GEM compilation | *none*
US mainland     | [*Petersen et al., 2008*][p08] | HazFaults
Taiwan          | [*Shyu et al., 2016*][s16] | *none*
Mexico          | [*Villegas et al., 2017*][v17] | *none*
Southeast Asia  | Earth Observatory of Singapore | *none*
Northeast Asia  | [*Styron et al., in prep.*][nea] | *none*
North Africa    | [*Poggi et al., in prep*][naf]  | *none?*
Central America and Caribbean | [*Styron et al., in revision*][ccara] | CCAF
Global (various regions) | [*Christophersen et al., 2015*][c15] | Faulted Earth
Global (plate boundaries) | [*Bird, 2003*][b03] | *none*



[l14]: https://www.tandfonline.com/doi/full/10.1080/00288306.2013.854256
[m15]: https://www.sciencedirect.com/science/article/pii/S1464343X14003240
[d17]: https://doi.org/10.1007/s10518-017-0096-8
[w15]: https://doi.org/10.1007/s10518-015-9795-1
[v12]: http://www.geosociety.org/gsatoday/archive/22/10/abstract/i1052-5173-22-10-4.htm
[s10]: http://geosphere.gsapubs.org/content/7/2/582.short
[p08]: https://pubs.er.usgs.gov/publication/ofr20081128
[s16]: http://tao.cgu.org.tw/index.php/articles/archive/geophysics/item/1376-tao
[v17]: http://dx.doi.org/10.22201/igg.terradigitalis.2017.1.3.50
[c15]: https://link.springer.com/article/10.1007/s11069-015-1831-6
[b03]: https://rmets.onlinelibrary.wiley.com/doi/abs/10.1029/2001GC000252


[ccara]: {filename}../2017/carib_central_am_map.md
[naf]: https://github.com/GEMScienceTools/n_africa_active_faults
[nea]: https://github.com/GEMScienceTools/ne-asia-active-faults
[sam]: https://github.com/GEMScienceTools/SARA-Active-Faults
[mapstyle]: {filename}../2018/mapping-active-faults-for-databases.md
