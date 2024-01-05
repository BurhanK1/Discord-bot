import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
async def send_stat(message, user_message):
    try:
        response = responses.handle_stat(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)
async def send_luck(message, user_message):
    try:
        response = responses.handle_luck(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

intents = discord.Intents.default()
intents.typing = True  # You can adjust these based on your bot's needs
intents.presences = True
intents.message_content = True
def run_discord_bot():
    TOKEN = 'MTE1ODA4MjgwMjc4OTY2Njg0Nw.GX4NbL.AYXAyTczH_wQ3xuxFWvr1XkkorJfPMyPeroxEU'
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author) #name of the user that sent the message
        user_message = str(message.content) #message that the author sent
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})") #for debugging

        if user_message[0] == '%':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif user_message[0] == '!':
            await send_stat(message, user_message)
        elif user_message == '?luck':
            await  send_luck(message, user_message)
        else:
            await send_message(message, user_message, is_private=False)
    

    client.run(TOKEN)