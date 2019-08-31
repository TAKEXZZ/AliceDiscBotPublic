#coding: utf-8

import discord
import asyncio
import re
import time
import config
import random
import nunuhara_pedia

if config.IS_DEBUG:
    print("This is debug mode app!")

client = discord.Client()
pretime_after = time.time()#基準点の時刻を設定


@client.event
async def on_ready():
    print('Bot Name:' , client.user.name)
    print('Client ID：' , client.user.id)
    print('------')

@client.event
async def on_message(message):
    global pretime_after #pretime_afterのグローバル定義
    pretime_before = time.time() #on_messageが呼び出された時点の時刻を取得
    duration_time = int(pretime_before)-int(pretime_after) #基準点の時刻と呼び出された時刻の時間差
    ran=random.randint(0, 100)
    num=random.randint(0,len(nunuhara_pedia.kaiga))

    if duration_time < 30: #30秒以内なら何もしない
        if re.search('ヌヌハラさん、定期連絡の', message.content):
            await discord.TextChannel.send(message.channel, 'オッケー！アリスちゃん！まかせて！')
            await asyncio.sleep(3)
            await discord.TextChannel.send(message.channel, 'あなた！ここで見聞きしたことは絶対よそで言っちゃ駄目よ！私たちは共犯者なの、私からのお願い。')

        return

    if client.user == message.author:   # BOTとメッセージの送り主が同じ人なら処理しない
        return

    if message.content.startswith('こんにち'):
        if message.author.id == '615900248090607631':  # 相手がアリスちゃんなら処理しない
            return
        day = ["こんにちは！", "こんにちは、あなた！", "こんこん～"]
        await discord.TextChannel.send(message.channel, random.choice(day))
        pretime_after = time.time() #基準点を再設定

    if message.content.startswith(("こんばん", "今晩", "バンワ", "ばんわ")):
        if message.author.id == '615900248090607631':  # 相手がアリスちゃんなら処理しない
            return
        night = ["こんばんは！", "こんばんは、あなた！", "こんばんわ～"]
        await discord.TextChannel.send(message.channel, random.choice(night))
        pretime_after = time.time() #基準点を再設定

    if message.content.startswith(("おはよ", "お早", "はよ")):
        if message.author.id == '615900248090607631':  # 相手がアリスちゃんなら処理しない
            return
        mor = ["おはようございます！", "お早う、あなた！", "ふぁ～おはよう…え、何をしてたって？ら、ランス様の写真の整理よー！！キャーキャー"]
        await discord.TextChannel.send(message.channel, random.choice(mor))
        pretime_after = time.time()  # 基準点を再設定

    if message.content.startswith('そもさん'):
        await discord.TextChannel.send(message.channel, 'せっぱ')

    if message.content.rfind('だよね') > 0:
        await discord.TextChannel.send(message.channel, 'わかりみが深い…')

    if message.content.rfind('いい…') > 0:
        await discord.TextChannel.send(message.channel, 'いいよね…')

    if re.search("ランス君", message.content):
        await discord.TextChannel.send(message.channel, 'ランス様！？どこどこ！？')
        pretime_after = time.time()  # 基準点を再設定
    if re.search('ランス様', message.content):
        await discord.TextChannel.send(message.channel, 'ランス様！？どこどこ！？')
        pretime_after = time.time()  # 基準点を再設定

    if message.content.startswith('/poll'):
        await discord.TextChannel.send(message.channel, '選ぶなんて無理！死ぬわ！！！')

    if re.search('アラー|あらー', message.content):
        await discord.TextChannel.send(message.channel, 'https://cdn.discordapp.com/attachments/612291698134876160/615173606132940800/img_2_m.jpg')

    if re.search('ヌヌハラさん、お絵かき板を出して', message.content):
        await discord.TextChannel.send(message.channel, 'https://draw.kuku.lu/room/?hash=62723885')

    if re.search('ヌヌハラさん、定期連絡の',message.content):
        await discord.TextChannel.send(message.channel, 'オッケー！アリスちゃん！まかせて！')
        await asyncio.sleep(3)
        await discord.TextChannel.send(message.channel, 'あなた！ここで見聞きしたことは絶対よそで言っちゃ駄目よ！私たちは共犯者なの、私からのお願い。')

    if  re.search('ヌヌハラさん', message.content):
        text_au = message.content
        if re.search('教えて', message.content):
          flag=0
          print(text_au)
          for index in range(len(nunuhara_pedia.rance_chars2)):
              string1=nunuhara_pedia.rance_chars2[index][0]
              string2=nunuhara_pedia.rance_chars2[index][1]
              string3=nunuhara_pedia.rance_chars2[index][2]
              string4=nunuhara_pedia.rance_chars2[index][3]
              print(string1)
              print(string2)
              print(string3)
              if re.search(string1, message.content) or re.search(string2, message.content)  or re.search(string3, message.content):
               flag=1 #発見フラグ
               await discord.TextChannel.send(message.channel, 'この人かしら？ここで見たことは、私と貴方だけの秘密よ？')
               await discord.TextChannel.send(message.channel,string4)
               await discord.TextChannel.send(message.channel, 'ひつじ小屋別館 -ルドラサウム世界 用語集-')
               await discord.TextChannel.send(message.channel, 'https://littleprincess.sakura.ne.jp/pukiwiki/index.php?'+string1)
               #return
          if flag==0:
              await discord.TextChannel.send(message.channel, 'ごめんなさい、その人については編集中なの。')
        elif re.search('出して', message.content):
            if re.search('絵茶', message.content) or re.search('お絵描きチャット', message.content) or re.search('お絵かきチャット', message.content) or re.search('絵チャ', message.content) or re.search('絵ちゃ', message.content):
                await discord.TextChannel.send(message.channel, 'https://draw.kuku.lu/room/?hash=62723885')

    if ran < 2:
        picture=nunuhara_pedia.kaiga[num]
        place=['そこの宝箱','そこのゴミ箱', 'そこのロッカーの中','ランス様の机の中','ヘルマンの宝物庫','ゼスの博物館','ゴルチの家']
        await discord.TextChannel.send(message.channel, 'ねえ！見てちょうだい！さっき、'+random.choice(place)+'から手に入れたの！「有名な絵画'+str(num)+'」よ！')
        await discord.TextChannel.send(message.channel,picture)



client.run(config.token_nunu)
