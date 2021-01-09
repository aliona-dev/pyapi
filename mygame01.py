#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')
  print('Image you are in a a hallway and all you see are doors to the s,w,and n')
def showStatus():
  #print the player's current status
  print('---------------------------') 
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'mirror',
                  'east'  : 'Blue Door',
                  'item'  : 'flute',
                  'west'  : 'Red Door',
                  'north' : 'Black Door'
                },

            'Blue Door' : {
                  'west' : 'Hall',
                  'item' : 'monster'
                },
            'Red Door' : {
                  'east' : 'Hall',
                  'item' : 'speacial gold coin'
               },
            'Black door' : {
                  'north' : 'Dining Room',
                  'item' : 'gate keeper'
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()
    move = ''
    while move == '':  
        move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
  else:
      print('You can\'t go that way!')

  #if they type 'take' first
  if move[0] == 'take' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' stored in your inventory for later use!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom] and flute not in inventory:
      print('A monster has got you... GAME OVER!')
      break
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom] and flute in inventory:
      print('you calmed the beast with your magic flute. I would leave this room if I were you') 
elif currentRoom == 'Black door' and 'special gold coin' in inventory and 'gate keeper' in rooms[currentRoom]:
    print('You escaped the dreary place with the ultra rare coin ... YOU WIN!')
    break

