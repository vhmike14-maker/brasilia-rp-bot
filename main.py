import discord
import os
import re

CANAL_CLIPES_ID = 1572554946681896991
TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado com sucesso como {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == CANAL_CLIPES_ID:
        urls = re.findall(r'(https?://[^\s]+)', message.content)

        if urls:
            link_clipe = urls[0]
            texto_extra = message.content.replace(link_clipe, '').strip()

            embed = discord.Embed(
                title="🎬 Novo Clipe - Brasília RP",
                description=f"**Enviado por:** {message.author.mention}\n" + (f"**Descrição:** {texto_extra}\n" if texto_extra else "") + f"\n🔗 [Assistir ao Clipe]({link_clipe})",
                color=discord.Color.green()
            )
            embed.set_footer(text="Sistema Automático de Clipes • Brasília RP")
            if message.author.avatar:
                embed.set_thumbnail(url=message.author.avatar.url)

            try:
                await message.delete()
            except discord.Forbidden:
                pass

            await message.channel.send(content=link_clipe, embed=embed)

client.run(TOKEN)
