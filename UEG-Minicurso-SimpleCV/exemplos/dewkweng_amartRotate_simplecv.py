from SimpleCV import *
import time

cam = Camera()


while True:

	img = cam.getImage().scale(0.5).rotate(30,fixed=False)
	i = img.smartRotate().binarize()


	side = img.sideBySide(image=i)




	side.show()

