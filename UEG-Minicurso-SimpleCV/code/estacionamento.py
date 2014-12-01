from SimpleCV import *


carroestacionado = Image("imagens/parking-car.png")

fullimage = carroestacionado.hueDistance(Color.YELLOW)
full = carroestacionado - fullimage

carro = carroestacionado.crop(470,200,230,200) #x,y h,w



carro_amarelo = carro.hueDistance(Color.YELLOW)
estacionado = img - carro_amarelo
estacionado.show()