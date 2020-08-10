from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("我正在看著你X:"+str(x)+"y:"+str(y)+"z:"+str(z))
    time.sleep(0.5)