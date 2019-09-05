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
import yogen

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

CHANNEL_ID = config.CHANNEL_ID

msg_id = ['ほげ'] * len(CHANNEL_ID)


@client.event
async def on_ready():
    print('Bot Name:', client.user.name)
    print('Client ID：', client.user.id)
    print('------')
    time_check.start()

@client.event
async def on_member_join(member):  # サーバーに参加したときに発動
    print(member)  # デバッグ用
    result_channel = client.get_channel(config.CHANNEL_ID[0])  # メッセージを送りたいチャンネル設定
    await result_channel.send('ようこそ' + str(member.mention) + 'さん。\n'
                              'ここは、アリスソフト作品を愛するファンの交流の場です。\n'
                              'この鯖を利用するにあたって、まずは「諸注意」部屋をご確認ください。\n'
                              '特に、下記内容についてはルール遵守でお願いいたします。\n'
                              '【転載禁止について】\n'
                              'Discord上にあがった、参加者の発言、ログ、画像、音声、その他を本人に無断でどこかに転載する行為は厳禁です。\n'
                              'イラスト、写真、文書などの著作権は本人に帰属します。\n'
                              '【この鯖について】\n'
                              'この鯖はファンの皆さんの熱い交流の場を創りたいと有志で運営しています。\n'
                              'ルールを守って使っていただけない場合は、跡形もなく消滅いたします。\n'
                              '以上、長いお話となりましたが、これらを守った上で、楽しく参加してくださいね。')
    await result_channel.send('「自己紹介」のお部屋に、あなたがどんな作品が好きか書いてもらったら、嬉しいです。')


@tasks.loop(seconds=60)
async def time_check():
    dt = datetime.now()
    timeStr = datetime.now().strftime('%H:%M')  # 時間を取得
    timeStr_minute = datetime.now().strftime('%M')  # 分を抜き出す
    timeStr_hour = int(datetime.now().strftime('%H'))  # 時間をint型に変更

    if timeStr_minute == '00':  # XX:00分の時
        if timeStr_hour == 6:  # 6時のとき
            for index in range(len(CHANNEL_ID)):
                # if  msg_id[index] != client.user.name: # 直前の発言者が自分じゃないとき以下を実行
                result_channel = client.get_channel(CHANNEL_ID[index])
                await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。',delete_after=180)
                await asyncio.sleep(2)
                await result_channel.send('皆さん、おはようございます。今日のご予定はなんですか？',delete_after=180)

        elif timeStr_hour == 12:  # 12時のとき
            for index in range(len(CHANNEL_ID)):
                # if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                result_channel = client.get_channel(CHANNEL_ID[index])
                await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。',delete_after=180)
                await result_channel.send('お昼になりました。これからお昼ごはんですか？美味しいものをいっぱい食べて、ごごからも元気いっぱいがんばってくださいね。',delete_after=180)

        elif timeStr_hour == 13:  # 13時のとき
            for index in range(len(CHANNEL_ID)):
                # if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                result_channel = client.get_channel(CHANNEL_ID[index])
                lunch = ["カツサンド", "オムライス", "ひつまぶし", "ぶぶづけ", "タコライス", "味千ラーメン", "トルコライス", "釜玉うどん", "トムヤムクン", "お好み焼き",
                         "盛岡冷麺"]
                await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                await asyncio.sleep(2)
                random.seed(int(dt.strftime('%Y%m%d')) + int(timeStr_hour))
                await result_channel.send('今日のお昼ごはんは何でしたか？私は諭吉と' + random.choice(lunch) + 'をたべました。')
                await asyncio.sleep(2)
                await result_channel.send('さあ、ヌヌハラさん、定期連絡のお仕事ですよ？')

        elif timeStr_hour == 18:  # 18時のとき
            for index in range(len(CHANNEL_ID)):
                # if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                result_channel = client.get_channel(CHANNEL_ID[index])
                await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。')
                dinner = ["ジンギスカン", "へんでろぱ", "モツ鍋", "きりたんぽ鍋", "長崎ちゃんぽん", "芋煮"]
                random.seed(int(dt.strftime('%Y%m%d')) + int(timeStr_hour))
                await result_channel.send(
                    '今日も一日お疲れさまでした。今夜の晩ごはんはなんですか？私は闇アリスちゃんと' + random.choice(dinner) + 'を食べに行くの。とっても楽しみ。')
                await asyncio.sleep(5)
                await result_channel.send('さあ、ヌヌハラさん、定期連絡のお仕事ですよ？')

        elif timeStr_hour == 0:  # 0時～4時までのとき
            for index in range(len(CHANNEL_ID)):
                if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ぴんぽんぱんぽーん！ただいまの時刻は' + timeStr + '丁度です。',delete_after=180)
                    await result_channel.send('今日も一日お疲れさまでした。ゆっくり休んで、また明日元気なお姿みせてくださいね。明日はきっと良いことあるかも。',delete_after=180)

        elif timeStr_hour == 2:  # 0時～4時までのとき
            for index in range(len(CHANNEL_ID)):
                if msg_id[index] != client.user.name:  # 直前の発言者が自分じゃないとき以下を実行
                    result_channel = client.get_channel(CHANNEL_ID[index])
                    await result_channel.send('ふぁぁぁ・・・。ただいまの・・・時刻は・・・' + timeStr + '丁度です・・すぴー。',delete_after=180)
                    await result_channel.send('まだ起きてたんですか・・？・・・夜ふかしは身体に毒ですよぉ・・。',delete_after=180)

        else:
            return


@client.event
async def on_message(message):
    global voice, player, msg_id
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
        dt = datetime.now()
        random.seed(int(dt.strftime('%Y%m%d')) + int(message.author.id))
        choice = '今日は・・・' + random.choice(yogen.de) + 'で' + random.choice(yogen.syou) + 'でしょう。'  # 上記のランダム分を結合
        await asyncio.sleep(2)
        await discord.TextChannel.send(message.channel, choice)
        await asyncio.sleep(1)
        await discord.TextChannel.send(message.channel, '・・・多分')

    if re.search('いま何時？|今何時？', message.content):
        if 5 < timeStr_hour < 24:
            await discord.TextChannel.send(message.channel, 'はーい！只今の時刻は' + timeStr + 'です。')
        else:
            await discord.TextChannel.send(message.channel, 'ふぁぁぁ・・・。只今の・・時刻は' + timeStr + 'ですぅぅー・・すぴー・・・。')


    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} なあに？ 今お仕事中なのー。ね、諭吉っ' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

#　アリスちゃんへの呼びかけの場合、応えてあげる（こーのさん、えっちゃんさん対応）
    if message.author.id not in [config.id_nunu, config.id_alice]:
        if ('アリスちゃん' in message.content):

            if (('おはよ' in message.content) or ('お早う' in message.content)):
                await discord.TextChannel.send(message.channel, 'はーい！おはようございます！')

            if (('こんに' in message.content) or ('こんち' in message.content)):
                await discord.TextChannel.send(message.channel, 'はい、こんにちは！ゆっくりしていってね！')

            if (('こんばん' in message.content) or ('ばんわ' in message.content)):
                await discord.TextChannel.send(message.channel, 'はーい、こんばんは！')

            if (('またね' in message.content) or ('おやす' in message.content)):
                await discord.TextChannel.send(message.channel, 'は～い、またいらしてくださいね！')

            if (('お疲れ' in message.content) or ('おつかれ' in message.content)):
                await discord.TextChannel.send(message.channel, 'はい、ありがとうございます！でも私、全然疲れてませんよ？\n'
                                                                '諭吉「カァーッカァーッ」')

            if (('疲れた' in message.content) or ('つかれた' in message.content)):
                await discord.TextChannel.send(message.channel, 'あらあらどうしたの？おつかれさまですねぇ。\n'
                                                                '諭吉「カァカァ」')

            if ('ありがと' in message.content):
                await discord.TextChannel.send(message.channel, 'どういたしまして～')

client.run(config.token_alice)
