#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:22:13 2020

@author: sherburn

Use an initial video, from the start of the tracking process, and add on that
the track lines that the tracked objects will subsequently take. The track lines
come from earlier analysis (tracking) on a video.

The format of the track information is
framenum,time,skier,centrex,centrey
119,7.933333333333334,0,325,157
119,7.933333333333334,1,383,153
We are only interested in showing centrex,centrey for each skier.

"""
import cv2
import pandas as pd
import numpy as np


imgPath = '/home/sherburn/Work/skier_video/initial_with_zones.jpg'
trackPath = '/home/sherburn/Work/skier_video/tracking_data.csv'

#prepare track data
skiers = pd.read_csv(trackPath)
skiernums = skiers['skier'].unique()

#read image
img = cv2.imread(imgPath)

#for each skier, as indicated by their number
for skier in skiernums:
    skitrack = skiers[skiers['skier']==skier] #get that skier's track data
    #transform track centres to required format
    #https://stackoverflow.com/questions/17710672/create-2-dimensional-array-with-2-one-dimensional-array
    x = skitrack['centrex'].values
    y = skitrack['centrey'].values
    pts = np.vstack((x, y)).T
    pts = pts.reshape((-1,1,2))
    #draw track path on image
    cv2.polylines(img,[pts],False,(0,255,255),2)
    cv2.putText(img, str(skier), (x[0],y[0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

#show image
cv2.imshow('Initial image', img)
cv2.imwrite('initial_with_skiers.jpg', img)

#clean up once any key pressed
cv2.waitKey()
cv2.destroyAllWindows()
