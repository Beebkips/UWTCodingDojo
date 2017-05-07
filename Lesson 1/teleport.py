from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 110
z = 12

mc.player.setTilePos(x, y, z)
