# Connect to api
from mcpi.minecraft import minecraft
mc = Minecraft.create()

# Set the world coordinates as variables
x = 10.0
y = 110.0
z = 12.0

# Set player's position
mc.player.setPos(x, y, z)
