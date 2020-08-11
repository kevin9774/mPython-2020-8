import time 
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    time.sleep(3)
    color = random.randrange(0,16)
    mc.setBlocks( x+2 , y-1 , z+2 , x-2 , y-1 , z-2 , 35,color )