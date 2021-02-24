import discord
from discord.ext import commands
client=commands.Bot(command_prefix="&&",case_insensitive=True)
@client.event #لمعرفة اذا كان البوت يعمل 
async def on_ready():
    print(f"the bot id run {client.user}")

@client.command() #لعمل ping
async def ping(ctx):
    await ctx.send("pong !")
@client.command()
async def id(ctx):
    user=ctx.author
    await ctx.send(user.id)
'''@client.event #لحذف الرسائل 
async def on_message(message):
	await message.delete()'''
@client.event
async def on_message_delete(message):
	idchanel= 813807748818141184
	chanel=client.get_channel(idchanel)
	user=message.author
	channel=message.channel
	await chanel.send(f"user --> {user.mention} \n delet message --> {message.content} \n in channel {channel.mention}")
@client.command()
async def embed(ctx):
    e=discord.Embed(title="hello",description="m yname is hassan",colour=0x000)
    await ctx.send(embed=e)
@client.command()
async def clear(ctx,clearmsg=100):
    await ctx.channel.purge(limit=clearmsg)
#________________________________________________________
@client.command(description="Mutes the specified user.") #mute
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
#_______________________________________________________________
@client.command(description="Unmutes a specified user.") #unmut
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)
#________________________________________________________________
client.run('ODEzNzEzMTc4NzQ3MjA3Njgx.YDTTcw.f_oYCuP0S-CZwRMaNQAgITSFHdM')