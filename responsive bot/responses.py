import random
def handle_response(message) -> str:
    p_message = message.strip().lower()

    if p_message == 'hello':
        return 'Hey, how are you doing today?'
    elif p_message == 'roll':
        return str(random.randint(1, 6))
    elif p_message == '!help':
        return "`This is a help message that you can modify.`"
    elif p_message == 'How are you?':
        return 'I\'m well!'
    elif p_message == 'how is the weather today?':
        return 'I am not too sure I have not been outside today.'
    else:
        return "I don't know what you said"

def handle_stat(message) -> str:

    league_user_name =  message.split(' ')[1]
    print(league_user_name)

    return 'https://op.gg/summoners/na/' + league_user_name

def handle_luck(message) -> str:
    probabilty = random.randint(1, 100)

    if probabilty > 1:
        return 'https://www.vets4pets.com/siteassets/species/cat/kitten/tiny-kitten-in-sunlight.jpg?w=585&scale=down'
    else:
        return 'https://www.garzablancaresort.com/blog/wp-content/uploads/2020/03/oSRR9qHQ.jpeg'