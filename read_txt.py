import discord
import subprocess
import ffmpeg
from voice_generator import creat_WAV
import config


if config.IS_DEBUG:
    print("This is debug mode app!")




client = discord.Client()
voice_client = None
vc_channel=615415919920807941
text_channel=615415919920807939 #出力する対象となるチャンネルID ＊ボイチャ推奨（コレがないと、全部のチャンネル読みに行きます）





@client.event
async def on_message(message):
    global voice_client

    if message.content.startswith('$join'):
        vc = client.get_channel(vc_channel)
        # voicechannelに接続
        voice_client = await vc.connect()
        pass
    elif message.content.startswith('$bye'):
        await voice_client.disconnect()

    else:
        if message.guild.voice_client :
           if message.channel.id==text_channel:
                print(message.content)
                creat_WAV(message.content)
                source = discord.FFmpegPCMAudio("output.wav")
                message.guild.voice_client.play(source)
           else:
               pass
        else:
            pass
    if  message.content.startswith('$test'):
        await message.channel.send(message.channel.id)



client.run(config.token_alice)