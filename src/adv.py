from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Hello, what is your name? ")
player = Player(player_name, room['outside'])

# Write a loop that:
#
selection = ''
print(hasattr(player.location, 'n_to'))
while selection != 'q':
    print(f'Hello {player.name}, you are currently in room {player.location}')
    selection = input('Please enter a direction: ')
    try:
        if selection == 'north':
            if hasattr(player.location, 'n_to'):
                player.location = player.location.n_to
            else:
                print('you\'re not allowed to move there.')
        elif selection == 'south':
            if hasattr(player.location, 's_to'):
                player.location = player.location.s_to
            else:
                print('you\'re not allowed to move there.')
        elif selection == 'west':
            if hasattr(player.location, 'w_to'):
                player.location = player.location.w_to
            else:
                print('you\'re not allowed to move there.')
        elif selection == 'east':
            if hasattr(player.location, 'e_to'):
                player.location = player.location.e_to
            else:
                print('you\'re not allowed to move there.')
        else:
            print('You cannot travel there')
    except ValueError:
        print('Error, unrecognized input')


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
