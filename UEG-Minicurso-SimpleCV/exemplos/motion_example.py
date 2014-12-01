from SimpleCV import *
scaler = 0.5
cam = Camera(0)
disp = Display((320,240))
last = cam.getImage().scale(scaler)
sz = last.width/10
while disp.isNotDone():
    img = cam.getImage().scale(scaler)
    motion = img.findMotion(last,sz,method='HS')
    motion.draw(color=Color.RED,width=1)
    
    
    img.save(disp)
    last = img
