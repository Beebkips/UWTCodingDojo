from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getPos()

for i in range(0, 100, 10):
    mc.player.setPos(x + i, y - 1, z)
    time.sleep(1)