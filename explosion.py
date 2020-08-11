from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        big_magic = mc.createExplosion(x,y,z)