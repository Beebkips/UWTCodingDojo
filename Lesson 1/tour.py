# Connect to api
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Set the world coordinates as variables
x = # Fill in
y = # Fill in
z = # Fill in

# Teleport the player
mc.player.setTilePos(x, y, z)

# Wait for 10 seconds
time.sleep(10)

# Set the world coordinates as variables
x = # Fill in
y = # Fill in
z = # Fill in

# Teleport the player
mc.player.setTilePos(x, y, z)
