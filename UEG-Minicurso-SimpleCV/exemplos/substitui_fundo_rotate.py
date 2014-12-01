from SimpleCV import Camera, Image,Color
import time

'''exemplo que carrega uma imagem totalmente vermelha e substiui o fundo do rotate
que e sempre preto por vermelho'''

cam = Camera(1)
img = cam.getImage()
vermelho = Image('/home/administrador-x/vermelho.png').resize(img.width,img.height)
rotate = img.rotate(-65)


mask = rotate.hueDistance(color=Color.BLACK,minsaturation=1,minvalue=1).erode(3).binarize(254)


img2 = mask+vermelho.invert()
img3 = img2.invert()+rotate

img3.show()
time.sleep(5)
