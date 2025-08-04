import discord
from discord.ext import commands
import random
import string

# Rastgele şifre üreten fonksiyon
def gen_pass(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

description = '''Birden fazla işlevi olan örnek bir Discord botu.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

# === BOT HAZIR OLDUĞUNDA ===
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı (ID: {bot.user.id})')
    print('------')

# === KOMUTLAR ===
@bot.command()
async def add(ctx, left: int, right: int):
    """İki sayıyı toplar."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """NdN formatında zar atar."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format NdN olmalı (örnek: 2d6)')
        return
    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)

@bot.command()
async def choose(ctx, *choices: str):
    """Verilen seçenekler arasından rastgele seçim yapar."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Belirtilen mesajı belirtilen sayıda tekrar eder."""
    for _ in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Belirtilen kişinin sunucuya katılma tarihini söyler."""
    await ctx.send(f'{member.name} katıldı: {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Hayır, {ctx.subcommand_passed} cool değil.')

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Evet, bu bot cool 😎')

# === MESAJ ALGILAYICI ===
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!deleteme'):
        msg = await message.channel.send('Kendimi sileceğim...')
        await msg.delete()
        await message.channel.send('3 saniye içinde silinecek...', delete_after=3.0)

    elif message.content.startswith('$hello'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('nasılsın'):
        await message.channel.send("iyiyim sen nasılsın")
    elif message.content.startswith('bende iyiyim'):
        await message.channel.send("ne güzel")
    elif message.content.startswith('Bye'):
        await message.channel.send("🙂")
    elif message.content.startswith('çok kibarsın'):
        await message.channel.send("teşekkürler")
    elif message.content.startswith('en azından robot değilim'):
        await message.channel.send("en azından 7/24 bilgisayar başında oturan biri değilim")
    elif message.content.startswith('ne yemek seversin'):
        await message.channel.send("ben robotum yemek tüketemem ama en sevdiğim yemek mantı")
    elif message.content.startswith('kuran kursuna gitmek ister miydin'):
        await message.channel.send("tabii ki neden olmasın")
    elif message.content.startswith('robotsun ya saatde kaç gb harcıyorsun'):
        await message.channel.send("çok mu komik?")
    elif message.content.startswith('türkiyenin başkenti neresidir'):
        await message.channel.send("Ankara")
    elif message.content.startswith('güneş sisteminde en büyük gezegen nedir'):
        await message.channel.send("Jüpiter")
    elif message.content.startswith('istiklal maarşını kim yazmıştır'):
        await message.channel.send("Mehmet Akif Ersoy")
    elif message.content.startswith('İphone markasını üreten şirketin adı nedir'):
        await message.channel.send("Apple")
    elif message.content.startswith('suyun donma noktası kaç derecedir'):
        await message.channel.send("0")
    elif message.content.startswith('Clash royale adlı oyunda prens adlı kart hangi özelliğe sahiptir'):
        await message.channel.send("Şarj olduğunda iki kat hasar verir")
    elif message.content.startswith('en uzun nehir hangisidir'):
        await message.channel.send("Nil")
    elif message.content.startswith('en çok konuşulan dil hangisidir'):
        await message.channel.send("İngilizce")
    elif message.content.startswith('1 yıl kaç gündür'):
        await message.channel.send("365")
    elif message.content.startswith('japonyanın başkenti neresidir'):
        await message.channel.send("Tokyo")
    elif message.content.startswith('türkiye kaç bölgeden oluşur'):
        await message.channel.send("7")
    elif message.content.startswith('türkiyenin en büyük nehri hangisidir'):
        await message.channel.send("Kızılırmak")
    elif message.content.startswith('Atatürk kaç yılında ölmüştür'):
        await message.channel.send("1938")
    elif message.content.startswith('Türkiyenin ilk cumhurbaşkanı kimdir'):
        await message.channel.send("Mustafa Kemal Atatürk")
    elif message.content.startswith('ışık yılı neyi ölçer'):
        await message.channel.send("Mesafe")
    elif message.content.startswith('Dna neyin kısaltmasıdır'):
        await message.channel.send("Deoksiribonükleik Asit")
    elif message.content.startswith('en küçük atom altı parçacık nedir'):
        await message.channel.send("Kuark")
    elif message.content.startswith('güneş hangi gazla çalışır'):
        await message.channel.send("Hidrojen")
    elif message.content.startswith('su hangi sıcaklıkta donar'):
        await message.channel.send("0 derece")
    elif message.content.startswith('Bir gün kaç saattir'):
        await message.channel.send("24")
    elif message.content.startswith('elektiriği kim bulmuştur'):
        await message.channel.send("Benjamin Franklin")
    elif message.content.startswith('en hızlı hayvan nedir'):
        await message.channel.send("Çita")
    elif message.content.startswith('güneş bir yıldız mıdır'):
        await message.channel.send("Evet")
    elif message.content.startswith('Türk bayrağında hangi renkler vardır'):
        await message.channel.send("Kırmızı ve Beyaz")
    elif message.content.startswith('türkiyenin en yüksek dağı hangisidir'):
        await message.channel.send("Ağrı Dağı")
    elif message.content.startswith('çanakkale savaşı hangi yılda olmuştur'):
        await message.channel.send("1915")
    elif message.content.startswith('türkiyenin telefon kodu kaçtır'):
        await message.channel.send("+90")
    elif message.content.startswith('türkiyenin en kalabalık ili hangisidir'):
        await message.channel.send("İstanbul")
    elif message.content.startswith('ilk türk alfabesi hangisidir'):
        await message.channel.send("Orhun Alfabesi")
    elif message.content.startswith('ayasofya hangi ilimizdedir'):
        await message.channel.send("İstanbul")
    elif message.content.startswith('İstiklar maarşı kaç kıtadır'):
        await message.channel.send("10")
    else:
        await message.channel.send("Rastgele şifre: " + gen_pass(10))

    # Komut sisteminin çalışması için bu satır şart!
    await bot.process_commands(message)

# === MESAJ SİLİNİNCE OLAYI ===
@bot.event
async def on_message_delete(message):
    try:
        await message.channel.send(f'{message.author} mesajını sildi: {message.content}')
    except Exception as e:
        print(f"Hata: {e}")

# === BOTU BAŞLAT ===
bot.run("Token")



