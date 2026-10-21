import discord
from discord.ext import commands
from keep_alive import keep_alive  # <-- TAMBAHAN BARU

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

VOICE_CHANNEL_ID = 1445337473252196421  # Ganti ID Voice Channel lu
TOKEN = 'MTUzNTkyMTU3MzYzNzI2NzQ2Ng.GCAkym.talhu26PvQW8oc9H5E1v00irjEHikzZ6oFGPGc'    # Ganti Token lu

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f'Bot siap: {bot.user}')
    
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel:
        try:
            await channel.connect()
            print(f'Berhasil nangkring di channel: {channel.name}')
        except Exception as e:
            print(f'Gagal join voice: {e}')
    else:
        print('Voice channel ga ketemu.')

# Nyalain web server bohongannya
keep_alive()  # <-- TAMBAHAN BARU
# Jalanin botnya
bot.run(TOKEN)