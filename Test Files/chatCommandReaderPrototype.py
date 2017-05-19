from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# command = ""

while 1:
    chatEvent = mc.events.pollChatPosts()
    # print(type(chatEvent))
    if len(chatEvent) > 0:
        print(chatEvent)
        command = chatEvent[0].message
        if command.startswith('!teleport'):
            command = command.split('!teleport')[1].strip()
            command = command.split(' ')
            x, y, z = command[0], command[1], command[2]
            mc.player.setPos(x, y, z)
            mc.postToChat('Teleporting to: ' + str(x) + ' ' + str(y) + ' ' + str(z))
    time.sleep(0.5)