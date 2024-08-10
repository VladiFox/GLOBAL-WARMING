import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        with open(f'images/гп1.jpg', 'rb') as f:
            picture = discord.File(f) 
        await message.channel.send("Привет. Знаешь ли ты о проблемах, которые окружают твой мир? Я создан для осведомления пользователей об одной огромной проблеме - глобальное потепление.")
    if message.content.startswith('$global_warming'):
        await message.channel.send('Глобальное потепление — распространенное название изменения климата, которое идет уже около двух веков. С 1800-х годов по большой части фактором вызова глобального потепление является человеческая деятельность. Например сжигание ископаемых видов топлива, в результате образуются газы, удерживающие тепло в атмосфере.')
    if message.content.startswith('$solution'):
        with open(f'images/гп4.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send("В качестве решений я предлагаю вам такие варианты: 1) отказаться от личной машины, больше пользоваться общественным транспортом или же велосипедом. 2) Экономьте энергию. Отключайте электроприборы, которыми не пользуетесь. Как можно больше заменяйте электроприборы, например вместо электронной сушилки можно высушить на обычной или на балконе. 3) Утилизация отходов приводит к сокращению энергопотребления, но еще лучше было бы повторно использовать продукцию или сокращать масштабы потребления. 4) Как можно больше освещайте эту проблему с окружением, рекламируйте меня и подобные проекты. Призывайте общество к действиям указанным выше.")
    if message.content.startswith('$ocean'):
        await message.channel.send("Океан является крупнейшим поглотителем углерода на планете. Его загрязнение пластиком влияет на глобальное потепление. Пластик по мере разложения высвобождает метан, что вносит существенный вклад в глобальное потепление")
    if message.content.startswith('$temperature'):
        with open(f'images/гп5.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send("Средняя глобальная температура Земли около 15 градусов Цельсия. Это невероятно плохие результаты.")
    if message.content.startswith('animals'):
        with open(f'images/гп2.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send("Глобальное потепление приводит к тому, что миграция животных начинается раньше, чем обычно, поэтому детеныши не успевают окрепнуть и гибнут, пытаясь преодолеть препятствия, например, реки. Отставшие от стада животные становятся жертвами браконьеров и бродячих собак")
    if message.content.startswith('gracier'):
        with open(f'images/гп3.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send("Таяние ледников приведет к дисбалансу мирового климата, в результате планета все чаще будет сталкиваться с сильными дождями, штормами, ураганами и засухой. На Земле существование многих видов животных и растений напрямую зависит от ледников.")
    if message.content.startswith('petition'):
        petition = await message.channel.send(input('Вы можете предотварить нарастание глобального потепления! Подпишите петицию. Введите свой электронный адрес, куда в дальнейшем поступит вся информация.'))
    if message.content.startswith(petition):
        await message.channel.send("Спасибо! Скоро придет ссылка на нашу петицию. Нам нужна ваша подпись.")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTI3MTgxODg2MzU5OTk0MzY4MQ.GlqdXd.Rbgt4dk1rTK19Ady9BG5x26HBW57LgecZZytIo")