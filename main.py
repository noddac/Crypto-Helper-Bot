import asyncio
import random
import string
import discord
import requests
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
async def help(ctx):
    embed = discord.Embed(title="Help Menu", description="Need some help?")
    embed.add_field(name="?help", value="Shows this menu", inline=False)
    embed.add_field(name="?info", value="Shows some information about the bot", inline=False)
    embed.add_field(name="?invite", value="Invite the bot to your server", inline=False)
    embed.add_field(name="?join", value="Join the support server", inline=False)
    embed.add_field(name="?ping", value="Display the bot latency", inline=False)
    embed.add_field(name="?btc or ?bitcoin", value="Shows some information and the course of Bitcoin", inline=False)
    embed.add_field(name="?ltc or ?litcoin", value="Shows some information and the course of Litcoin", inline=False)
    embed.add_field(name="?ether or ?ethereum", value="Shows some information and the course of Ethereum", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=827437359036760064&permissions=8&scope=bot")


@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0} seconds'.format(round(client.latency, 1)))


@client.command()
async def btc(ctx):
    embed = discord.Embed(title="Bitcoins")
    embed.add_field(name="Information", value="d", inline=False)
    embed.add_field(name="Price per Bitcoin", value=btc_price, inline=False)
    embed.add_field(name="Price per 0,5 Bitcoin", value=btc_price/2, inline=False)
    embed.add_field(name="Price per 0,1 Bitcoin", value=btc_price/10, inline=False)
    embed.add_field(name="Price per 0,01 Bitcoin", value=btc_price / 100, inline=False)
    await ctx.send(embed=embed)


@client.command()
async def bitcoin(ctx):
    embed = discord.Embed(title="Bitcoins")
    embed.add_field(name="Information", value="d", inline=False)
    embed.add_field(name="Price per Bitcoin", value=btc_price, inline=False)
    embed.add_field(name="Price per 0,5 Bitcoin", value=btc_price/2, inline=False)
    embed.add_field(name="Price per 0,1 Bitcoin", value=btc_price/10, inline=False)
    embed.add_field(name="Price per 0,01 Bitcoin", value=btc_price / 100, inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ltc(ctx):
    embed = discord.Embed(title="Litcoin")
    embed.add_field(name="Information", value="d", inline=False)
    embed.add_field(name="Price per Litcoin", value=ltc_price, inline=False)
    embed.add_field(name="Price per 0,5 Litcoin", value=ltc_price/2, inline=False)
    embed.add_field(name="Price per 0,1 Litcoin", value=ltc_price/10, inline=False)
    embed.add_field(name="Price per 0,01 Litcoin", value=ltc_price/100, inline=False)
    await ctx.send(embed=embed)


@client.command()
async def litcoin(ctx):
    embed = discord.Embed(title="Litcoin")
    embed.add_field(name="Information", value="d", inline=False)
    embed.add_field(name="Price per Litcoin", value=ltc_price, inline=False)
    embed.add_field(name="Price per 0,5 Litcoin", value=ltc_price/2, inline=False)
    embed.add_field(name="Price per 0,1 Litcoin", value=ltc_price/10, inline=False)
    embed.add_field(name="Price per 0,01 Litcoin", value=ltc_price/100, inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ether(ctx):
    embed = discord.Embed(title="Ethereum")
    embed.add_field(name="Information", value="d", inline=False)
    embed.add_field(name="Price per Ethereum", value=ether_price, inline=False)
    embed.add_field(name="Price per 0,5 Ethereum", value=ether_price/2, inline=False)
    embed.add_field(name="Price per 0,1 Ethereum", value=ether_price/10, inline=False)
    embed.add_field(name="Price per 0,01 Ethereum", value=ether_price/100, inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ethereum(ctx):
    embed = discord.Embed(title="Ethereum")
    embed.add_field(name="Information", value="d", inline=False)
    embed.add_field(name="Price per Ethereum", value=ether_price, inline=False)
    embed.add_field(name="Price per 0,5 Ethereum", value=ether_price/2, inline=False)
    embed.add_field(name="Price per 0,1 Ethereum", value=ether_price/10, inline=False)
    embed.add_field(name="Price per 0,01 Ethereum", value=ether_price/100, inline=False)
    await ctx.send(embed=embed)


client.run("ODI3NDM3MzU5MDM2NzYwMDY0.YGbBFw.9i7PjeRwYUSNIZdI4gPuTH9BfEE")
