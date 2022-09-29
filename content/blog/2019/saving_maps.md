---
title: How to make high-resolution maps while reducing file size in ArcGIS and Adobe
subtitle: A tutorial by your concerned colleague with a slow internet connection and limited disk space
author: Lydia Staisch
date: 2019-11-23
slug: high-resolution-maps-low-file-size-arcgis-adobe
---

*A guest post by the Figure Master [Lydia Staisch][lms]*

Here is a map! It's LiDAR and scaled to a poster size of 45"x30" -- it
has the potential to be an absolutely monstrous file size when exported.

![]({static}/images/2019/saving-maps/Picture1.png)

<!-- PELICAN_END_SUMMARY -->

First, we of course have to save it. Use File -> Export

![]({static}/images/2019/saving-maps/Picture2.png)

Change the resolution to 300 DPI (usually sufficient!) and save as an
.ai file.

![]({static}/images/2019/saving-maps/Picture3.png)

Your new .ai file will be large, but we'll fix that soon.

![]({static}/images/2019/saving-maps/Picture4.png)

Open your new .ai file in Adobe Illustrator. In the "Layers" tab, you
can find the raster of your topographic layer. It's usually called
"Image"

![]({static}/images/2019/saving-maps/Picture5.png)

Annoyingly, the rasters are all saved as these tiny horizontal strips.
Gross!

![]({static}/images/2019/saving-maps/Picture6.png)

To fix that, we first need to remove the clipping masks. Go to Select
Object Clipping Masks. This will select all the masks in your .ai file.
Then, simply press Delete.

![]({static}/images/2019/saving-maps/Picture7.png)

Now you can select all these tiny horizontal rasters easily.

![]({static}/images/2019/saving-maps/Picture8.png)

Next, you want to Rasterize these layers, effectively making one raster
out of many. Go to Object -> Rasterize.

![]({static}/images/2019/saving-maps/Picture9.png)

Then select the resolution. Again, 300 is good. No reason to set it
higher than what you initially saved it as. Also select "Transparent"
for the background.

![]({static}/images/2019/saving-maps/Picture10.png)

If you want a higher resolution, just chose "Other" and type it in.

![]({static}/images/2019/saving-maps/Picture11.png)

Once you've made all the changes you want to the map, save it as an .eps
file

![]({static}/images/2019/saving-maps/Picture12.png)

You'll notice that it's still a huge file, that's fine.

![]({static}/images/2019/saving-maps/Picture13.png)

To reduce the size and save as a .pdf file, open the .eps in Acrobat
Distiller.

![]({static}/images/2019/saving-maps/Picture14.png)

WHOA. Check out your tiny file size.

![]({static}/images/2019/saving-maps/Picture15.png)

And it still looks beautiful!


![]({static}/images/2019/saving-maps/Picture16.png)


[lms]: https://www.usgs.gov/staff-profiles/lydia-m-staisch