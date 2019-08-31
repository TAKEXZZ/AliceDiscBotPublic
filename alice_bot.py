# coding: utf-8

import discord
import asyncio
from discord.ext import tasks
from datetime import datetime
import re
import time
import json
import os
import random
from time import sleep
import threading
import config

if config.IS_DEBUG:
    print("This is debug mode app!")

client = discord.Client()
choice = ''
# CHANNEL_ID = [
#     611480149287895072   # 本番_総合
#     ,612094843975368734  # 本番_ランスシリーズ
#     ,612095157827010580  # 本番 １８禁
#     ,612291698134876160  # 本番_ボイスチャット用
#
#     ,615146529010745354 #キャベツ畑_テスト用
#     ,616619849996828674 #キャベツ畑_テスト用２
#
#     #以下、各自の裏庭
#     ,615711031578198029
#     ,616453506404057096
#     ,616609948675211264
#
# ]  # アナウンスするためのチャンネルIDを記述
#
# ★検証したところ、CHANNEL_IDは5つ以上だとバグになるので、
#   時報を修正するときは上記部屋番号を起こして使ってください　★

CHANNEL_ID = [
        611480149287895072   # 本番_総合
        ,612094843975368734  # 本番_ランスシリーズ
        ,612095157827010580  # 本番 １８禁
        ,612291698134876160  # 本番_ボイスチャット用
]  # アナウンスするためのチャンネルIDを記述
msg_id =['ほげ'] * len(CHANNEL_ID)

@client.event
async def on_ready():
    print('Bot Name:', client.user.name)
    print('Client ID：', client.user.id)
    print('------')
    time_check.start()

@tasks.loop(seconds=60)
async def time_check():
    timeStr = datetime.now().strftime('%H:%M')  # 時間を取得
    timeStr_minute = datetime.now().strftime('%M')  # 分を抜き出す
    timeStr_hour = int(datetime.now().strftime('%H'))  # 時間をint型に変更

    if timeStr_minute == '00':  # XX:00分の時
        if timeStr_hour == 6:  # 6時のとき
            for index in range(len(CHANNEL_ID)):
                # if  msg_id[index] != client.user.name: # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                    await asyncio.sleep(2)
                    await result_channel.send('おはようございます。今日のご予定はなんですか？')

        elif timeStr_hour == 12:  # 12時のとき
            for index in range(len(CHANNEL_ID)):
                # if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                    await result_channel.send('お昼になりました。これからお昼ごはんですか？美味しいものをいっぱい食べて、ごごからも元気いっぱいがんばってくださいね。')

        elif timeStr_hour == 13:  # 13時のとき
            for index in range(len(CHANNEL_ID)):
                # if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    lunch = ["カツサンド", "オムライス", "ひつまぶし", "ぶぶづけ", "タコライス", "味千ラーメン", "トルコライス", "釜玉うどん", "トムヤムクン", "お好み焼き",
                             "盛岡冷麺"]
                    await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                    await asyncio.sleep(2)
                    await result_channel.send('今日のお昼ごはんは何でしたか？私は諭吉と' + random.choice(lunch) + 'をたべました。')
                    await asyncio.sleep(2)
                    await result_channel.send('さあ、ヌヌハラさん、定期連絡のお仕事ですよ？')

        elif timeStr_hour == 18:  # 18時のとき
            for index in range(len(CHANNEL_ID)):
                # if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                    dinner = ["ジンギスカン", "へんでろぱ", "モツ鍋", "きりたんぽ鍋", "長崎ちゃんぽん", "芋煮"]
                    await result_channel.send(
                        'こんばんは。今日も一日お疲れさまでした。今夜の晩ごはんはなんですか？私は闇アリスちゃんと' + random.choice(dinner) + 'を食べに行くの。楽しみ。')
                    await asyncio.sleep(2)
                    await result_channel.send('さあ、ヌヌハラさん、定期連絡のお仕事ですよ？')

        elif timeStr_hour == 0:  # 0時～4時までのとき
            for index in range(len(CHANNEL_ID)):
                if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                    await result_channel.send('今日も一日お疲れさまでした。ゆっくり休んで、また明日元気なお姿みせてくださいね。明日はきっと良いことあるかも。')

        elif timeStr_hour == 2:  # 0時～4時までのとき
            for index in range(len(CHANNEL_ID)):
                if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ふぁぁぁ・・・。ただいまの・・・時刻は・・・' + timeStr + '丁度です・・すぴー。')
                    await result_channel.send('まだ起きてたんですか・・？・・・夜ふかしは身体に毒ですよぉ・・。')

        else:
         return

@client.event
async def on_message(message):
    global voice, player,msg_id
    timeStr = datetime.now().strftime('%H:%M')  # 時間を取得
    timeStr_hour = int(datetime.now().strftime('%H'))  # 時間をint型に変更

    # for index in range (len(CHANNEL_ID)):#デバッグ用
    #     result_channel = client.get_channel(CHANNEL_ID[index])
    #     msg_id[index]=result_channel.last_message.author.name
    #     print (result_channel.last_message.author.name )
    #
    # if re.search('/だれ', message.content):
    #   await discord.TextChannel.send(message.channel, '最後の発言者は' + msg_id[0]+msg_id[1]+msg_id[2]+msg_id[3] + 'です。')

    if re.search('今日の予言', message.content):
        global choice  # こうするとエラーがでなくなった・・・
        de = ["徹夜で仕事", "洗礼　ｂｙ　うめずかずお", "逆噴射", "馬", "秋葉原", "島唄", "お好み焼き屋で妊婦さん"]
        syou = ["クジラ喰いたい", "アルプスの少女おんじ（あれ？）", "だいぶっこん", "大吉", "わからん", "金がない", "うさぎ", "たこやき"]
        choice = '今日は・・・' + random.choice(de) + 'で' + random.choice(syou) + 'でしょう。'  # 上記のランダム分を結合
        await discord.TextChannel.send(message.channel, choice)
        await asyncio.sleep(1)
        await discord.TextChannel.send(message.channel, '・・・多分')

    if re.search('いま何時？', message.content):
        if 5 < timeStr_hour < 24:
            await discord.TextChannel.send(message.channel, 'はーい！只今の時刻は' + timeStr + 'です。')
        else:
            await discord.TextChannel.send(message.channel, 'ふぁぁぁ・・・。只今の・・時刻は' + timeStr + 'ですぅぅー・・すぴー・・・。')

client.run(config.token_alice)
