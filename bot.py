import discord
import re

# Configurações do Bot - Brasília RP
CANAL_CLIPES_ID = 1572554946681896991
TOKEN = "MTU3MjU2MDYwODI5MTg0ODE5NA.G9WpS8.erXpkYJ6MD7nqq3Y2il7Jgb36qwXG0_ktkrG28"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado com sucesso como {client.user}!')

@client.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == client.user:
        return

    # Verifica se a mensagem foi enviada no canal de clipes
    if message.channel.id == CANAL_CLIPES_ID:
        # Procura por links (http:// ou https://) na mensagem
        urls = re.findall(r'(https?://[^\s]+)', message.content)
        
        if urls:
            link_clipe = urls[0]
            texto_extra = message.content.replace(link_clipe, '').strip()

            # Cria o cartão formatado (Embed)
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

            await message.channel.send(content=
