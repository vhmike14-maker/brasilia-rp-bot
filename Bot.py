import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ID do canal de clipes configurado
CANAL_CLIPES_ID = 1572554946681896991

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == CANAL_CLIPES_ID:
        if "http://" in message.content or "https://" in message.content:
            link_enviado = message.content.strip()

            embed = discord.Embed(
                title="BRASÍLIA RP",
                color=0x202225
            )
            
            embed.add_field(name="▶ ASSISTIR CLIPE", value=f"[Clique aqui para assistir]({link_enviado})", inline=False)
            embed.add_field(name="JOGADOR", value=message.author.display_name, inline=True)
            embed.add_field(name="SERVIDOR", value="Brasília RP", inline=True)
            
            embed.set_footer(text="CENTRAL DE CLIPES • BRASÍLIA RP")

            await message.channel.send(embed=embed)

            try:
                await message.delete()
            except discord.Forbidden:
                print("O bot não tem permissão para deletar mensagens.")

    await bot.process_commands(message)

# Token do bot configurado
bot.run("MTU3MjU2MDYwODI5MTg0ODE5NA.G9WpS8.erXpkY
