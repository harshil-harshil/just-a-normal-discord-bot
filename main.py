import discord
from discord.ext import commands
import json
import os


from discord.ext import  commands

TOKEN  = 'OTQxNjgyODg4OTc2NTMxNDc2.YgZgiA.3Lwfe3gWCsPZP-B0jLAO_X5kXv4'

client = commands.Bot(command_prefix="cs")
client2 = discord.Client()

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def hello(ctx):  
  await ctx.send("Hi " + ctx.author.name + " !, I am a bot! :) ")
@client.command()
async def burger(ctx):
    await ctx.send("https://i.gifer.com/UtFj.gif")
    


# async def money_balance(ctx):
#     await open_account(ctx.author)
#     users = await get_bank_data()
#     em = discord.Embed(title=f"{ctx.author.name}'s balance", colour=discord.Colour.green())
#     wallet_amt =  users[str(user.id)]["wallet"]
#     em.add_field(name="wallet", value=wallet_amt)
#
#     await ctx.send(embed=em)

@client.command()
async def bal(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    em = discord.Embed(title=f"{ctx.author.name}'s balance",
                       color=discord.Color.orange())
    em.add_field(name="Wallet balance", value=wallet_amt)
    await ctx.send(embed=em)

async def open_account(user):
    with open("economy.json", "r") as f:
        users = json.load(f)

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]["wallet"] = 0

    json.dump(users, f)

    return True


async def get_bank_data():
    with open("economy.json", "r") as f:
        users = json.load(f)
        return users

# async def open_account(user):
#
#     users = await  get_bank_data()
#     if str(user.id) in users:
#         return False
#     else:
#         users[str(user.id)]["wallet"] = 5000
#     with open("economy.json","w") as f:
#         json.dump(users , f)
#         users = json.load(f)
#     return True

async def get_bank_data():
    with open("economy.json", "r") as f:
        users = json.load(f)
        return users
    return True



@client.command()
async def functions(ctx):
  embedVar = discord.Embed(title=f"Bot Commands",
                                 description="\n 1)**csHello_Bot** - Say hello to our bot! \n 2)csmoney_balance** - Shows how much money you have, YAY! \n 3)**csmenu** - Shows items available in the menu, YAY AND YUMMY!",
                                 color=0x00ff00)
  await ctx.send(embed=embedVar)
  

@client.command()
async def menu(ctx):
  embedVar = discord.Embed(title=f"DuoBot restraunt menu",
                                 description=" \n 1)**cspizza** -  order pizza  \n 2)**csburger** - order burger \n 3)**csfrench_fries **- order french fries \n 4)**cschicken_pizza** - order chicken pizza \n 5)**cschoclate_ice_cream** - order choclate ice cream \n 6)**csvanilla_ice_cream** - order vanilla ice cream \n 7)****csbutterscotch_ice_cream** - order butterscotch ice cream \n 8)**cscheese_pizza** - order cheese pizza \n Thats all in the menu lol",
                                 color=0x00ff00)
  await ctx.send(embed=embedVar)

@client.command()
async def pizza(ctx):
    await ctx.send("https://media3.giphy.com/media/4ayiIWaq2VULC/giphy.gi")

@client.command()
async def french_fries(ctx):
    await ctx.send("https://media1.giphy.com/media/622RBpIlB0HxTiUD8u/giphy.gif")

@client.command()
async def chicken_pizza(ctx):
    await ctx.send("https://i.makeagif.com/media/2-15-2016/YUJ3aj.gif")

@client.command()
async def chocolate_ice_cream(ctx):
    await ctx.send("https://c.tenor.com/a2x2Rh0GvlwAAAAM/serving-chocolate-icecream.gif")

@client.command()
async def vanilla_ice_cream(ctx):
    await ctx.send("https://media3.giphy.com/media/11uLNcfvw0knkI/giphy.gif")

@client.command()
async def butterscotch_ice_cream(ctx):
    await ctx.send("https://5.imimg.com/data5/TX/PO/MY-31939142/butterscotch-ice-cream-500x500.jpg")

@client.command()
async def cheese_pizza(ctx):
    await ctx.send("https://c.tenor.com/7jvfDIiI9BkAAAAd/dominos-pizza-pizza.gif")


client.run(TOKEN)