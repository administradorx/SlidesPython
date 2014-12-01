from SimpleCV import *

cam = Camera()
cont = 0
add=5
disp = Display((640,480))
while disp.isNotDone:
	frame = cam.getImage().scale(800,600).flipHorizontal()
	
	

	
	
	
		# desenhando retangulos #
		#(x,y,largura,altura)
		
		
	frame.drawRectangle(305,25,100,100,Color.GREEN,width=4) #num1 
	frame.drawRectangle(405,25,100,100,Color.GREEN,width=4) #num2  
	frame.drawRectangle(505,25,100,100,Color.GREEN,width=4) #num3
	frame.drawRectangle(305,125,100,100,Color.GREEN,width=4) #num4
	frame.drawRectangle(405,125,100,100,Color.GREEN,width=4) #num5
	frame.drawRectangle(505,125,100,100,Color.GREEN,width=4) #num6
	frame.drawRectangle(305,225,100,100,Color.GREEN,width=4) #num7
	frame.drawRectangle(405,225,100,100,Color.GREEN,width=4) #num8
	frame.drawRectangle(505,225,100,100,Color.GREEN,width=4) #num9
	frame.drawRectangle(305,325,100,100,Color.GREEN,width=4) #num0
	
	#desenhando numeros
	
	frame.drawText('1',305+30,25,color=Color.RED,fontsize=90)#num1
	frame.drawText('2',405+30,25,color=Color.RED,fontsize=90)#num2
	frame.drawText('3',505+30,25,color=Color.RED,fontsize=90)#num3
	frame.drawText('4',305+30,125,color=Color.RED,fontsize=90)#num4
	frame.drawText('5',405+30,125,color=Color.RED,fontsize=90)# num5
	frame.drawText('6',505+30,125,color=Color.RED,fontsize=90)#num7
	frame.drawText('7',305+30,225,color=Color.RED,fontsize=90)#num7
	frame.drawText('8',405+30,225,color=Color.RED,fontsize=90)#num8
	frame.drawText('9',505+30,225,color=Color.RED,fontsize=90)#num9
	frame.drawText('0',305+30,325,color=Color.RED,fontsize=90)#num0
		
	
	
	
	
	
	
	# desenhando retangulos #
	#(x,y,largura,altura)
	
	
	frame.drawRectangle(305,25,100,100,Color.GREEN,width=4) #num1 
	frame.drawRectangle(405,25,100,100,Color.GREEN,width=4) #num2  
	frame.drawRectangle(505,25,100,100,Color.GREEN,width=4) #num3
	frame.drawRectangle(305,125,100,100,Color.GREEN,width=4) #num4
	frame.drawRectangle(405,125,100,100,Color.GREEN,width=4) #num5
	frame.drawRectangle(505,125,100,100,Color.GREEN,width=4) #num6
	frame.drawRectangle(305,225,100,100,Color.GREEN,width=4) #num7
	frame.drawRectangle(405,225,100,100,Color.GREEN,width=4) #num8
	frame.drawRectangle(505,225,100,100,Color.GREEN,width=4) #num9
	frame.drawRectangle(305,325,100,100,Color.GREEN,width=4) #num0
	
	#desenhando numeros
	
	frame.drawText('1',305+30,25,color=Color.RED,fontsize=90)#num1
	frame.drawText('2',405+30,25,color=Color.RED,fontsize=90)#num2
	frame.drawText('3',505+30,25,color=Color.RED,fontsize=90)#num3
	frame.drawText('4',305+30,125,color=Color.RED,fontsize=90)#num4
	frame.drawText('5',405+30,125,color=Color.RED,fontsize=90)# num5
	frame.drawText('6',505+30,125,color=Color.RED,fontsize=90)#num7
	frame.drawText('7',305+30,225,color=Color.RED,fontsize=90)#num7
	frame.drawText('8',405+30,225,color=Color.RED,fontsize=90)#num8
	frame.drawText('9',505+30,225,color=Color.RED,fontsize=90)#num9
	frame.drawText('0',305+30,325,color=Color.RED,fontsize=90)#num0
			
	frame.show()
		
			
