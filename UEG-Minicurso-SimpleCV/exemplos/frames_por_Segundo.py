from SimpleCV import *
from time import strftime

cam = Camera(threaded=True)
tempo=0
cont=0
f=0

while True:
    time = strftime('%S') 
    cont+=1
    if time  > 1:
        tempo=time
        f=cont
        cont=0
    img = cam.getImage()
    img.drawText(str(f)+' Frames P/s',10,10,color=Color.RED,fontsize=43)
    img.show()
