<p align="center">
      <img src="https://docs.disnake.dev/en/stable/_static/disnake.svg" width="726">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Language-Python-blue?cacheSeconds=https%3A%2F%2Fwww.python.org%2F" alt="Language Python">
   <img src="https://img.shields.io/badge/Version-3.12-red?link=https%3A%2F%2Fpeps.python.org%2Fpep-0693%2F" alt="Version 3.12">
   <img src="https://img.shields.io/badge/Library-Disnake-yellow?link=https%3A%2F%2Fdocs.disnake.dev%2Fen%2Fstable%2F" alt="Library Disnake">
   <img src="https://img.shields.io/badge/License-MIT-purple?link=https%3A%2F%2Fgithub.com%2Fgit%2Fgit-scm.com%2Fblob%2Fmain%2FMIT-LICENSE.txt" alt="License MIT">
</p>

## About

A simple code example to automatically create voice channels for your discord server.

## Documentation

### 1. Installation:
+ Clone the repository from GitHub.
+ Install dependencies using pip install -r requirements.txt.

### 2. Getting Started:
+ Configure your token in [bot.py](https://github.com/cr1stalyoung/discord-voice-channel-simple/blob/master/bot.py).

### 3. Usage:
In [create_room.py](https://github.com/cr1stalyoung/discord-voice-channel-simple/blob/master/cogs/create_room.py) you need to configure list_channel, list_category, channel_settings.
+ **list_channel**: list of voice channel IDs. When switched to a new voice channel is created and the user is automatically connected to it.
+ **list_category**: list of category IDs specifies in which categories the voice channel will be automatically deleted if the number of participants is zero.
+ **channel_settings**: dictionary containing information about the channel to be created. The key is the id of the channel after which the voice channel is created, the values of the key contain the category where the channel is created, the name of the channel and the limit of participants in the voice channel.

## License

This project is licensed under the terms of the MIT License - see the [LICENSE.md](https://github.com/cr1stalyoung/discord-voice-channel-simple/blob/master/LICENSE.md) file for details.
