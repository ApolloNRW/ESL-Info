import discord
import random
import asyncio
import os
import sys
import logging

#from pyfiglet import figlet_format, FontNotFound

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")

else:
    import config


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=config.logfile, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = discord.Client()
DEIN_USERNAME = "192794157842956290"

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    await client.change_presence(game=discord.Game(name="")),


@client.event
async def on_message(message):
   if message.content.lower().startswith('?test'):
       embed = discord.Embed(
           title="ESL",
           color=0x2ecc71,
           description="**BOT ACTIVE!**"
       )
       embed.set_footer(
           text="by Apollo",
           icon_url="https://eslgfx.net/gfx/logos/playerphotos/7992000/7992037_big.jpg"
       )
       await client.send_message(message.channel, embed=embed)


   if message.content.lower().startswith('?version'):
       version = str(discord.__version__)
       await client.send_message(message.channel, "Die aktuelle Discord Version ist: " + version)


   if message.content.lower().startswith('!commands'):
       userembed = discord.Embed(title="BOT-COMMANDS", color=0x009bdb, description=" Please note that all bot replies will be sent as DMs")
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Help", value="!help", inline = True)
       userembed.add_field(name="Support", value="!support", inline = True)
       userembed.add_field(name="Admin", value="!admin", inline = True)
       userembed.add_field(name="Premium", value="!premium", inline = True)
       userembed.add_field(name="Playercard", value="!playercard", inline = True)
       userembed.add_field(name="Trusted", value="!trusted", inline = True)
       userembed.add_field(name="Apply", value="!apply", inline = True)
       userembed.set_footer(text="by Apollo", icon_url="https://eslgfx.net/gfx/logos/playerphotos/7992000/7992037_big.jpg")

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!help'):
       userembed = discord.Embed(title="Help",
                             description="Please note that admins might not always be available. If no admins are currently available please create a support ticket. If you're experiencing any issues with a match you'll be able to open a protest ticket here.",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Support Ticket", value="https://play.eslgaming.com/global/support", inline = False)
       userembed.add_field(name="Protest Ticket", value="https://play.eslgaming.com/protest/add", inline = True)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!support'):
       userembed = discord.Embed(title="Support",
                             description="Please note that admins might not always be available. If no admins are currently available please create a support ticket. If you're experiencing any issues with a match you'll be able to open a protest ticket here.",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Support Ticket", value="https://play.eslgaming.com/global/support", inline = False)
       userembed.add_field(name="Protest Ticket", value="https://play.eslgaming.com/protest/add", inline = True)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!admin'):
       userembed = discord.Embed(title="Admin",
                             description="Please note that admins might not always be available. If no admins are currently available please create a support ticket. If you're experiencing any issues with a match you'll be able to open a protest ticket here.",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Support Ticket", value="https://play.eslgaming.com/global/support", inline = False)
       userembed.add_field(name="Protest Ticket", value="https://play.eslgaming.com/protest/add", inline = True)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!premium'):
       userembed = discord.Embed(title="ESL Premium",
                             description="Would you like to support ESL, ESL Play's development and participate in our Premium Only tournaments? Check out ESL Premium!",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="ESL Premium", value="[Buy ESL Premium | ESL Play](https://play.eslgaming.com/order/)", inline = False)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!playercard'):
       userembed = discord.Embed(title="Playercard",
                             description="The ESL Playercard stands for mutual trust, security and fairness in the online gaming world. Our verification system gives each player in the ESL a unique identity. Check it out!",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Playercard", value="[Playercard Portal | ESL Play](https://play.eslgaming.com/playercard_portal/)", inline = False)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!trusted'):
       userembed = discord.Embed(title="Trusted",
                             description="The ESL Playercard stands for mutual trust, security and fairness in the online gaming world. Our verification system gives each player in the ESL a unique identity. Check it out!",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Playercard", value="[Playercard Portal | ESL Play](https://play.eslgaming.com/playercard_portal/)", inline = False)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('!apply'):
       userembed = discord.Embed(title="Join our Staff!",
                             description="Are you interested in joining our staff? We'd be happy to have you! More information can be found here:",
                             color=0x009bdb)
       userembed.set_author(
           name="ESL", icon_url = "https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.set_thumbnail(
           url="https://cdn-eslgaming.akamaized.net/play/drupal/profiles/eslgaming_play/themes/eslgaming/eslgaming_play_base/dist/images/esl_2014_horizontal_light.png")
       userembed.add_field(name="Apply", value="[Join the ESL staff | ESL Play](https://play.eslgaming.com/join-the-staff/)", inline = False)

       await client.send_message(message.author, embed=userembed)


   if message.content.lower().startswith('?coin'):  # Coinflip 50/50% chance kopf oder zahl
     choice = random.randint(1, 2)
     if choice == 1:
       await client.add_reaction(message, 'ðŸŒ‘')
     if choice == 2:
       await client.add_reaction(message, 'ðŸŒ•'),


   if message.content.startswith('?gameonline') and message.author.id == DEIN_USERNAME:
       game = message.content[13:]
       await client.change_presence(game=discord.Game(name=game), status=discord.Status.online)
       await client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geaendert")

   if message.content.startswith('?gameoffline') and message.author.id == DEIN_USERNAME:
       game = message.content[13:]
       await client.change_presence(game=discord.Game(name=game), status=discord.Status.offline),
       await client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geaendert")

   if message.content.startswith('?gameidle') and message.author.id == DEIN_USERNAME:
       game = message.content[13:]
       await client.change_presence(game=discord.Game(name=game), status=discord.Status.idle),
       await client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geaendert")

   if message.content.startswith('?gamednd') and message.author.id == DEIN_USERNAME:
       game = message.content[13:]
       await client.change_presence(game=discord.Game(name=game), status=discord.Status.dnd),
       await client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geaendert")

   if message.content.startswith('?gameinvisible') and message.author.id == DEIN_USERNAME:
       game = message.content[13:]
       await client.change_presence(game=discord.Game(name=game), status=discord.Status.invisible),
       await client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geaendert")


   if message.content.startswith('?uptime'):
      for role in message.author.roles:
         if role.name == "Admin":
          await client.send_message(message.channel,"```I am online since {0} hour/s und {1} minutes on {2}. ```".format(hour, minutes,message.server))


async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
    #client.loop.create_task(tutorial_uptime())

client.loop.create_task(tutorial_uptime())


client.run(open("token","r").read())
