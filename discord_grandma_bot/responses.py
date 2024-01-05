import random
def handle_response(message) -> str:
    p_message = message.strip().lower()

    if p_message == 'hello grandma':
        return 'Hey, you are looking handsome today!'
    
    elif p_message == 'roll':
        return str(random.randint(1, 6))
    
    elif p_message == '!help':
        return "`This is a help message that you can modify.`"
    elif p_message == 'really grandma?':
        return 'Of course!'
    elif p_message == 'grandma is eunji dumb?':
        return 'Damn right she is'
    elif p_message == 'grandma am i looking handsome today?':
        return 'No you ugly'
    elif p_message == 'fuck you grandma':
        return 'shut up lil nig**'
    elif p_message == 'grandma who\'s better? me or eunji?':
        return "burhan is way better"
    elif p_message == 'grandma who is the nicest person you know?':
        return 'burhan'
    elif p_message == 'grandma can you tell jay to shut up?':
        return 'shut the fuck up jay'
    elif p_message == 'i miss grandma':
        return 'I am right here.'
    elif p_message == 'grandma is stan better or me?':
        return 'You are way better than that fucking loser'
    elif p_message == 'grandma do you wanna tft call with stan?':
        return 'Fuck no'
    elif p_message == 'grandma is stan being cringe again?':
        return 'yeah shut your bitch ass up stan'
    elif p_message == 'grandma it\'s erins birthday':
        return 'Happy birthday, don\'t eat the cake all by yourself fatass. Leave some for grandma'
    elif p_message == 'grandma it\'s joshs birthday':
        return 'HAPPY 😊 BIRTHDAY 🎂 HANDSOME!!! 😎😜😩😆 Its time 🕦 to get LIT 🔥 for your special 👉😎👈 BIRTHDAY 🎊! You finna turn UP 👆🤯 and get DOWN 👇🤩 on this BEAUTIFUL day 😩💕 because you\'re 👀 a CHAMP🎖and a COOL 😎 DUDE 💪! Get all that 💰🤑 and 🤪🍹 and HAVE A HAPPY BIRTHDAY 🎊🎊🎊 don\'t forget 😤😤 to eat your cake 🍰😋 or your other cake 🍑😩👅💦 because today you the MAN 🤠😏🤤'
    elif p_message == 'thank you grandma':
        return 'You\'re welcome my cutie'
    #return "I don't know what you said"

def handle_stat(message) -> str:

    league_user_name =  message.split(' ')[1]
    print(league_user_name)

    return 'https://op.gg/summoners/na/' + league_user_name

def handle_luck(message) -> str:
    probabilty = random.randint(1, 100)

    if probabilty > 1:
        return 'https://www.vets4pets.com/siteassets/species/cat/kitten/tiny-kitten-in-sunlight.jpg?w=585&scale=down'
    else:
        return 'https://i.kym-cdn.com/photos/images/newsfeed/002/444/001/a3e.jpg'