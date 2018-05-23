Title: Matplotlib perceptually-uniform colormaps as QGIS color ramps
Date: 2016-07-27
slug: qgis_perceptually_uniform_colorramps
summary: I've taken the new Matplotlib perceptually-uniform colormaps and converted them to QGIS color ramps. Check 'em out!
tags: python, GIS, programming


Due to the [substantial limitations of Python's default colormat Jet][jethate],
a few Python programmers (Stéfan van der Walt, Nathaniel Smith and Eric Firing)
created some perceptually-uniform colormaps for Matplotlib. The benefit of
perceptually-uniform colormaps is that we perceive the color ramp to be linear
(so it doesn't look like there are numerical discontinuities or breaks in slope
in an actually-smooth dataset), the colormap is still very effective for the
many people with colorblindness, and the ramp still works well when printed (or
just viewed) in black and white. See [this nice post][np] for a good comparison
and discussion of the different colormaps. 

I use [QGIS][qgis] quite a bit as my default GIS system (Arc is expensive and
has less interoperability with FOSS geospatial data types). The benefits of
perceptually-uniform color ramps certainly extend to geospatial data and
analysis, so I've ported the color ramps to the QGIS color ramp XML file
([here][ramp_xml]). 

Here are some images (from the blog post linked above) displaying the new
colormaps:

![Magma](/images/magma_colormap.png)
*Magma*

![Inferno](/images/inferno_colormap.png)
*Inferno*

![Plasma](/images/plasma_colormap.png)
*Plasma*

And my favorite,

![Viridis](/images/viridis_colormap.png)
*Viridis*

Here's a map of coseismic slip model of the 2015 Gorkha, Nepal earthquake from
Galetzka et al 2015:

![Gorkha slip](/images/galetzka_slip_viridis.png)


And you can do geospatial analysis in your Lisa Frank fantasy Earth by using
the Inferno color ramp for topography (with topo stresses on the
Tibrikot-Dogari fault shown as well):

![Thakkhola graben](/images/tib_thak_inferno.png)

To install the color ramps, save the file and in the QGIS menu, go to
`Settings` -> `Style Manager` -> `Color ramp` and hit the green Plus sign and
select the file.

```XML
<!DOCTYPE qgis_style>
<qgis_style version="0">
  <symbols/>
  <colorramps>
    <colorramp type="gradient" name="Magma">
      <prop k="color1" v="0,0,3,255"/>
      <prop k="color2" v="251,252,191,255"/>
      <prop k="stops" v="0.04;4,4,21,255:0.08;14,10,42,255:0.12;26,16,65,255:0.16;40,17,89,255:0.20;57,15,110,255:0.23;74,16,121,255:0.27;90,21,126,255:0.31;105,28,128,255:0.35;121,34,129,255:0.39;137,40,129,255:0.43;153,45,127,255:0.47;169,50,124,255:0.51;185,55,120,255:0.55;202,62,114,255:0.59;217,70,106,255:0.62;230,81,98,255:0.66;240,96,93,255:0.70;247,113,91,255:0.74;251,132,96,255:0.78;253,151,104,255:0.82;254,170,116,255:0.86;254,188,130,255:0.90;253,207,146,255:0.94;253,225,163,255:0.98;252,243,181,255"/>
    </colorramp>
    <colorramp type="gradient" name="Inferno">
      <prop k="color1" v="0,0,3,255"/>
      <prop k="color2" v="252,254,164,255"/>
      <prop k="stops" v="0.04;37,5,145,255:0.08;56,4,153,255:0.12;73,2,159,255:0.16;89,1,164,255:0.20;104,0,167,255:0.23;120,1,168,255:0.27;134,7,166,255:0.31;149,17,161,255:0.35;162,28,154,255:0.39;174,39,145,255:0.43;185,51,136,255:0.47;195,62,127,255:0.51;205,73,117,255:0.55;214,85,109,255:0.59;222,96,100,255:0.62;229,108,91,255:0.66;236,120,83,255:0.70;242,133,74,255:0.74;247,146,65,255:0.78;250,160,57,255:0.82;253,175,49,255:0.86;253,190,41,255:0.90;252,206,37,255:0.94;248,223,36,255:0.98;242,240,38,255"/>
    </colorramp>
    <colorramp type="gradient" name="Plasma">
      <prop k="color1" v="12,7,134,255"/>
      <prop k="color2" v="239,248,33,255"/>
      <prop k="stops" v="0.04;37,5,145,255:0.08;56,4,153,255:0.12;73,2,159,255:0.16;89,1,164,255:0.20;104,0,167,255:0.23;120,1,168,255:0.27;134,7,166,255:0.31;149,17,161,255:0.35;162,28,154,255:0.39;174,39,145,255:0.43;185,51,136,255:0.47;195,62,127,255:0.51;205,73,117,255:0.55;214,85,109,255:0.59;222,96,100,255:0.62;229,108,91,255:0.66;236,120,83,255:0.70;242,133,74,255:0.74;247,146,65,255:0.78;250,160,57,255:0.82;253,175,49,255:0.86;253,190,41,255:0.90;252,206,37,255:0.94;248,223,36,255:0.98;242,240,38,255"/>
    </colorramp>
    <colorramp type="gradient" name="Viridis">
      <prop k="color1" v="68,1,84,255"/>
      <prop k="color2" v="253,231,36,255"/>
      <prop k="stops" v="0.04;71,15,98,255:0.08;72,29,111,255:0.12;71,42,121,255:0.16;69,54,129,255:0.20;65,66,134,255:0.23;60,77,138,255:0.27;55,88,140,255:0.31;50,98,141,255:0.35;46,108,142,255:0.39;42,118,142,255:0.43;38,127,142,255:0.47;35,137,141,255:0.51;31,146,140,255:0.55;30,155,137,255:0.59;32,165,133,255:0.62;40,174,127,255:0.66;53,183,120,255:0.70;69,191,111,255:0.74;89,199,100,255:0.78;112,206,86,255:0.82;136,213,71,255:0.86;162,218,55,255:0.90;189,222,38,255:0.94;215,226,25,255:0.98;241,229,28,255"/>
    </colorramp>
  </colorramps>
</qgis_style>
```


[jethate]: https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/

[np]: https://bids.github.io/colormap/

[qgis]: www.qgis.org

[ramp_xml]: https://gist.github.com/cossatot/6fd455d6a2e0e1fdb8ed547dd2176eae

