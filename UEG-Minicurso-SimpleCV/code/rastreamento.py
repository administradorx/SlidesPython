#!/usr/bin/env python

#  -*- coding: utf-8 -*-   # permite a?entua??es
 
from SimpleCV import * #importa todo meu FrameWork
from pymouse import PyMouse
 
__author__ = 'Rodrigo Gomes'
 
cam = Camera()    # instanciacao da camera.

p = PyMouse()
 
while True: 
    img = cam.getImage().flipHorizontal()  #captura os frames 
    mascara = img.hueDistance(color=Color.GREEN,minsaturation=140,minvalue=20).invert().threshold(150) #cria mascara
 
    blobs = img.findBlobsFromMask(mascara,minsize=10) #procura obj apartir da mascara
    if blobs: # se existir objetos
        blobs = blobs[-1] # passa o objeto maior
        cod = blobs.coordinates()  # pega as coordenadas do objeto em uma tupla
        blobs.draw(color=Color.RED)
        print "coordenadas do objeto ---> %d  %d" % (cod[0],cod[1])
        p.move(cod[0],cod[1])
        
        
    img = img.applyLayers() # aplica as camadas
    result = img.sideBySide(img,side='right') # divide a tela
    result = img.sideBySide(mascara,side='botton')  #parte 1 da tela ? a mascara
    result.show() #mostra na tela