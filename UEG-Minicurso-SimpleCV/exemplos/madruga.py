#!/usr/bin/python
# -*- coding: utf8 -*-

# exemplo para substituir um rosto!

import time
from SimpleCV import *

cam = Camera() 
madruga_face = Image("madruga.jpg")

while True:
    img = cam.getImage().flipHorizontal().scale(320, 240)
    faces = img.findHaarFeatures("face.xml")

    if faces:
        face = faces[-1]
        madruga = madruga_face.scale(face.height(), face.width()) 
        mymask = madruga.invert()
        img = img.blit(madruga, face.topLeftCorner(),alphaMask=mymask)
    img.show() 
    time.sleep(0.01)
