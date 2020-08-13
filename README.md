# skier_tracking
Tracking skiers using drone footage - a project based at Whakapapa skifield, Mt Ruapehu and led by Geoff Kilgour.

Tracking and associated work uses OpenCV called from python scripts. This is a MVP product designed to show the potential usefulness of this technique.

There are three aspects to the work:
- skier tracking
- safe zones and if/when skiers enter them
- summarising where skiers were tracked.

The tracking script produces a file summarsing the tracking information. This can be used for further visualization or analysis.
```
framenum,time,skier,centrex,centrey,safe
37,2.466666666666667,0,380,150,False
37,2.466666666666667,1,530,149,False
37,2.466666666666667,2,595,163,False
37,2.466666666666667,3,588,207,True
37,2.466666666666667,4,488,414,False
37,2.466666666666667,5,399,639,False
```
The coordinate system (reference frame) used is that is the video image. All work has to be done in that reference frame, but it should be possible to later convert that to a 'real' reference frame, and the reverse for safe zones.

## Tracking
Run *multi_tracker.py*.
1. Enter any safezone polygons, one per request.
2. Hit <enter> key to finish that process.
3. Video view opens, showing any safezones in green.
4. Stop the video; press \<s> key.
5. Highlight ROIs (region of interest = skiers) with left mouse, holding down mouse and drawing a small square over the skier.
  
   a. Move to top-left of skier.
   
   b. Hold down left mouse.
   
   c. Move mouse to bottom-left of skier.
   
   d. Release the mouse. A blue box will have been drawn round the skier.
6. Hit \<space> or \<enter> to accept that ROI and to move on to entering another.
7. When all ROIs (skiers) have been selected, hit the \<Esc> key.
8. The video with tracking will then play.
9. Once the video is playing, hitting the \<q> key will terminate the whole video tracking process.
10. If the \<q> is not hit, the video tracking process will continue until the video ends.

## Creating Safe Zones
Run *polygon_by_mouse.py*.
1. This will open an image created by *multi_tracker.py*. That image is from the start of a previous tracking run.
2. Use the mouse to select vertices of a polygon.

   a. Click left mouse at a polygon vertex.
   
   b. Move the mouse to another vertex and click left mouse.
   
   c. Do not try to return to the start point.
   
   c. When all vertices have been entered, hit \<Esc>.
 3. The coordinates of the vertices will be displayed. Enter a filenme to safe the polygon to.
 4. Move your cursor back to the video screen and hit the \<q> to terminate the process.

 ## Visualizing Tracks
 ![skier tracks](reference_images/initial_with_skiers.jpg?raw=true "Title")
 
 Start position of skiers is outlined and numbered. A path, shown in yellow, marks where they moved while being tracked.

 Run *tracks_on_start_image.py*.
 1. Uses *initial_with_zones.jpg* only.
 2. TRacking output uses *tracking_data.csv* only.
 3. No user input required
