# Версия 6

# импортируем все нужные библиотеки, импортируем по порядку надобности

import discord
from discord.ext import commands
import random
import json
import requests
import aiohttp
import io


# обозначаем префикс, благодаря которому бот будет распознавать команду пользователя

client = commands.Bot(command_prefix='>')


# начало бота (активность на сервере,что делает, текстовый статус)

@client.event
async def on_ready():
    activity = discord.Activity(name=">mhelp", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Makima is ready")


# help команда для вывода всех доступных команд

@client.command(pass_contex=True)
async def mhelp(ctx):
    embed = discord.Embed(title='remember these fucking commands', color=7419530)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_image(url='https://i.pinimg.com/564x/cb/f0/11/cbf011216f89b21f43d62afca3b4d4a9.jpg')
    embed.add_field(name='Talking', value='```>i_love_u``` ```>how_are_u``` '
                                          '```>hi``` ```>may_i_touch_your_tits``` '
                                          '```>what_do_you_think_about_power``` ```>should_i_treat_you_to_beer``` '
                                          '```>who_is_the_whore``` ```>what_do_you_think_about_denji``` '
                                          '```>what_do_you_want_to_eat``` ```>who_is_the_evil``` '
                                          '```>show_me_some_boobs``` ```>what_do_you_think_about_aki``` '
                                          '```>shall_we_watch_some_films``` '
                                          '```>what_is_your_dream``` ```>are_you_a_simp``` ```>are_you_hentai``` '
                                          '```>who_is_your_favorite_person``` '
                                          ' ```>i_want_to_be_your_dog``` ')
    embed.add_field(name='Attempt',
                    value='```>hug``` ```>wink``` ```>pat``` ```>horny``` ```>shreks``` ```>boobs``` '
                          '```>masturbation``` ```>blowjob``` ```>slap``` '
                          '```>sign_a_contract_with_makima``` ```>feed``` ```>slap``` ')
    await ctx.send(embed=embed)


# текстовые команды бота , разнообразные ответы на них

@client.command(pass_context=True)
async def hi(ctx):
    possible_responses = ['shut up, dirty dog', 'die worthless', 'how did you get me already']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention} ")


@client.command(pass_context=True)
async def may_i_touch_your_tits(ctx):
    possible_responses = ['sign a contract first', ' i did not expect anything else from a worthless virgin like you',
                          'here you are leans towards your hand', 'bang!']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def what_do_you_think_about_power(ctx):
    possible_responses = ['the corpse', 'denji’s little sister', 'the annoying one']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def should_i_treat_you_to_beer(ctx):
    possible_responses = ['i am always in', 'alcohol is worthless', 'do you want get drunk and nasty']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def who_is_the_whore(ctx):
    possible_responses = ['i am', 'power is', 'quanxi - the lesbian whore']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def what_do_you_think_about_denji(ctx):
    possible_responses = ['the simp', 'the perverted one']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def what_do_you_want_to_eat(ctx):
    possible_responses = ['toast bread', 'you', 'beer', 'chopstick']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def who_is_the_evil(ctx):
    possible_responses = ['the government keeps the essential evil by its side', 'denji is the sinner man',
                          'your mother is', 'people. I hate people. ']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def show_me_some_boobs(ctx):
    possible_responses = ['give me all of yourself then, and sign a contract first ', 'power can do it',
                          'shut up you fucking simp', 'see you at my place~', 'no. bang!']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def what_do_you_think_about_aki(ctx):
    possible_responses = ['the poor one', 'the sexy one', 'i want him to sign a contract',
                          'the piece of my mankind collection']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def shall_we_watch_some_films(ctx):
    possible_responses = ['let’s spend the whole day watching them', 'i hate bad films',
                          'we must watch at least ten till midnight']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def what_is_your_dream(ctx):
    possible_responses = ['equal love', 'being eaten by denji', 'kill power', 'kill men']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def are_you_a_simp(ctx):
    possible_responses = ['currently simping for the chainsaw man…', 'no you are',
                          'i am an independent working person.']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def are_you_hentai(ctx):
    possible_responses = ['I didn’t expect anything else from a worthless virgin like you', 'fucking simp',
                          'only for you', 'only for denji', 'quanxi is ']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def who_is_your_favorite_person(ctx):
    possible_responses = [' i only appreciate dogs', 'not you, fucking simp', 'the chainsaw man']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_contex=True)
async def i_want_to_be_your_dog(ctx):
    possible_responses = ['you don’t even deserve to be alive', 'sign a contract with me~~ ',
                          'you are a worthless simp']
    await ctx.send(f"{random.choice(possible_responses)} {ctx.message.author.mention}")


@client.command(pass_context=True)
async def how_are_u(ctx):
    possible_responses = ['ha, a corpse talking', 'i bought you a dog food']
    await ctx.send(f"{random.choice(possible_responses)}{ctx.message.author.mention}")


@client.command(pass_context=True)
async def i_love_u(ctx):
    possible_responses = ['you are my dog now)', 'after you eat the feed']
    await ctx.send(f"{random.choice(possible_responses)}{ctx.message.author.mention}")

# команды с выводом изображения api

@client.command()
async def pat(ctx):
    response = requests.get("https://some-random-api.ml/animu/pat")  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=7419530, title='fucking simp')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed


@client.command()
async def wink(ctx):
    response = requests.get("http://some-random-api.ml/animu/wink")
    json_data = json.loads(response.text)

    embed = discord.Embed(color=7419530, title='dirty dog')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@client.command()
async def hug(ctx):
    response = requests.get("https://some-random-api.ml/animu/hug")
    json_data = json.loads(response.text)

    embed = discord.Embed(color=7419530, title='find yourself a girl')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)

@client.command()
async def feed (ctx, member:discord.Member = None):
    feedGIF = [
        "https://c.tenor.com/tyQ9H4slRDkAAAAC/kon-yui.gif",
        "https://data.whicdn.com/images/81561319/original.gif",
        "https://thumbs.gfycat.com/EagerSpectacularHoverfly-max-14mb.gif",
        "https://64.media.tumblr.com/4d160635539ef31d8b058bc3e35a907c/tumblr_p4e113SOw91wn2b96o1_400.gifv",
        "https://i.pinimg.com/originals/7a/cb/20/7acb209c594f42e0d56b87d70421c85d.gif",
        "https://c.tenor.com/0kInGG3jn1kAAAAC/anime-corn.gif",
        "https://c.tenor.com/JHqOKnXVNDQAAAAC/azunom-feed.gif",
        "https://c.tenor.com/QL5EG0op4uQAAAAC/kamuikanna-anime.gif",
        "https://c.tenor.com/_Wn5KdSnphEAAAAd/anime-feed-anime.gif",
        "https://c.tenor.com/CHTk5L8ls8cAAAAd/eat-food.gif",
    ]

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
            f"{ctx.author.mention} ",
            f"{ctx.author.mention} ",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",
        ]
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(embed=embed)



@client.command()
async def slap (ctx, member:discord.Member = None):
    feedGIF = [
        "https://c.tenor.com/hNa8BhraaXsAAAAC/anime-nagatoro.gif",
        "https://c.tenor.com/1lJTSPaUfKkAAAAd/chika-fujiwara-fwap.gif",
        "https://c.tenor.com/_RZ87T5zbzsAAAAC/aqua-anime.gif",
        "https://c.tenor.com/FKwVjGlrp1YAAAAd/higurashi-sotsu.gif",
        "https://c.tenor.com/klNTzZNDmEgAAAAC/slap-hit.gif",
        "https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif",
        "https://c.tenor.com/EfhPfbG0hnMAAAAC/slap-handa-seishuu.gif",
        "https://c.tenor.com/vr7tTAEuj1QAAAAC/baka-slap.gif",
        "https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif",
        "https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif",
        "https://c.tenor.com/aP7Du3RWX6YAAAAC/slap-anime.gif",
        "https://c.tenor.com/eS3xAaYHDeMAAAAC/ass-ass-slap.gif",
    ]

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} oh, you.. little naughty human ///-//",
            f"{ctx.author.mention} I did not expect to hear anything else from a slave like you. ",
            f"{ctx.author.mention} can you do something I ask you first?",
            f"{ctx.author.mention}  sign a contract then.",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="slap", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",
        ]
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="slap", value=(feed))
        await ctx.send(embed=embed)

@client.command()
async def boobs (ctx, member:discord.Member = None):
    feedGIF = [
        "https://www.gifmeat.com/wp-content/uploads/2017/05/Hentai-Hitou-Meguri-The-Animation.gif",
        "https://www.gifmeat.com/wp-content/uploads/2016/04/Grabbing-big-tits-hentai.gif",
        "https://www.elergonomista.com/wp-content/uploads/2019/05/h34.gif",
        "https://i1.wp.com/uncensored-hentai.top/wp-content/uploads/2020/07/anime-hentai-",
        "https://blowjobgif.net/albums/2018/03/03/23/1/hentai-huge-boob-foursome-blowjob.gif",
        "https://blowjobgif.net/albums/2017/06/06/23/1/big-boobs-hentai-babe-porn-gif-for-more-hot-photos-go-to-hotgirlhub.gif",
        "https://hentai-gif.top/wp-content/uploads/2021/07/hentai-boobs-gif-2.gif",
    ]

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
            f"{ctx.author.mention} ",
            f"{ctx.author.mention} ",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="boobs", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",
        ]
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="boobs", value=(feed))
        await ctx.send(embed=embed)


@client.command()
async def shreks (ctx, member:discord.Member = None):
    feedGIF = [
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-blowjob-1_001-min-3.gif",
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-blowjob-1_001-min-7.gif",
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-blowjob-1_001-min-5.gif",
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-Hentaj-porno-anime-gifki-anal-ebut-v-popu-3-1.gif",
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-ts-2.gif",
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-ts-8.gif",
        "https://www.elergonomista.com/wp-content/uploads/2019/05/h5.gif",
        "https://www.elergonomista.com/wp-content/uploads/2019/05/h9.gif",
        "https://www.elergonomista.com/wp-content/uploads/2019/05/h27.gif",
        "https://blowjobgif.net/albums/2017/06/26/17/1/hentai-gif-29.gif",



    ]

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="shreks", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",
        ]
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="shreks", value=(feed))
        await ctx.send(embed=embed)


@client.command()
async def masturbation (ctx, member:discord.Member = None):
    feedGIF = [
        "https://hentai-gif.top/wp-content/uploads/2021/08/GT-blowjob-1_001-min-2.gif",
        "https://blowjobgif.net/albums/2017/07/15/11/1/hentai-gif-34.gif",

    ]

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="masturbation", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",
        ]
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="masturbation", value=(feed))
        await ctx.send(embed=embed)

@client.command()
async def blowjob (ctx, member:discord.Member = None):
    feedGIF = [
        "https://blowjobgif.net/albums/2018/02/22/3/1/hentai-gif-49.gif",
        "https://blowjobgif.net/albums/2017/07/17/7/1/hentai-69-pov-blowjob.gif",
        "https://blowjobgif.net/albums/2017/07/15/11/1/hentai-gif-34.gif",
        "https://blowjobgif.net/albums/2017/04/12/5/1/hentai-blowjob-2.gif",
        "https://blowjobgif.net/albums/2016/08/14/8/1/hentai-blowjob-cumshot.gif",
        "https://blowjobgif.net/albums/2019/02/18/3/1/blowjob.gif",

    ]

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
            f"{ctx.author.mention} ",
            f"{ctx.author.mention}  ",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="blowjob", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",
        ]
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=7419530)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="blowjob", value=(feed))
        await ctx.send(embed=embed)

@client.command()
async def horny(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.trigger_typing()
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}') as af:
            if 300 > af.status >= 200:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "horny.png")
                em = discord.Embed(
                    title="i did not expect anything else from a virgin",
                    color=7419530,
                )
                em.set_image(url="attachment://horny.png")
                await ctx.send(embed=em, file=file)
            else:
                await ctx.send('No horny :(')
            await session.close()


# команды для того, чтобы учатсник сервера получил ту или иную роль на сервере

@client.command()
async def sign_a_contract_with_makima(ctx):
    member = ctx.message.author
    role_1 = member.guild.get_role(917876285714350120)
    await member.add_roles(role_1)

# запуск бота

client.run("Token")