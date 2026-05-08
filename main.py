import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# سيرفر ويب بسيط لإبقاء البوت حياً
app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# إعدادات البوت
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! I am working 24/7')

if __name__ == "__main__":
    keep_alive()
    # استبدل الكلمة التالية بالتوكن الجديد الخاص بك
    bot.run('MTUwMTUwNTUzNjk4NDYxMjkyNQ.GpvUBz.N4Bd397iJn9AL3CQgXgMek09OVsd4V2Tw1TrA8')
  
