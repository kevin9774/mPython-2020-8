
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
length = 20
width = 10
height = 5
x,y,z =mc.player.getTilePos()

x2 = x+length
y2 = y+height
z2 = z+width
mc.setBlocks(x,y,z,x2,y2,z2,0)
mc.setBlocks(x+1,y+1,z+1,x2-1,y2-1,z2-1,0)