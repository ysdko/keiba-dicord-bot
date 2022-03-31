# インストールした discord.py を読み込む
import discord
import scrape

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTU1MzM0MzEzMjc5Mzg5Njk3.YjgKaQ.uFxopJ3TMEYb_gmdzgs9ix7bkOQ'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        scrape.func(True)
        # await message.channel.send('にゃーん')
    if message.content == '/stop':
        exit(1)
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)