#coding: utf-8

import discord
import config
import googletrans

if config.IS_DEBUG:
    print("This is debug mode app!")

client = discord.Client()

@client.event
async def on_ready():
    print('Bot Name:' , client.user.name)
    print('Client ID：' , client.user.id)
    print('------')

@client.event
async def on_message(message):
    from googletrans import Translator
    translator = Translator()

    if message.content.startswith('-t'):
        pre_txt = message.content
        print(pre_txt)
        lang = pre_txt[3:5]
        txt = pre_txt[5:]
        if lang == 'jp': lang = 'ja'
        trans = translator.translate(txt, dest=lang)
        print(lang)
        print(txt)
        await discord.TextChannel.send(message.channel, trans.text)

client.run(config.token_nunu)
