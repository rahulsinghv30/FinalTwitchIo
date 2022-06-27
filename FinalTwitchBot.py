from twitchio.ext import commands, routines
import random, sched, time 

class Bot(commands.Bot):
    def __init__(self):
       # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
       super().__init__(token='oauth:a47vhfexb2e2roryfpoh01c51iax0o', prefix='!', initial_channels=['hypercoolness30'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
            # Messages with echo set to True are messages sent by the bot...
            # For now we just want to ignore them...
            if message.echo:
                return

            # Print the contents of our message to console...
            print(message.content)

            # Since we have commands and are overriding the default `event_message`
            # We must let the bot know we want to handle and invoke our commands...
            await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        print('Hello')
        await ctx.send(f'Hello {ctx.author.name}!')
    @commands.command()
    async def randomNum(self, ctx: commands.Context):
        num = random.randint(0, 10)
        print(num)
        #send a random number between 1-10
        await ctx.send(f'random #: {num}!')
    
    @routines.routine(seconds=1.0, iterations=5)
    async def remember(arg: str):
        print(f'Remember {arg}!')
        
    remember.start('to like and subscribe!')
        
bot = Bot()
bot.run()
