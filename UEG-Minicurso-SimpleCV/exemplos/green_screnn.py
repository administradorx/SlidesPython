'''
This program takes a person standing in front of a green screen
and then removes the background and inserts a new one
'''
print __doc__

from SimpleCV import *

sleep_time = 2 #the amount of time to show each image for

#Load and show the greenscreen image
print "Showing Greenscreen image"
greenscreen = Image("/home/administrador-x/Imagens/Wallpapers/logo.png")
greenscreen.show()
time.sleep(sleep_time)


#load and show the background image
print "Showing background image"
background = Image("/home/administrador-x/Imagens/Wallpapers/logo.png")
background.show()
time.sleep(sleep_time)

#Create the mask to apply and show the mask
print "Showing Masked Image"
mask = greenscreen.hueDistance(color=Color.GREEN).binarize()
mask.show()
time.sleep(40)

#Combine the mask and other images to get the final result
print "Showing final image"
result = (greenscreen - mask) + (background - mask.invert())
result.show()
time.sleep(sleep_time)

