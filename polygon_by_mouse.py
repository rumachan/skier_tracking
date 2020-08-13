#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:54:39 2020

@author: sherburn

Use mouse on a base image to select and save a single polygon.
"""
import cv2
import imutils
import numpy as np

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
       # We want to be able to draw the line-in-progress, so update current mouse position
       current = (x, y)
       #print (current)
    elif event == cv2.EVENT_LBUTTONDOWN:
        # Left click means adding a point at current position to the list of points
        print("Adding point #%d with position(%d,%d)" % (len(points), x, y))
        points.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right click means we're done
        print("Completing polygon with %d points." % len(points))
        print ('Hit ESC to end polygon selection')
        done = True

FINAL_LINE_COLOR = (255, 255, 255)
WORKING_LINE_COLOR = (127, 127, 127)

done = False # Flag signalling we're done
current = (0, 0) # Current position, so we can draw the line-in-progress
points = [] # List of points defining our polygon

img = cv2.imread("initial_without_zones.jpg")
img = imutils.resize(img, width=1200)


#cv2.namedWindow('image')
cv2.imshow('image', img)

# cv2.waitKey(1)
cv2.setMouseCallback('image', on_mouse)


while(not done):
# This is our drawing loop, we just continuously draw new images
# and show them in the named window
    if (len(points) > 0):
        # Draw all the current polygon segments
        cv2.polylines(img, np.array([points]), False, FINAL_LINE_COLOR, 1)
        # And  also show what the current segment would look like
        cv2.line(img, points[-1], current, WORKING_LINE_COLOR)
        # Update the window
    cv2.imshow('image', img)
    #And wait 50ms before next iteration (this will pump window messages meanwhile)
    if cv2.waitKey(50) == 27: # ESC hit
        done = True

# User finised entering the polygon points, so let's make the final drawing
if (len(points) > 0):
        #cv2.fillPoly(img, np.array([points]), FINAL_LINE_COLOR)
        cv2.polylines(img, np.array([points]), True, FINAL_LINE_COLOR)
# And show it
cv2.imshow('image', img)

#write polygon points
print (points)

polyfile = input('Enter name to save polygon file: ')
f = open(polyfile,"w")

for p in points:
    line = ' '.join(str(x) for x in p)
    f.write(line + '\n')
f.close() 

#print ('Any key to end')
cv2.waitKey()
cv2.destroyAllWindows()
