import discord
from discord.ext import commands

# *** List of Intents ***
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
# *** List of Intents ***

client = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=intents,
)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='create channel'))


@client.event
async def on_voice_state_update(member, before, after):
    try:
        listChannelBeforeDelete = [
            id_channel,  # Channel IDs that will not be deleted in categories.
        ]
        listCategoryDelete = [
            id_category, # category IDs of the categories in which the created channel will be deleted.
        ]
        if before.channel.members == [] and before.channel.id not in listChannelBeforeDelete:
            if before.channel.category_id in listCategoryDelete:
                await before.channel.delete()
    except Exception as error:
        print(f"An error occurred [delete_voice]: >>> {error}")

    try:
        listChannelIdAfter = [
            id_channel,  # channel IDs after switching to which custom channel will be created for the user.
        ]
        channel_id = after.channel.id

        if channel_id in listChannelIdAfter:
            if channel_id == id_channel: # channel id of the channel after which the custom channel will be created
                category_id = id_category # category id of the category where the channel is to be created
                voice_prefix = name_channel # channel of room
                user_limit = 2 # limit of channel

            CategoryCreateNewChannel = discord.utils.get(after.channel.guild.categories, id=category_id)
            existing_channel_names = [channel.name for channel in CategoryCreateNewChannel.channels]

            count = 1
            voice_channel_name = f"{voice_prefix} #{count}"
            while voice_channel_name in existing_channel_names:
                count += 1
                voice_channel_name = f"{voice_prefix} #{count}"

            voice = await after.channel.guild.create_voice_channel(name=voice_channel_name,
                                                                   category=CategoryCreateNewChannel, user_limit=user_limit)
            await voice.set_permissions(member, connect=True, mute_members=True, move_members=True,
                                        manage_channels=True)
            await member.move_to(voice)
    except Exception as error:
        print(f"An error occurred [create_voice]: >>> {error}")

client.run('TOKEN')
