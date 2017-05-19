from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getPos()

mc.postToChat('You are at position: ' + str(x) + ' ' + str(y) + ' ' + str(z))