import time 
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
length = 20
width = 10
height = 5
x,y,z =mc.player.getTilePos()

x2 = x+length
y2 = y+height
z2 = z+width
while True:
    time.sleep(3)
    color = random.randrange(0,16)
    mc.setBlocks(x,y,z,x2,y2,z2,35,color)
    mc.setBlocks(x+1,y+1,z+1,x2-1,y2-1,z2-1,0)