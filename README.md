# skier_tracking
Tracking skiers using drone footage.

A project based at Whakapapa skifield, Mt Ruapehu.

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
 Run *tracks_on_start_image.py*.
 1. 
