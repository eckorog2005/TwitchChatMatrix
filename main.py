from twitchio.ext import commands

import configparser


class Bot(commands.Bot):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        oauthToken = config['credentials']['oauth']
        mainChannel = config['channels']['main']
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=oauthToken, prefix='?', initial_channels=[mainChannel])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()