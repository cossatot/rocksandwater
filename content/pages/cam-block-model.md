---
Title: Central America and Caribbean Block Model
slug: cam-block-model
date: 2022-04-14
---

This is the WORK IN PROGRESS block model for Central America and the Caribbean.  
The block model extrapolates instantaneous block motions forward and back in 
time, to better visualize their current motions. This is not mean to accurately 
represent past or future geographies.

Press 'Draw Blocks' below to get started.  You may have to wait a minute or two 
for the data to load.  Then you can click on the globe and drag it around and 
zoom, and you can move the plates forward and back through time with the slider 
below.

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
"https://raw.githubusercontent.com/cossatot/cca_blocks/master/web_viewer/blocks.geojson";

const poles_path = 
"https://raw.githubusercontent.com/cossatot/cca_blocks/master/web_viewer/poles.csv";

</script>

</div>

</br>


