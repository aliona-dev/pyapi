#!/usr/bin/python3

def showInstructions():
    # print a main menu and the commands
    print('''
Author: Aliona
RPG Game
========
Commands:
  go [direction]
  take [item]
  quit [quit]
  '2 special words' [secret victory]
''')
    print('Imagine you are in pitch darkness. It feels cold and you hear unusual sounds of creaking and growling.')
    print('Slowly your eye sight adjusts, there is smog on the ground and you are standing in the hallway.')
    print('Looking around you notice there are 3 distinct doors. To the west there is a bloodied red door,')
    print('To the east there is a blue scratched up door. To the north is a black door barely visible in the darkness')
    print('and when you turn south you can see a dim flickering light coming from inside of the mirror.')
    print("You cannot stay in this hallway forever, choose a direction, find clues, and find your way out!")


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    elif 'npc' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['npc'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Mirror',
        'east': 'Blue Door Room',
        'west': 'Red Door Room',
        'north': 'Black Door Room'
    },
    'Mirror': {
        'item': 'flute',
        'north': 'Hall'
    },

    'Blue Door Room': {
        'west': 'Hall',
        'npc': 'monster',
        'item': 'coin'
    },
    'Red Door Room': {
        'east': 'Hall',
        'item': 'cookies',
        'npc': 'glutton'
    },
    'Black Door Room': {
        'south': 'Hall',
        'npc': 'gatekeeper'
    }
}

# start the player in the Hall
currentRoom = 'Hall'
showInstructions()

# loop forever
while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 2)

    # quit and secret passage option
    if move[0] == 'quit':
        break
    elif move[0] == 'stop' and move[1] == 'imagining':
        print('Yesss, since this is all in your mind, you stopped imagining the nightmare. You Won!')
        break

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    # if they type 'take' first
    if move[0] == 'take':
        # if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' stored in your inventory for later use!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to take tell cant get the item.
        else:
            print('Can\'t get ' + move[1] + '!')

    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc']:
        if 'flute' in inventory and 'cookies' in inventory:
            print('Monster: That gluttonous pig, stole my cookies Arghh!')
            print("You: Don't be hangry, here are some cookies and I'll play you a song with this flute.")
            print('Monster: What a nice meal with a performance, I will spare you and give you a gift.')
            gift = rooms[currentRoom]['item']
            print("monster's gift: " + gift)
            del rooms[currentRoom]['npc']
            inventory.remove('cookies')
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc']:
        if 'flute' not in inventory and 'cookies' not in inventory:
            print('Arghh! OH NOOO, a hangry monster got you! You are lost in your mind forever! GAME OVER')
            break
        if 'flute' in inventory and 'cookies' not in inventory:
            print('The monster had fun dancing to your flute but ate you anyways because it was hungry!')
            break
        if 'cookies' in inventory and 'flute' not in inventory:
            print('Monster ate the cookies but was still angry and stomped on you. GAME OVER!')
            break

    if 'npc' in rooms[currentRoom] and 'glutton' in rooms[currentRoom]['npc']:
        print('You see a creepy looking demon with red eyes on top of piles of corpses in the kitchen eating cookies.')
        print('To your surprise, the Glutton Demon says: I am full and lazy, take these cookies and leave!')
        gift = rooms[currentRoom]['item']
        print("monster's gift: " + gift)
        del rooms[currentRoom]['npc']

    if currentRoom == 'Black Door Room' and 'coin' in inventory:
        print("Precious coin, I'll take it! You shall pass. The gatekeeper opened up the passage for you.")
        print('You escaped the dreary nightmare designed by your own imagination. YOU WON!')
        break
    elif currentRoom == 'Black Door Room' and 'coin' not in inventory:
        print('You shall not pass without payment, go away freeloader!')

