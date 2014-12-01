#!/usr/bin/env python
# Original Author: Patrick Benz / @Pa_trick17
# Check out the video here:
# http://www.youtube.com/watch?v=cAL6u6Q0Xuc
from SimpleCV import Image, Display
import time
 
#webcam-URLs
marktplatz = 'http://www.tuebingen.de/camera/webcam...'
marktgasse = 'http://leuchtengalerie.com/webcam/leu...'
neckarbruecke1 = 'http://www.tagblatt.de/cms_media/webc...'
neckarbruecke2 = 'http://tuebingen-info.de/fileadmin/we...'
 
display = Display((1240, 960))
 
counter = 0
 
while not display.isNotDone():
img1 = Image(marktplatz)
img1 = img1.adaptiveScale((640, 480))
img2 = Image(marktgasse)
img2 = img2.adaptiveScale((640, 480))
img3 = Image(neckarbruecke1)
img3 = img3.adaptiveScale((640, 480))
img4 = Image(neckarbruecke2)
img4 = img4.adaptiveScale((640, 480))
top = img1.sideBySide(img2)
bottom = img3.sideBySide(img4)
combined = top.sideBySide(bottom, side="bottom")
combined.save(display)
combined.save("webcam" +str(counter).zfill(4) +".jpg")
time.sleep(60)
counter = counter + 1
