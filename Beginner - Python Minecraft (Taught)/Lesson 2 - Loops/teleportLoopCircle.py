from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time, math

x, y, z = mc.player.getPos()

for i in range(0, 30):
    mc.player.setPos(x + 25 * math.cos(i * math.pi * .1), y, z + 25 * math.sin(i * math.pi * .1))
    time.sleep(.25)