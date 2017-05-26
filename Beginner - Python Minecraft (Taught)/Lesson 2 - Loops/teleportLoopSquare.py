from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getPos()

for i in range(10, 110, 10):
    mc.player.setPos(x + i, y, z)
    time.sleep(1)

x, y, z = mc.player.getPos()

for i in range(10, 110, 10):
    mc.player.setPos(x, y, z + i)
    time.sleep(1)

x, y, z= mc.player.getPos()

for i in range(10, 110, 10):
    mc.player.setPos(x - i, y, z)
    time.sleep(1)

x, y, z = mc.player.getPos()

for i in range(10, 110, 10):
    mc.player.setPos(x, y, z - i)
    time.sleep(1)