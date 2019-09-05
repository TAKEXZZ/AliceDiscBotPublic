#coding: utf-8

import discord
import asyncio
import re
import config
import random
import nunuhara_pedia
import subprocess
import ffmpeg
from voice_generator import creat_WAV
import pandas


voice_flag = False  #特殊音声フラグ
voice_flag2= False #読み上げ使用時判断フラグ

if config.IS_DEBUG:
    print("This is debug mode app!")



client = discord.Client()


vc_channel	 = config.vc_channel
text_channel = config.text_channel

#出力する対象となるチャンネルID ＊ボイチャ推奨（コレがないと、全部のチャンネル読みに行きます）

voice_client = None

@client.event
async def on_ready():
    print('Bot Name:' , client.user.name)
    print('Client ID：' , client.user.id)
    print('------')


@client.event
async def on_message(message):

    global voice_client ,voice_flag,voice_flag2,trans_flag

    text = message.content

    #本番botと違って、読み上げ接続時と読み上げ切断時によって、サイコロ処理と時報処理変えてます。

    if voice_flag2 == False and voice_flag == False:#フラグ条件（読み上げ切断時、特殊音声中以外の時）
       if message.content.startswith('/join'):
        voice_flag2 = True #読み上げ接続フラグ　オン
        vc = client.get_channel(vc_channel)
        # voicechannelに接続
        voice_client = await vc.connect()
        pass
    elif voice_flag2 == True and voice_flag == False:#フラグ条件（読み上げ接続中、特殊音声中以外の時）
       if message.content.startswith('/bye'):
        await voice_client.disconnect() #読み上げ接続フラグ　オフ
        voice_flag2 = False
       else:
        if message.guild.voice_client :

           if message.channel.id==text_channel:
              if  message.content.startswith('/ring') and voice_flag == False:#フラグ条件（特殊音声中以外の時）
                    voice_flag=True#特殊音声フラグ　オン
                    source = discord.FFmpegPCMAudio("ring.mp3")
                    message.guild.voice_client.play(source)
                    await asyncio.sleep(15)
                    voice_flag = False#特殊音声フラグ　オフ
                    return
              elif  message.content.startswith('ぴんぽんぱんぽーん！ただいまの時刻は') and voice_flag == False:#フラグ条件（特殊音声中以外の時）
                    voice_flag=True#特殊音声フラグ　オン
                    source = discord.FFmpegPCMAudio("ring.mp3")
                    message.guild.voice_client.play(source)
                    await asyncio.sleep(15)
                    voice_flag = False#特殊音声フラグ　オフ
                    return

              elif message.content.startswith('/sai') and voice_flag == False:#フラグ条件（特殊音声中以外の時）
                  voice_flag=True #特殊音声フラグ　オン
                  await discord.TextChannel.send(message.channel, 'サイコロスタート！')
                  await discord.TextChannel.send(message.channel,
                                                 'https://cdn.discordapp.com/attachments/615102255334686722/617600058820395008/AW385985_17.gif')
                  source = discord.FFmpegPCMAudio("sai.mp3")
                  message.guild.voice_client.play(source)
                  await asyncio.sleep(7)
                  talk_t = nunuhara_pedia.TALK_T
                  await discord.TextChannel.send(message.channel, random.choice(talk_t))
                  voice_flag=False #特殊音声フラグ　オフ

                  return

              else:#入力文字を音声に変える処理開始
               if voice_flag == False :
                print(message.content)
                text = re.sub(r'[!-~]', '', text)       #ここで半角文字を消す処理を入れる
                text = text[:100] #100文字制限
                creat_WAV(text)
                source = discord.FFmpegPCMAudio("output.wav")
                message.guild.voice_client.play(source)
           else:
               pass
        else:
            pass
#    if message.content == '!ring':
#        voice_client = message.guild.voice_client
#        if voice_client is None:
#            vc = client.get_channel(vc_channel)
#            voice_client = await vc.connect()
#        voice_client.play(discord.FFmpegPCMAudio('ring.mp3'))
#        await asyncio.sleep(20)
#        await voice_client.disconnect()


# --------------------------読み上げ切断時の時報処理
    if message.content.startswith("ぴんぽんぱんぽーん！ただいまの時刻は") and voice_flag2== False and voice_flag == False:#フラグ条件（読み上げ切断時、特殊音声中以外の時）
        voice_flag=True#特殊音声フラグ　オン
        vc = client.get_channel(vc_channel)
         # voicechannelに接続
        voice_client = await vc.connect()
        source = discord.FFmpegPCMAudio("ring.mp3")
        message.guild.voice_client.play(source)
        await asyncio.sleep(15)
        await voice_client.disconnect()
        voice_flag=False#特殊音声フラグ　オフ

#--------------------------読み上げ切断時のサイコロ処理
    if message.content == '/sai' and voice_flag2== False and voice_flag==False:#フラグ条件（読み上げ切断時、特殊音声中以外の時）
        voice_flag=True#特殊音声フラグ　オン
        vc = client.get_channel(vc_channel)
         # voicechannelに接続
        voice_client = await vc.connect()
        await discord.TextChannel.send(message.channel, 'サイコロスタート！')
        await discord.TextChannel.send(message.channel, 'https://cdn.discordapp.com/attachments/615102255334686722/617600058820395008/AW385985_17.gif')
        source = discord.FFmpegPCMAudio("sai.mp3")
        message.guild.voice_client.play(source)
        await asyncio.sleep(7)
        talk_t = nunuhara_pedia.TALK_T
        await discord.TextChannel.send(message.channel, random.choice(talk_t))
        await voice_client.disconnect()
        voice_flag=False #特殊音声フラグ　オフ


#-----------------------簡易スタンプ機能部分
    if message.content == '/挑発' or message.content =='/1':
        await discord.TextChannel.send(message.channel, 'https://cdn.discordapp.com/attachments/615415919920807939/617713983645810689/unknown.png')
    if message.content == '/衝撃' or message.content =='/2':
        await discord.TextChannel.send(message.channel, 'https://cdn.discordapp.com/attachments/615415919920807939/617716885865234609/unknown.png')
    if message.content == '/美味' or message.content =='/3':
        await discord.TextChannel.send(message.channel, 'https://cdn.discordapp.com/attachments/615415919920807939/617717132351897608/unknown.png')
    if message.content == '/グッドだ' or message.content == '/4':
        await discord.TextChannel.send(message.channel,
                                       'https://cdn.discordapp.com/attachments/615415919920807939/617716523288494080/unknown.png')
    if message.content == '/殺意' or message.content == '/5':
        await discord.TextChannel.send(message.channel,
                                           'https://cdn.discordapp.com/attachments/615415919920807939/617717550746304512/unknown.png')

#------------------------簡易画像表示機能部分
    if message.content.startswith("$") or message.content.startswith("＄"):
        df = pandas.DataFrame(nunuhara_pedia.rance_chars2,columns=['charname1','charname2','charname3','charname4','fig_url','shp_url'])
        flag = 0
        text_au = message.content
        print(text_au)
        for i in range(len(nunuhara_pedia.rance_chars2)):
            if re.search(df.charname1[i], message.content) or re.search(df.charname2[i], message.content)  or re.search(df.charname3[i], message.content) or re.search(df.charname4[i], message.content):
                flag = 1 #発見フラグ
                await discord.TextChannel.send(message.channel, df.charname1[i] + df.fig_url[i])

            elif re.search('ランス', message.content):
                flag = 1
                await discord.TextChannel.send(message.channel, 'https://www.youtube.com/watch?v=9OCoR_C0AlA')
                return
        if flag == 0:
            await discord.TextChannel.send(message.channel, 'ごめんなさい、お探しの方は発見できませんでした。')
#---------------------------------------------


client.run(config.token_voice)