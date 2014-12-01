#!/usr/bin/python
# -*- coding: utf8 -*-

# exemplo para substituir um rosto!

import time
from SimpleCV import *

cam = Camera() 
troll_face = Image("troll_face.png", sample=True)

while True:
    image = cam.getImage().flipHorizontal().scale(320, 240)
    faces = image.findHaarFeatures("face.xml")

    if faces:
        face = faces[-1] 
        troll = troll_face.scale(face.height(), face.width()) 
        mymask = troll.invert()
        image = image.blit(troll, face.topLeftCorner(),alphaMask=mymask)
    image.show() 
    time.sleep(0.01)
