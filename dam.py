from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
a = 0
while a<10  :
    mc.setBlocks(x,y-1,z+10,x,y-5,z-10,19)
    x = x-5
    a = a+1
    