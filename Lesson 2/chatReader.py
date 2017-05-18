from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while 1:
    chatEvent = mc.events.pollChatPosts()
    print(chatEvent)
    time.sleep(0.5)