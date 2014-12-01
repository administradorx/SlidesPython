from SimpleCV import *
import time


cam = Camera()

while True:

	img = cam.getImage().flipHorizontal().scale(320,240)

	binary = img.binarize().invert()
	edges = img.edges().invert()
	invert = img.invert()


	result = img.sideBySide(binary,side='right')
	result = result.sideBySide(edges,side='right')
	result = result.sideBySide(invert,side='botton')


	result.show() 

