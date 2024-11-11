import asyncio
import random
import re
import os
import logging
import base64
import json

from datetime import datetime, timezone, timedelta
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
print('Loading env variables.')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
print('Env vars loaded correctly.')

# EXPECTED EVENT TEXTS
forest_text = re.compile("In a dire need for an adventure, you went to a forest. You'll be back in 3 minutes")
# forest_text = re.compile("You went to the Mirkwood. Beware of spooders. Back in 3 minutes")

swamp_text = re.compile("An adventure is calling. But you went to a swamp. You'll be back in 4 minutes.")
# swamp_text = re.compile("You went to the Dead Marshes. The dead are near. Back in 4 minutes")

valley_text = re.compile(
    "Mountains can be a dangerous place. You decided to investigate, what's going on. You'll be back in 4 minutes.")
# valley_text = re.compile("You went to the Devil's Valley. Don't lose your soul. Back in 4 minutes")

night_forest_text = re.compile("In a dire need for an adventure, you went to a forest. You'll be back in 5 minutes")
# night_forest_text = re.compile("You went to the Mirkwood. Beware of spooders. Back in 5 minutes")

night_swamp_text = re.compile("An adventure is calling. But you went to a swamp. You'll be back in 6 minutes.")
# night_swamp_text = re.compile("You went to the Dead Marshes. The dead are near. Back in 6 minutes")

night_valley_text = re.compile(
    "Mountains can be a dangerous place. You decided to investigate, what's going on. You'll be back in 6 minutes.")
# night_valley_text = re.compile("You went to the Devil's Valley. Don't lose your soul. Back in 6 minutes")

foray_text = re.compile('You were strolling around on your horse when you noticed')
mob_text = re.compile('You met some hostile creatures. Be careful:')
# pledge_received_text = re.compile('To accept their offer, you shall')
mtf = re.compile("You've met a serious mtf")
full_storage = re.compile("your warehouse is full and you lost your loot")
foray_clueless = re.compile(" was completely clueless. Village was successfully pillaged")
foray_tried = ("tried stopping you, but you were stronger")
foray_noticed = re.compile("noticed you and nearly beat you to death. You crawled back home to a nice warm bath.")

quest_text = re.compile('Here you fight against other players')
no_stamina = re.compile('Not enough stamina. Come back after you take a rest.')
near_war = re.compile('Battle is coming. You have no time for games.')
full_stamina = re.compile('Stamina restored. You are ready for more adventures!')
busy_adventure = re.compile('You are too busy with a different adventure. Try a bit later.')
no_hp_for_quest = re.compile('You should heal up a bit first.')
arena_complete = re.compile('Leaderboard of fighters are updated:')
arena_done = re.compile('You need to heal your wounds and recover, come back later.')
arena_night = re.compile('It’s hard to see your opponent in the dark. Wait until the morning.')
no_money = re.compile('Not enough gold to pay the entrance fee.')

# CHANNELS
ChatWars_Channel = '@chtwrsbot'
Master = '@Lady_Destroy3r'
AshMaster = '@TereAsh'

# DEV MSG
control_words = re.compile('control words')
forward_msg = re.compile('forward msgs')
dev_send_me = re.compile('send me')
dev_send_quest = re.compile('send quest')
dev_status = re.compile('status')
dev_quest = re.compile('quest on')
dev_bot_off = re.compile('set bot off')
dev_bot_on = re.compile('set bot on')
arena_on = re.compile('arena')
ammount = re.compile("scrolls ammount")
tactics_text = re.compile("You joined the defensive formations. The next battle is in")
order = ''
detord = ''
preparing = re.compile("You are preparing for a fight")

# FLAGS
bot_flag = 0
questtype = 1
forward_to_dev = 1

lbot_flag = 0
lquesttype = 1
lforward_to_dev = 1

marbot_flag = 0
marquesttype = 1
marforward_to_dev = 1

tolbot_flag = 0
tolquesttype = 1
tolforward_to_dev = 1

milebot_flag = 0
milequesttype = 0
mileforward_to_dev = 1

sanbot_flag = 0
sanquesttype = 1
sanforward_to_dev = 1

# withdrawer

# on/off
work = 1
turn_on = re.compile('/turn on')
turn_off = re.compile('/turn off')
reset = re.compile('/restart')

# ids
canal = -1001749192981
cw = '@chtwrsbot'

# textos
wd = re.compile('/g_withdraw')
bad_format = re.compile('Usage: /g_withdraw [{item code, from /g_stock} {quantity}] (up to 9 pairs)')
not_enough = re.compile('Not enough items on guild stock')
wd_busy = re.compile('You are too busy with a different adventure. Try a bit later.')
wd_invalid = re.compile('invalid action')
wd_ok = re.compile('Recipient shall send to bot')

# semaforos
mutex = 0

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
greter = os.getenv('GRETER')
greter_alt = os.getenv('GRETER_ALT')

print('Trying to connect to Telegram')

client = TelegramClient(StringSession(greter), api_id=api_id, api_hash=api_hash)
liclient = TelegramClient(StringSession(greter_alt), api_id=api_id, api_hash=api_hash)

# greter

@client.on(events.NewMessage(chats=ChatWars_Channel, incoming=True))
async def cw_handler(event):
    if bot_flag == 0:

        searchforflame = event.message.message
        localizadorflame = searchforflame.find("🔥")
        if localizadorflame != -1:
            if searchforflame[localizadorflame - 7] == "t":  # searching for the 7th character before the flame
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(0)
            elif searchforflame[localizadorflame - 7] == "p":  # searching for the 7th character before the flame
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(1)
            elif searchforflame[localizadorflame - 7] == "y":  # searching for the 7th character before the flame
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(2)

        else:

            if re.search(quest_text, event.raw_text):
                #                    await client.send_message(Alessio, 'quest text')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(questtype)

            elif re.search(forest_text, event.raw_text):
                #                    await client.send_message(Alessio, 'forest text')
                sleep_time = random.randint(255, 260)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(swamp_text, event.raw_text):
                #                    await client.send_message(Alessio, 'forest text')
                sleep_time = random.randint(315, 320)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(valley_text, event.raw_text):
                #                    await client.send_message(Alessio, 'forest text')
                sleep_time = random.randint(315, 320)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(night_forest_text, event.raw_text):
                #                    await client.send_message(Alessio, 'night foress text')
                sleep_time = random.randint(375, 380)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(night_swamp_text, event.raw_text):
                #                    await client.send_message(Alessio, 'night foress text')
                sleep_time = random.randint(435, 440)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(night_valley_text, event.raw_text):
                #                    await client.send_message(Alessio, 'night foress text')
                sleep_time = random.randint(435, 440)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(near_war, event.raw_text):
                #                    await client.send_message(Alessio, 'near war u fuck')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🛡Defend')
                wind_blowing = random.randint(1500, 1560)
                await asyncio.sleep(wind_blowing)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(no_stamina, event.raw_text):
                #                    await client.send_message(Alessio, 'no stamina text')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🛡Defend')

            elif re.search(busy_adventure, event.raw_text):
                sleep_time = random.randint(435, 440)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(no_hp_for_quest, event.raw_text):
                sleep_time = random.randint(600, 660)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(full_stamina, event.raw_text):
                #                    await client.send_message(Alessio, 'full stamina text')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(foray_text, event.raw_text):
                # await client.send_message('me', 'lo cogi')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await event.click(0)

            elif re.search(arena_complete, event.raw_text):
                #                 await client.send_message('me', 'arena completada')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '▶️Fast fight')

            elif re.search(arena_done, event.raw_text):
                #                 await client.send_message('me', 'se acabaron las arenas por hoy')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🛡Defend')

            elif re.search(arena_night, event.raw_text):
                #                 await client.send_message('me', 'No hay arenas de noche')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🛡Defend')

            elif re.search(no_money, event.raw_text):
                #                 await client.send_message('me', 'No money')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🏅Me')
                await asyncio.sleep(sleep_time)
                await client.send_message(ChatWars_Channel, '🛡Defend')

            # elif re.search(mob_text, event.raw_text):
            #     await client.forward_messages('me', event.message)
            #     sleep_time = random.randint(70, 85)
            #     await asyncio.sleep(sleep_time)

            # elif re.search(full_storage, event.raw_text):
            #     await meclient.send_message('me', 'papa full stock')
            #     sleep_time = random.randint(10, 30)
            #     await asyncio.sleep(sleep_time)

            else:
                if forward_to_dev == 0:
                    await client.forward_messages('me', event.message)

    else:
        if forward_to_dev == 0:
            if re.search(quest_text, event.raw_text):
                await client.send_message('me', 'bot is currently off')
            else:
                await client.forward_messages('me', event.message)


@client.on(events.NewMessage(chats='me', incoming=True))
async def dev_handler(event):
    global bot_flag
    global questtype
    global forward_to_dev

    if re.search(dev_bot_off, event.raw_text):
        bot_flag = 1
        await client.send_message('me', 'bot is now off')
        print("The bot flag is: " + str(bot_flag))

    elif re.search(dev_bot_on, event.raw_text):
        bot_flag = 0
        await client.send_message('me', 'bot is now on')
        print("The bot flag is: " + str(bot_flag))

    elif re.search(forward_msg, event.raw_text):
        forward_to_dev = 0
        await client.send_message('me', 'bot is now forwarding msgs')
        print("The bot flag is: " + str(forward_to_dev))

    elif re.search(dev_status, event.raw_text):
        await client.send_message('me', "The bot flag is: " + str(bot_flag))
        await client.send_message('me', "The forward flag is: " + str(forward_to_dev))
        await client.send_message('me', "Currently questing on : " + str(questtype))
    #        print ("The bot flag is: " + str(bot_flag))
    #        print ("The forward flag is: " + str(forward_to_dev))
    #        print ("Currently questing on : " + str(questtype))

    elif re.search(dev_send_quest, event.raw_text):
        bot_flag = 0
        await client.send_message(ChatWars_Channel, '🗺Quests')

    elif re.search(dev_send_me, event.raw_text):
        await client.send_message(ChatWars_Channel, '🏅Me')

    elif re.search(arena_on, event.raw_text):
        await client.send_message(ChatWars_Channel, '▶️Fast fight')

    elif re.search(dev_quest, event.raw_text):
        questmsg = event.message.message
        localizadorquest = questmsg.find("n") + 2

        if questmsg[localizadorquest] == "f":
            questtype = 0
            await client.send_message('me', 'questeando en Forest')

        elif questmsg[localizadorquest] == "s":
            questtype = 1
            await client.send_message('me', 'questeando en Swamp')

        elif questmsg[localizadorquest] == "v":
            questtype = 2
            await client.send_message('me', 'questeando en Valley')


# greter alt

@liclient.on(events.NewMessage(chats=ChatWars_Channel, incoming=True))
async def cw_handler(event):
    if lbot_flag == 0:

        searchforflame = event.message.message
        localizadorflame = searchforflame.find("🔥")
        if localizadorflame != -1:
            if searchforflame[localizadorflame - 7] == "t":  # searching for the 7th character before the flame
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(0)
            elif searchforflame[localizadorflame - 7] == "p":  # searching for the 7th character before the flame
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(1)
            elif searchforflame[localizadorflame - 7] == "y":  # searching for the 7th character before the flame
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(2)

        else:

            if re.search(quest_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'quest text')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await event.click(lquesttype)

            elif re.search(forest_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'forest text')
                sleep_time = random.randint(255, 260)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(swamp_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'forest text')
                sleep_time = random.randint(315, 320)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(valley_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'forest text')
                sleep_time = random.randint(315, 320)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(night_forest_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'night foress text')
                sleep_time = random.randint(375, 380)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(night_swamp_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'night foress text')
                sleep_time = random.randint(435, 440)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(night_valley_text, event.raw_text):
                #                    await liclient.send_message(Alessio, 'night foress text')
                sleep_time = random.randint(435, 440)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(near_war, event.raw_text):
                #                    await liclient.send_message(Alessio, 'near war u fuck')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🛡Defend')
                wind_blowing = random.randint(1500, 1560)
                await asyncio.sleep(wind_blowing)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(no_stamina, event.raw_text):
                #                    await liclient.send_message(Alessio, 'no stamina text')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🛡Defend')

            elif re.search(busy_adventure, event.raw_text):
                sleep_time = random.randint(435, 440)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(no_hp_for_quest, event.raw_text):
                sleep_time = random.randint(600, 660)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(full_stamina, event.raw_text):
                #                    await liclient.send_message(Alessio, 'full stamina text')
                sleep_time = random.randint(5, 10)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🗺Quests')

            elif re.search(foray_text, event.raw_text):
                # await liclient.send_message(Master, 'lo cogi')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await event.click(0)

            elif re.search(arena_complete, event.raw_text):
                #                 await liclient.send_message(Master, 'arena completada')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '▶️Fast fight')

            elif re.search(arena_done, event.raw_text):
                #                 await liclient.send_message(Master, 'se acabaron las arenas por hoy')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🛡Defend')

            elif re.search(arena_night, event.raw_text):
                #                 await liclient.send_message(Master, 'No hay arenas de noche')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🛡Defend')

            elif re.search(no_money, event.raw_text):
                #                 await liclient.send_message(Master, 'No money')
                sleep_time = random.randint(10, 35)
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🏅Me')
                await asyncio.sleep(sleep_time)
                await liclient.send_message(ChatWars_Channel, '🛡Defend')

            # elif re.search(mob_text, event.raw_text):
            #     # await liclient.forward_messages(Master, event.message)
            #     sleep_time = random.randint(70, 85)
            #     await asyncio.sleep(sleep_time)

            else:
                if lforward_to_dev == 0:
                    await liclient.forward_messages(Master, event.message)

    else:
        if lforward_to_dev == 0:
            if re.search(quest_text, event.raw_text):
                await liclient.send_message(Master, 'bot is currently off')
            else:
                await liclient.forward_messages(Master, event.message)


@liclient.on(events.NewMessage(chats=Master, incoming=True))
async def dev_handler(event):
    global lbot_flag
    global lquesttype
    global lforward_to_dev

    if re.search(dev_bot_off, event.raw_text):
        lbot_flag = 1
        # await liclient.send_message(Master, 'bot is now off')
        print("The bot flag is: " + str(lbot_flag))

    elif re.search(dev_bot_on, event.raw_text):
        lbot_flag = 0
        # await liclient.send_message(Master, 'bot is now on')
        print("The bot flag is: " + str(lbot_flag))

    elif re.search(forward_msg, event.raw_text):
        lforward_to_dev = 0
        # await liclient.send_message(Master, 'bot is now forwarding msgs')
        print("The bot flag is: " + str(lforward_to_dev))

    # elif re.search(dev_status, event.raw_text):
    #     await liclient.send_message(Master, "The bot flag is: " + str(lbot_flag))
    #     await liclient.send_message(Master, "The forward flag is: " + str(lforward_to_dev))
    #     await liclient.send_message(Master, "Currently questing on : " + str(lquesttype))
    #        print ("The bot flag is: " + str(lbot_flag))
    #        print ("The forward flag is: " + str(lforward_to_dev))
    #        print ("Currently questing on : " + str(lquesttype))

    elif re.search(dev_send_quest, event.raw_text):
        lbot_flag = 0
        await liclient.send_message(ChatWars_Channel, '🗺Quests')

    elif re.search(dev_send_me, event.raw_text):
        await liclient.send_message(ChatWars_Channel, '🏅Me')

    elif re.search(arena_on, event.raw_text):
        await liclient.send_message(ChatWars_Channel, '▶️Fast fight')

    elif re.search(dev_quest, event.raw_text):
        questmsg = event.message.message
        localizadorquest = questmsg.find("n") + 2

        if questmsg[localizadorquest] == "f":
            lquesttype = 0
            await liclient.send_message(Master, 'questeando en Forest')

        elif questmsg[localizadorquest] == "s":
            lquesttype = 1
            await liclient.send_message(Master, 'questeando en Swamp')

        elif questmsg[localizadorquest] == "v":
            lquesttype = 2
            await liclient.send_message(Master, 'questeando en Valley')


client.start()
liclient.start()
client.run_until_disconnected()
