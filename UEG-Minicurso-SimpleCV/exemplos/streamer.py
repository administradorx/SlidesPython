from SimpleCV import *
import webbrowser 
from time import *
import time

cam = Camera() 
saida = JpegStreamer("10.1.1.182:8880",st=0.1) 
time.sleep(1)
webbrowser.open("http:10.1.1.182:8880")

def halfsies(left,right):
    result = left
    # crop the right image to be just the right side.
    crop   = right.crop(right.width/2.0,0,right.width/2.0,right.height)
    # now paste the crop on the left image.
    result = result.blit(crop,(left.width/2,0))
    # return the results.
    return result

while True:
    img = cam.getImage()
    output = img.edges().invert()
    # generate the side by side image.
    result = halfsies(img,output)    
    result.drawText('TESTANDO TRANSMISAO',30,40,color=Color.BLUE,fontsize=60)
    img.applyLayers()
    result.save(saida)
    time.sleep(0.1)
