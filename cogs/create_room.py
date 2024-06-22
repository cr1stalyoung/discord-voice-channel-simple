import disnake
from disnake.ext import commands


class CreateRoom(commands.Cog):
    def __init__(self, bot):
        self._bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("The create_room.py file has started working")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        list_channel = [1207336758694379520, 1207336826210357309, 1207330615670743170]
        list_category = [1207336446147698808, 1207336188843917312, 1207335752409546803]
        channel_settings = {
            1207336758694379520: {
                "category_id": 1207336446147698808,
                "voice_prefix": "Duo Room",
                "user_limit": 2,
            },
            1207336826210357309: {
                "category_id": 1207336188843917312,
                "voice_prefix": "Trios Room",
                "user_limit": 3,
            },
            1207330615670743170: {
                "category_id": 1207335752409546803,
                "voice_prefix": "Squad Room",
                "user_limit": 4,
            }
        }

        try:
            if after.channel and after.channel.id in list_channel:
                settings = channel_settings[after.channel.id]
                category_id = settings["category_id"]
                voice_prefix = settings["voice_prefix"]
                user_limit = settings["user_limit"]

                category = disnake.utils.get(after.channel.guild.categories, id=category_id)
                existing_channel_names = {channel.name for channel in category.channels}
                count = 1
                while True:
                    voice_channel_name = f"{voice_prefix} #{count}"
                    if voice_channel_name not in existing_channel_names:
                        break
                    count += 1

                voice_channel = await after.channel.guild.create_voice_channel(
                    name=voice_channel_name,
                    category=category,
                    user_limit=user_limit
                )
                await voice_channel.set_permissions(member, connect=True, mute_members=True, move_members=True)
                await member.move_to(voice_channel)
            elif len(before.channel.members) == 0 and before.channel.id not in list_channel:
                if before.channel.category_id in list_category:
                    await before.channel.delete()
        except Exception as error:
            print(f"An error occurred [on_voice_state_update]: {error}")


def setup(bot):
    bot.add_cog(CreateRoom(bot))
