#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:15:22 2020

@author: sherburn

This is working version of multi-skier tracking.
Includes safe zones.
Includes saving skier details, with in/out of safe zone.
Multiple safe zones possible
"""
import imutils
import cv2
import pandas as pd
import numpy as np

def rectdata(x, y, w, h):
    #posiion rectangle given bounds
    centrex = int(x+w/2)
    centrey = int(y+h/2)
    return (centrex, centrey)

videoPath = '/home/sherburn/Work/skier_video/video_files/FFnostabfps15.mp4'

#input safe zones polygons
print ('Add any safe zones for tracking analysis')
safelist = []
while True:
    infile = input("Enter filename for a safezone (Enter to quit): ")
    if not infile:
        break
    #format safe zones for display
    poly = np.loadtxt(infile).astype(int)
    poly = poly.reshape((-1, 1, 2))
    safelist.append(poly)

# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()
cap = cv2.VideoCapture(videoPath)

#dataframe for rectangle data
dfrect = pd.DataFrame() #for each rectangle

print ('\nSetting up object tracking\n') 
#loop for the video
while cap.isOpened():

    ret, frame = cap.read()
    if frame is None:
        break

    frame = imutils.resize(frame, width=1200)
    cv2.imwrite('initial_without_zones.jpg', frame)
    (success, boxes) = trackers.update(frame)
    
    #get stuff about video frames
    fnum = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) #frame number
    fps = int(cap.get(cv2.CAP_PROP_FPS)) #frame per second
    efftime = fnum/fps #calculate effective time (seconds)
    
    #draw safezone on image, in green
    for safe in safelist:
        cv2.polylines(frame,[safe],True,(0,255,0),2)
       
    # loop over the bounding boxes and draw them on the frame
    #label boxes with their box number (in red)
    for bnum,box in enumerate(boxes):
        (x, y, w, h) = [int(v) for v in box]
        #if centre of frame outside safe zone, draw in red, inside draw in green
        (centrex, centrey) = rectdata(x, y, w, h)
        issafe = False
        for safe in safelist:
            if (cv2.pointPolygonTest(safe, (centrex, centrey), False) > 0 or issafe): #safe
                issafe = True
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #unsafe
                issafe = False
        cv2.putText(frame, str(bnum), (int(x+w),int(y+h/2)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        
        #put position and other data in dataframe
        # (centrex, centrey) = rectdata(x, y, w, h)
        d = {'framenum':fnum, 'time':efftime, 'skier':bnum, 'centrex':centrex, 'centrey':centrey, 'safe':issafe}
        df = pd.DataFrame(data=d, index=[0])
        dfrect = dfrect.append(df)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
     
    # if the 's' key is selected, we are going to "select" a bounding box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        box = cv2.selectROIs("Frame", frame, fromCenter=False,
                             showCrosshair=True)
        box = tuple(map(tuple, box))
        
        for bb in box:
            # tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            tracker = cv2.TrackerCSRT_create()
            trackers.add(tracker, frame, bb)
        #write snapshot of image at tracking start
        cv2.imwrite('initial_with_zones.jpg', frame)
            
    # if you want to reset bounding box, select the 'r' key 
    elif key == ord("r"):
        trackers.clear()
        trackers = cv2.MultiTracker_create()

        box = cv2.selectROIs("Frame", frame, fromCenter=False,
                            showCrosshair=True)
        box = tuple(map(tuple, box))
        for bb in box:
            # tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            tracker = cv2.TrackerCSRT_create()
            trackers.add(tracker, frame, bb)
                
    #if the 'p' key is selected pause, until any other key
    elif key == ord('p'):
        cv2.waitKey(-1) #pause until any key is pressed
    
    #if the 'q' key is selected quit
    elif key == ord("q"):
        break

#save rectangle dataframes to csv
dfrect.to_csv('tracking_data.csv', index=False)

cap.release()
cv2.destroyAllWindows()