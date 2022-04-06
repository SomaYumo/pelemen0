import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= "a.")

@bot.event
async def on_ready():
    print(f"{bot.user} is connected")

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )

    await member.ban(reason = reason )
    await ctx.send(f'Участник {member.mention} был забанен' )

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )

    await member.kick(reason = reason )
    await ctx.send(f'Участник {member.mention} был кикнут')


@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, arg):
    if not member:
        await ctx.send("Кого ты хочешь, чтобы я выключил звук?")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"{member.name}был замьючен на {arg} seconds")

    await asyncio.sleep(int(arg))
    await member.remove_roles(role)
    await ctx.send("ok times up")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def clear(ctx, arg):
    await ctx.channel.purge(limit = int(arg))
    embed = discord.Embed(color = 0xff9900, title = 'Было очищено:', description = f'```{arg} сообщений 🌸```' )
    await ctx.send(embed = embed)
    print(f"команда, используемая: {ctx.message.author}, был очищен {arg} Сообщения")


bot.run("OTYwODA3NTE1MzQ2NTc5NDk3.Ykvzug.U1Mzf8r6N7xM3-EGxyx0kQc2zp4")