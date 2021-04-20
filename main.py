import asyncio
import discord
import requests
import secrets
from bs4 import BeautifulSoup
from discord.ext import commands

print("Bot starts")


client = commands.Bot(command_prefix="?", help_command=None, intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    print("Bot is started and ready for use")
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("?help"), status=discord.Status.online)
        await asyncio.sleep(10)
        response = requests.get("https://www.bitcoin.de")
        soup = BeautifulSoup(response.content, 'html.parser')
        btc_price = soup.find(id="ticker_price").text
        await client.change_presence(activity=discord.Game("BTC-Price: " + btc_price), status=discord.Status.online)
        await asyncio.sleep(10)
        response = requests.get("https://www.bitcoin.de/de/etheur/market")
        soup = BeautifulSoup(response.content, 'html.parser')
        ether_price = soup.find(id="ticker_price").text
        await client.change_presence(activity=discord.Game("Ether-Price: " + ether_price), status=discord.Status.online)
        await asyncio.sleep(10)
        response = requests.get("https://www.bitcoin.de/de/ltceur/market")
        soup = BeautifulSoup(response.content, 'html.parser')
        ltc_price = soup.find(id="ticker_price").text
        await client.change_presence(activity=discord.Game("LTC-Price: " + ltc_price), status=discord.Status.online)
        await asyncio.sleep(10)


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help Menu", description="Need some help?")
    embed.add_field(name="?help", value="Shows this menu", inline=False)
    embed.add_field(name="?invite", value="Invite the bot to your server", inline=False)
    embed.add_field(name="?join", value="Join the support server", inline=False)
    embed.add_field(name="?github", value="Shows the link to the github repository of ths open source bot", inline=False)
    embed.add_field(name="?ping", value="Shows the bot latency", inline=False)
    embed.add_field(name="?btc or ?bitcoin", value="Shows some information and the course of Bitcoin", inline=False)
    embed.add_field(name="?bch or ?bitcoincash", value="Shows some information and the course of Bitcoin", inline=False)
    embed.add_field(name="?btg or ?bitcoingolf", value="Shows some information and the course of Bitcoin Gold", inline=False)
    embed.add_field(name="?bsv or ?bitcoinsv", value="Shows some information and the course of Bitcoin SV", inline=False)
    embed.add_field(name="?ltc or ?litcoin", value="Shows some information and the course of Litcoin", inline=False)
    embed.add_field(name="?ether or ?ethereum", value="Shows some information and the course of Ethereum", inline=False)
    embed.add_field(name="?ripple or ?xrp", value="Shows some information and the course of Ripple", inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0} seconds'.format(round(client.latency, 1)))


response = requests.get("https://www.bitcoin.de")
soup = BeautifulSoup(response.content, 'html.parser')
btc_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/etheur/market")
soup = BeautifulSoup(response.content, 'html.parser')
ether_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/bcheur/market")
soup = BeautifulSoup(response.content, 'html.parser')
bch_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/btgeur/market")
soup = BeautifulSoup(response.content, 'html.parser')
btg_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/bsveur/market")
soup = BeautifulSoup(response.content, 'html.parser')
bsv_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/ltceur/market")
soup = BeautifulSoup(response.content, 'html.parser')
ltc_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/xrpeur/market")
soup = BeautifulSoup(response.content, 'html.parser')
xrp_price = soup.find(id="ticker_price").text


@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=827437359036760064&permissions=8&scope=bot")


@client.command()
async def join(ctx):
    await ctx.send("https://discord.com/invite/Q9stTbAHNF")


@client.command()
async def github(ctx):
    await ctx.send("Repository: https://github.com/noddac/Crypto-Helper-Bot \r\n Clone: https://github.com/noddac/Crypto-Helper-Bot.git")


@client.command()
async def btc(ctx):
    embed = discord.Embed(title="Bitcoins")
    embed.add_field(name="Name", value="Bitcoin or BTC", inline=False)
    embed.add_field(name="Founder", value="Satoshi Nakamoto", inline=False)
    embed.add_field(name="Publication", value="2009", inline=False)
    embed.add_field(name="Limit", value="20.999.999,97690000", inline=False)
    embed.add_field(name="Mining", value="SHA-256", inline=False)
    embed.add_field(name="Blockchain", value="340 GB", inline=False)
    embed.add_field(name="Price per Bitcoin", value=btc_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def bitcoin(ctx):
    embed = discord.Embed(title="Bitcoins")
    embed.add_field(name="Name", value="Bitcoin or BTC", inline=False)
    embed.add_field(name="Founder", value="Satoshi Nakamoto", inline=False)
    embed.add_field(name="Publication", value="2009", inline=False)
    embed.add_field(name="Limit", value="20.999.999,97690000", inline=False)
    embed.add_field(name="Mining", value="SHA-256", inline=False)
    embed.add_field(name="Blockchain", value="340 GB", inline=False)
    embed.add_field(name="Price per Bitcoin", value=btc_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def bitcoincash(ctx):
    embed = discord.Embed(title="Bitcoin Cash")
    embed.add_field(name="Name", value="Bitcoin Cash or BCH", inline=False)
    embed.add_field(name="Publication", value="2017", inline=False)
    embed.add_field(name="Based on", value="Bitcoin", inline=False)
    embed.add_field(name="Mining", value="SHA-256", inline=False)
    embed.add_field(name="Blockchain", value="167 GB", inline=False)
    embed.add_field(name="Price per Bitcoin", value=bch_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def bch(ctx):
    embed = discord.Embed(title="Bitcoin Cash")
    embed.add_field(name="Name", value="Bitcoin Cash or BCH", inline=False)
    embed.add_field(name="Publication", value="2017", inline=False)
    embed.add_field(name="Based on", value="Bitcoin", inline=False)
    embed.add_field(name="Mining", value="SHA-256", inline=False)
    embed.add_field(name="Blockchain", value="167 GB", inline=False)
    embed.add_field(name="Price per Bitcoin", value=bch_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def bitcoinsv(ctx):
    embed = discord.Embed(title="Bitcoins SV")
    embed.add_field(name="Name", value="Bitcoin SV or BSV", inline=False)
    embed.add_field(name="Founder", value="Satoshi Nakamoto", inline=False)
    embed.add_field(name="Mining", value="SHA-256", inline=False)
    embed.add_field(name="Blockchain", value="229 GB", inline=False)
    embed.add_field(name="Price per Bitcoin", value=bsv_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def bsv(ctx):
    embed = discord.Embed(title="Bitcoins SV")
    embed.add_field(name="Name", value="Bitcoin SV or BSV", inline=False)
    embed.add_field(name="Founder", value="Satoshi Nakamoto", inline=False)
    embed.add_field(name="Mining", value="SHA-256", inline=False)
    embed.add_field(name="Blockchain", value="229 GB", inline=False)
    embed.add_field(name="Price per Bitcoin", value=bsv_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def bitcoingolf(ctx):
    embed = discord.Embed(title="Bitcoin Gold")
    embed.add_field(name="Name", value="Bitcoin Gold or BTG", inline=False)
    embed.add_field(name="Based on", value="Bitcoin", inline=False)
    embed.add_field(name="Codebase", value="C++ & QT", inline=False)
    embed.add_field(name="Price per Bitcoin", value=btg_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def btg(ctx):
    embed = discord.Embed(title="Bitcoin Gold")
    embed.add_field(name="Name", value="Bitcoin Gold or BTG", inline=False)
    embed.add_field(name="Based on", value="Bitcoin", inline=False)
    embed.add_field(name="Codebase", value="C++ & QT", inline=False)
    embed.add_field(name="Price per Bitcoin", value=btg_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def ltc(ctx):
    embed = discord.Embed(title="Litcoin")
    embed.add_field(name="Name", value="Litcoin or LTC", inline=False)
    embed.add_field(name="Founder", value="Charlie Lee", inline=False)
    embed.add_field(name="Publication", value="2011", inline=False)
    embed.add_field(name="Mining", value="Scrypt", inline=False)
    embed.add_field(name="Blockchain", value="33 GB", inline=False)
    embed.add_field(name="Price per Litcoin", value=ltc_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def litcoin(ctx):
    embed = discord.Embed(title="Litcoin")
    embed.add_field(name="Name", value="Litcoin or LTC", inline=False)
    embed.add_field(name="Founder", value="Charlie Lee", inline=False)
    embed.add_field(name="Publication", value="2011", inline=False)
    embed.add_field(name="Mining", value="Scrypt", inline=False)
    embed.add_field(name="Blockchain", value="33 GB", inline=False)
    embed.add_field(name="Price per Litcoin", value=ltc_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def ether(ctx):
    embed = discord.Embed(title="Ethereum")
    embed.add_field(name="Name", value="Ethereum or Ether", inline=False)
    embed.add_field(name="Founder", value="Vitalik Buterin, Gavin Wood & Jeffrey Wilcke", inline=False)
    embed.add_field(name="Publication", value="30. Juli 2015", inline=False)
    embed.add_field(name="Codebase", value="Solidity", inline=False)
    embed.add_field(name="Mining", value="Ethash", inline=False)
    embed.add_field(name="Blockchain", value="337 GB", inline=False)
    embed.add_field(name="Price per Ethereum", value=ether_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def ethereum(ctx):
    embed = discord.Embed(title="Ethereum")
    embed.add_field(name="Name", value="Ethereum or Ether", inline=False)
    embed.add_field(name="Founder", value="Vitalik Buterin, Gavin Wood & Jeffrey Wilcke", inline=False)
    embed.add_field(name="Publication", value="30. Juli 2015", inline=False)
    embed.add_field(name="Codebase", value="Solidity", inline=False)
    embed.add_field(name="Mining", value="Ethash", inline=False)
    embed.add_field(name="Blockchain", value="337 GB", inline=False)
    embed.add_field(name="Price per Ethereum", value=ether_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def ripple(ctx):
    embed = discord.Embed(title="Ripple")
    embed.add_field(name="Name", value="Ripple or XRP", inline=False)
    embed.add_field(name="Founder", value="Chris Larsen", inline=False)
    embed.add_field(name="Developer", value="Chris Larsen & Brad Garlinghouse", inline=False)
    embed.add_field(name="Codebase", value="C++", inline=False)
    embed.add_field(name="Price per Ripple", value=xrp_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


@client.command()
async def xrp(ctx):
    embed = discord.Embed(title="Ripple")
    embed.add_field(name="Name", value="Ripple or XRP", inline=False)
    embed.add_field(name="Founder", value="Chris Larsen", inline=False)
    embed.add_field(name="Developer", value="Chris Larsen & Brad Garlinghouse", inline=False)
    embed.add_field(name="Codebase", value="C++", inline=False)
    embed.add_field(name="Price per Ripple", value=xrp_price, inline=False)
    embed.set_footer(text="Powered by Noddac#4399")
    await ctx.send(embed=embed)


client.run(secrets.TOKEN)
