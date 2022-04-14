---
Title: Global Tectonic Block Model
slug: global-block-model
date: 2021-10-14
---

This is the WORK IN PROGRESS Global Tectonic Block Model that I am building 
with some colleagues and other contacts. The block motions are constrained both 
by geodetic data (GNSS, as well as some InSAR-derived velocity fields using the 
COMET's [LiCSAR] data), and by geologic slip rates.  Expect both block 
geometries and results to change episodically over the next couple of years.  

The viewer below takes the "instantaneous" velocity field (derived from decadal 
geodetic to Quaternary geologic data, so sort of averaged over that timescale) 
and extrapolates it back 5 million years in the past (5 Ma) to 5 million years 
in the future (-5 Ma). This helps me visualize the results and understand what 
is working and what isn't, in a way that just looking at fault slip rates 
output by the model does not. *It is not intended to be a real paleo- or 
future-tectonic reconstruction* as these rotation poles are not time-invariant, 
and the block geometry changes due to deformation. Nonetheless, it is, in my 
opinion, pretty f-in fun to play with.

The primary motivation for this project is to estimate internally-consistent 
slip rates for all of the block-bounding faults (not shown explicitly yet), for 
a revised version of the [GEM Global Active Fault Database](gafdb).

The blocks won't show up until you press 'Draw Blocks' below. There is a decent 
amount of data, and it takes a long time to load, so please wait a few minutes 
if nothing seems to be happening.  Then, you can zoom and scroll around the 
globe, and move the blocks forward and backward in time with the slider at the 
bottom. 

</br>

<div id="block_viewer">

<canvas id="canvas" width="1100" height="1100"></canvas>

<div id="buttons">
    <button id="draw-blocks">Draw Blocks</button>
    </br>
    <!-- <button id="minus">-</button> -->
    <input type="range" min="-5.0" max="5.0" value="0" step="0.25" id="time_slider"
        style="transform: rotateY(180deg)" oninput="time_val.value=value" />
    <!-- <button id="plus">+</button> -->
    <output type="text" id="time_val" value="0"></output> Ma
</div>

<script>
    function showTimeVal(val) {
        document.getElementById('time_slider').value = val;
    }


</script>

<script type="text/javascript" src="https://d3js.org/d3.v5.min.js"></script>
<script type="text/javascript" src="https://unpkg.com/versor"></script>
<script type="text/javascript" src="https://unpkg.com/topojson@3"></script>
<!--<script type="text/javascript" src="/js/2021/main.js"></script>
-->
<script type="text/javascript" src="/js/2021/main.js"></script>
<script type="text/javascript" src="/js/2021/blockrotations.js"></script>

<script>

const blocks_path = 
"https://raw.githubusercontent.com/cossatot/global_blocks/master/web_viewer/blocks.geojson";

const poles_path = 
"https://raw.githubusercontent.com/cossatot/global_blocks/master/web_viewer/poles.csv";

</script>

</div>

</br>

Big thanks to the following people for their contributions, in no particular 
order: Tamarah King, Austin Elliott, Tiegan Hobbs, Murray Journeay, Ömer Emre, 
Zach Lifton, Tim Wright, John Elliott, Chris Rawlins.

I'd like to work on performance but I'm not a javascript wizard.  If you are 
and you want to help, [drop me a line](mailto:richard.h.styron@gmail.com). 
Similarly if you want to contribute positively or hurl vitriol at me, also 
don't hesitate.


[LiCSAR]: https://comet.nerc.ac.uk/comet-lics-portal/
[gafdb]: https://github.com/GEMScienceTools/gem-global-active-faults
