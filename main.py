import discord
import time

from discord.ext import commands
from csv_reader import reader 
from logger import log, clear

class MyClient(discord.Client):
    print('Бот запускается...')
    async def on_ready(self):
        print('Бот готов к работе!')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel is None or (before.channel != after.channel and after.channel != None):
            data = reader() # Загрузка нашего csv-файла
            print(f"{member} зашел в канал {after.channel} в {time.strftime('%H')}:{time.strftime('%M')}.") # Информация о входе (переходе) на голосовой сервер
##            clear() # Очистка файла
            log(data, str(member.name)+'#'+str(member.discriminator), str(after.channel.name), int(time.strftime('%w')), int(time.strftime('%H')), int(time.strftime('%M'))) # Проверка на наличие в списках и добавление, если есть

client = MyClient()
token = open('token.txt', 'r').readline()
client.run(token)
