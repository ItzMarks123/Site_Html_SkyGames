import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
  print("bot sky games iniciou!")
  
  @bot.event
  async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1352250588569800714)
    await canal.send(f"{membro.mention} NOVO MEMBRO NO SERVIDOR ")
  
bot.run("MTM1NjM2NDgzMzI3NjMwMTQ4Mw.G4P4LZ.wJ7vZFNcq6dUJ2ymwterZCHQrfn4znW2ZTgDjs")
