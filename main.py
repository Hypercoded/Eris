import discord

api_key = ""
bot_nick = "Eris"
command_prefix = "!"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if '{0.content}'.format(message) == 'Hello Eris!':
            channel = client.get_channel(message.channel.id)
            sender = message.author.nick
            await channel.send('Hello, ' + sender + "!")



client = MyClient()
client.run(api_key)
