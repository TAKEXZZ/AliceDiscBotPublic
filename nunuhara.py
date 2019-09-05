# coding: utf-8

import discord
import asyncio
import re
import time
import config
import random
import nunuhara_pedia
import pandas

if config.IS_DEBUG:
    print("This is debug mode app!")

client = discord.Client()
pretime_after = time.time()  # 基準点の時刻を設定


@client.event
async def on_ready():
    print('Bot Name:', client.user.name)
    print('Client ID：', client.user.id)
    print('------')

@client.event
async def on_message(message):
    global pretime_after  # pretime_afterのグローバル定義
    pretime_before = time.time()  # on_messageが呼び出された時点の時刻を取得
    duration_time = int(pretime_before) - int(pretime_after)  # 基準点の時刻と呼び出された時刻の時間差
    ran = random.randint(0, 150)  # 絵画ぶっこみ用乱数
    num = random.randint(0, len(nunuhara_pedia.kaiga))  # 絵画のNOを決めるための乱数
    ran_SSR = random.randint(0, 1000)  # 絵画ぶっこみ用乱数
    num_SSR = random.randint(0, len(nunuhara_pedia.kaiga_SSR))  # 絵画のNOを決めるための乱数


    if duration_time < 30:  # 30秒以内なら何もしない
        if re.search('ヌヌハラさん、定期連絡の', message.content):
            await discord.TextChannel.send(message.channel, 'オッケー！アリスちゃん！まかせて！')
            await asyncio.sleep(3)
            await discord.TextChannel.send(message.channel, 'あなた！ここで見聞きしたことは絶対よそで言っちゃ駄目よ！私たちは共犯者なの、私からのお願い。')
        return

    if client.user == message.author:  # BOTとメッセージの送り主が同じ人なら処理しない
        return

    if message.content.startswith(("こんにち", "こんち", "にちわ", "にちは")):
        if message.author.id != config.id_alice:  # 相手がアリス以外なら以下の処理へ
            day = ["こんにちは！", "こんにちは、あなた！", "こんこん～"]
            await discord.TextChannel.send(message.channel, random.choice(day))
            pretime_after = time.time()  # 基準点を再設定

    if message.content.startswith(("こんばん", "今晩", "バンワ", "ばんわ")):
        if message.author.id != config.id_alice:  # 相手がアリス以外なら以下の処理へ
            night = ["こんばんは！", "こんばんは、あなた！", "こんばんわ～"]
            await discord.TextChannel.send(message.channel, random.choice(night))
            pretime_after = time.time()  # 基準点を再設定

    if message.content.startswith(("おはよ", "お早", "はよ")):
        if message.author.id != config.id_alice:  # 相手がアリス以外なら以下の処理へ
            mor = ["おはようございます！", "お早う、あなた！", "ふぁ～おはよう…え、何をしてたって？ら、ランス様の写真の整理よー！！キャーキャー"]
            await discord.TextChannel.send(message.channel, random.choice(mor))
            pretime_after = time.time()  # 基準点を再設定

    if re.search("おやすみな|お休みな|寝ます", message.content):
        if message.author.id != config.id_alice:  # 相手がアリス以外なら以下の処理へ
            eve = ["はーい、おやすみなさい。いい夢を見てね。", "ゆっくり休んでね。", "くじらさんはどんな夢をみるのかしらね…ふふ、なんでもないわ。おやすみなさい、あなた！"]
            await discord.TextChannel.send(message.channel, random.choice(eve))
            pretime_after = time.time()  # 基準点を再設定

    # 絵文字で「寝て！」というワーグちゃんを返信したかったが、カスタム絵文字はうまくいかなかったのでコメントアウト。また今度やる気になっららがんばる。
    # if message.content.startswith(("眠い", "ねむい")):
    #     if message.author.id != config.id_alice:  # 相手がアリス以外なら以下の処理へ
    #         emoji = client.get_emoji(617750270423728184)
    #         await discord.TextChannel.send(message.channel, emoji)

    if message.content.startswith('そもさん'):
        await discord.TextChannel.send(message.channel, 'せっぱ')

    if message.content.rfind('だよね') > 0:
        dayone = ["わかりみが深い…", "わかる…","そ　れ　！！"]
        await discord.TextChannel.send(message.channel, random.choice(dayone))

    if message.content.rfind('いい…') > 0:
        ii = ['いいよね…','ほんそれ…']
        await discord.TextChannel.send(message.channel, random.choice(ii))

    if re.search("ランス君|ランス様", message.content):
        rance = ['ランス様！？どこどこ！？','ランス様の話をしているの！？私も混ぜてくれないかしら！','はあ…ランス様のギザ歯、かっこいいわよね…']
        await discord.TextChannel.send(message.channel, random.choice(rance))
        pretime_after = time.time()  # 基準点を再設定

    if message.content.startswith('/poll'):
        await discord.TextChannel.send(message.channel, '選ぶなんて無理！死ぬわ！！！')

    if re.search('アラー|あらー', message.content):
        await discord.TextChannel.send(message.channel,
                                       'https://cdn.discordapp.com/attachments/612291698134876160/615173606132940800/img_2_m.jpg')

    if re.search('ヌヌハラさん、定期連絡の',message.content):
        await discord.TextChannel.send(message.channel, 'オッケー！アリスちゃん！まかせて！')
        await asyncio.sleep(3)
        await discord.TextChannel.send(message.channel, 'あなた！ここで見聞きしたことは絶対よそで言っちゃ駄目よ！私たちは共犯者なの、私からのお願い。')

    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} うふふふふふ…！！！！\n' \
                f'え？　あ、な、何って？ランス様の資料に夢中になってて気づかなかったわ。ごめんなさい！' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

    # 　ヌヌハラさんへの呼びかけの場合、応えてあげる（こーのさん、えっちゃんさん対応）
    if message.author.id not in [config.id_nunu, config.id_alice]:
        if ('ヌヌ' in message.content):

            if (('おはよ' in message.content) or ('お早う' in message.content)):
                await discord.TextChannel.send(message.channel, 'おはよう、あなた！')

            if (('こんに' in message.content) or ('こんち' in message.content)):
                await discord.TextChannel.send(message.channel, 'こんにちは、あなた！')

            if (('こんばん' in message.content) or ('ばんわ' in message.content)):
                await discord.TextChannel.send(message.channel, 'こんばんは、あなた！')

            if (('またね' in message.content) or ('おやす' in message.content)):
                await discord.TextChannel.send(message.channel, 'おつかれさま。またこの世界について語り合いましょうね。')

            if (('お疲れ' in message.content) or ('おつかれ' in message.content)):
                await discord.TextChannel.send(message.channel, 'あら、ありがとう。でも私は全く疲れてないわ！')

            if (('疲れた' in message.content) or ('つかれた' in message.content)):
                await discord.TextChannel.send(message.channel, 'どうしたの？疲れた？そんなことではこの世界のことを知ることはできないわ！')

            if ('ありがと' in message.content):
                await discord.TextChannel.send(message.channel, 'どういたしまして～')

# 教えてヌヌハラさんの機能ココカラ
    if  re.search('ヌヌハラ', message.content):
      text_au = message.content
      if re.search('誰', message.content) or re.search('だれ', message.content) or re.search('教えて', message.content) or re.search('おしえて', message.content):
        df = pandas.DataFrame(nunuhara_pedia.rance_chars2,columns=['charname1','charname2','charname3','charname4','fig_url','shp_url'])
        flag = 0
        print(text_au)
        for i in range(len(nunuhara_pedia.rance_chars2)):
            if re.search(df.charname1[i], message.content) or re.search(df.charname2[i], message.content)  or re.search(df.charname3[i], message.content) or re.search(df.charname4[i], message.content):
                flag = 1 #発見フラグ
                await discord.TextChannel.send(message.channel, 'この人かしら？ここで見たことは、私と貴方だけの秘密よ？')
                await discord.TextChannel.send(message.channel, df.fig_url[i])
                await discord.TextChannel.send(message.channel, 'ひつじ小屋別館 -ルドラサウム世界 用語集-')
                await discord.TextChannel.send(message.channel, df.shp_url[i])

                return #「マリア」検索でリアまで出てきてしまうのを防ぐため、リストは上から検索。ヒットしたらループ抜ける必須。

            # だーくんとランス君は別処理。書き換え不要
            if re.search('ダークランス', message.content):
                flag = 1  # 発見フラグ
                figure = 'https://www.alicesoft.com/rance10/chara/independents/img/06.png'
                await discord.TextChannel.send(message.channel, 'この人かしら？ここで見たことは、私と貴方だけの秘密よ？')
                await discord.TextChannel.send(message.channel, figure)
                await discord.TextChannel.send(message.channel, 'ひつじ小屋別館 -ルドラサウム世界 用語集-ダークランス')
                await discord.TextChannel.send(message.channel,
                                               'https://littleprincess.sakura.ne.jp/pukiwiki/index.php?ダークランス')
                return
            elif re.search('ランス', message.content):
                flag = 1
                await discord.TextChannel.send(message.channel, 'え？！なになに？あなたもランス様について知りたいの？！ランス様の事なら私に任せて！')
                await discord.TextChannel.send(message.channel, 'https://www.youtube.com/watch?v=9OCoR_C0AlA')
                await discord.TextChannel.send(message.channel,
                                               '私がランス様と出会ったのは、暖かな日差しに包まれた穏やかな午後だったわ・・・。ハニーは舞い踊り、うし車が街の中を駆けていった・・・・・あらやだ、もうこんな時間。ゴメンナサイ、ホントはもっと詳しく話したかったんだけど、こんな字数じゃ収まらないわ。詳しくはここを見てね')
                await discord.TextChannel.send(message.channel, 'ひつじ小屋別館 -ルドラサウム世界 用語集-ランス')
                await discord.TextChannel.send(message.channel,
                                               'https://littleprincess.sakura.ne.jp/pukiwiki/index.php?ランス')
                return

        if flag == 0:
            await discord.TextChannel.send(message.channel, 'ごめんなさい、その人については編集中なの。')

#　絵チャ呼び出し
      elif re.search('出して', message.content) or re.search('だして', message.content) :

          if re.search('BLお絵', message.content) or re.search('BL絵', message.content):
              await discord.TextChannel.send(message.channel, 'https://draw.kuku.lu/pchat.php?h359bec0')
              await discord.TextChannel.send(message.channel, 'ここは腐っているほうのお絵かきチャットよ？気をつけてね。')

          elif re.search('絵茶', message.content) or re.search('お絵描き', message.content) or re.search('お絵かき', message.content) or re.search('絵チャ', message.content) or re.search('絵ちゃ', message.content):
              await discord.TextChannel.send(message.channel, 'https://draw.kuku.lu/room/?hash=62723885')

#　普通の宝箱
    if ran < 2:
        picture = nunuhara_pedia.kaiga[num]
        place = ['そこの宝箱', 'そこのゴミ箱', 'そこのロッカーの中', 'ランス様の机の中', 'ヘルマンの宝物庫', 'ゼスの博物館', 'ゴルチの家']
        await discord.TextChannel.send(message.channel,
                                       'ねえ！見てちょうだい！さっき、' + random.choice(place) + 'から手に入れたの！「有名な絵画' + str(num) + '」よ！')
        await discord.TextChannel.send(message.channel, picture)
        await discord.TextChannel.send(message.channel,'この絵画のことは私とあなただけの秘密よ？')

# 宝箱SSR
    if ran_SSR < 2:
        picture = nunuhara_pedia.kaiga_SSR[num_SSR]
        place_SSR = ['そこのレア宝箱', 'そこの宝箱だんご', 'はにわ開発室', '幸福きゃんきゃん']
        await discord.TextChannel.send(message.channel,
                                       'ちょっと！！！！！！！？ねえ！！！！！！？見てちょうだい！！！！！！！！！！\n'
                                       'さっき、' + random.choice(place_SSR) + 'から手に入れた「失われし古の絵画' + str(num_SSR) + '」よ！')
        await discord.TextChannel.send(message.channel, picture)
        await discord.TextChannel.send(message.channel,'この絵画のことは私とあなただけの秘密よ？絶対よ？約束！！！')

client.run(config.token_nunu)
