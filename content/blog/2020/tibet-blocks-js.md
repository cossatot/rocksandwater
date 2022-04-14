---
title: Block model of greater Tibetan deformation in Javascript
author: Richard Styron
date: 2020-11-23
slug: tibet-blocks-js
tags: geology, gis, tectonics, Tibet, geodesy
---


In a [previous post]({filename}tibet-blocks.md), I showed a movie of Tibetan
blocks motions from an inversion of geodetic and geologic data. The movie is
informative, but as I have developed the inversion, I have relied on
[GPlates](gplates.org) to be able to view the motions interactively, i.e. by
panning and zooming, and using a slider to move the blocks back and forth
through time.

I've implemented this in Javascript using the [D3](d3js.org) library.  You can
try it below.  Press 'Draw Blocks' to get started, and then you can pan, zoom
and scroll through time.  The slider at the bottom indicates the time (in Ma, or
million years ago, so negative time is in the future.)

<canvas id="canvas" width="1000" height="800"></canvas>

<div id="buttons">
    <button id="draw-blocks">Draw Blocks</button>
    </br>
    <!-- <button id="minus">-</button> -->
    <input type="range" min="-5" max="5" value="0" step="0.5" id="time_slider" style="transform: rotateY(180deg)"
        oninput="time_val.value=value" />
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
<script type="text/javascript" src="/js/2020/tibet-blocks-js/main.js"></script>
<script type="text/javascript" src="/js/2020/tibet-blocks-js/blockrotations.js"></script>
<script>
    var blocks_path = "/js/2020/tibet-blocks-js/chn_blocks_simp.geojson"
    var poles_path = "/js/2020/tibet-blocks-js/block_poles_eur_rel.csv"
</script>
