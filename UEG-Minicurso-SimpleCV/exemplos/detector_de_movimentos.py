from SimpleCV import *

cam = Camera()
threshold = 3.5 # if mean exceeds this amount do something

while True:
	previous = cam.getImage() #grab a frame
	time.sleep(0.5) #wait for half a second
	current = cam.getImage() #grab another frame
	diff = current - previous
	matrix = diff.getNumpy()
	mean = matrix.mean()
	print '%d   %d' % (diff.width,diff.height)
	diff.show()

	if mean >= threshold:
		print "Movimento Detectado!"
