from colors import Colors as c
from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['rope', 'hammer', 'chisel']),

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
player = None

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# get key with value function


def get_key(val):
    for key, value in room.items():
        if val == value:
            return key

    return "key doesn't exist"
# player approaches function


def playerAproaches(player):
    print(f'{c.OKBLUE}Player approaches {player.location.name}...\n{player.location.description}{c.ENDC}\n')


def playerLocation(player):
    print(f'{c.UNDERLINE}{c.WARNING}{c.BOLD}Current Location: {player.location.name}{c.ENDC}')


def printError():
    print(f'\n{c.FAIL}Command not recognized. Please try again{c.ENDC}\n')


def printCommands():
    commands = {
        'help': 'displays a list of commands',
        'n,e,s,w': 'to navigate in the cardinal direction',
        'q': 'command to quit instance',
        'player': 'displays player information',
        'search': 'searches the current location for items',
        'get': 'use syntax: get [item] after finding items to add item to player inventory',
        'get all': 'adds all items in current location to player inventory',
        'drop': 'use syntax: drop [item] to drop an item on the ground',
    }
    print(f'\n|---------- Adventure Game Commands ----------|\n')
    for (k, v) in commands.items():
        print(f' - {c.BOLD}{k}{c.ENDC}: {v}')
    print(f'\n|-------------------- End --------------------|\n')


while True:
    # prompts user to create new player
    if not player:
        prompt = input(
            f'\n{c.WARNING}*** WELCOME TO THE ADVENTURE GAME ***\n \nCreate a new character by typing in a name: ')
        if prompt == "q":
            print("Goodbye! Thanks for playing!")
            break
        else:
            player = Player(prompt, room['outside'])
            print(
                f'\n{c.OKGREEN}*** Created New Player ***\n\n{player}\n\n{c.ENDC}')
            # currentRoom = get_key(player.location)
    # adventure game starts
    else:
        try:
            # displays current user location
            playerLocation(player)
            # initialize input prompt
            prompt = input(
                f'\nEnter Command or type "help" for a list of commands: ').split()
            # Player Navigation
            if prompt[0].lower() in ("n", "s", "e", "w"):
                # check if navigation is possible
                if hasattr(player.location, f'{prompt[0]}_to'):
                    # update player location
                    player.setLocation(
                        getattr(player.location, f'{prompt[0]}_to'))
                    # print new location
                    print(f'\n{c.HEADER}Navigating......\n{c.ENDC}')
                    playerAproaches(player)
                else:
                    # print location not available
                    print('\nYou see nothing interesting in that direction..')
            # Player Room Search & Item pickup
            elif prompt[0].lower() == "search":

                print(f'\nYou begin searching the room....')
                # checks the room for items
                if not player.location.items:
                    print(
                        f'\n{c.FAIL}You fail to find any items{c.ENDC}\n')
                else:
                    print(
                        f'\n{c.OKGREEN}Aha! You find: {player.location.items}')
                    print(
                        f'\n{c.OKBLUE}Type "get [item]" to store item in your inventory OR Type "get all" to store all items in your inventory')
                    # prompt user to enter command
                    choice = input(f'\nWhat will you do?: ').split()
                    # check length of user input
                    if len(choice) == 1:
                        # exits loop if q
                        if choice[0] == "q":
                            pass
                        # prints error
                        else:
                            printError()
                    # picks up all items
                    elif choice[1].lower() == "all":
                        player.pickUpAll(player.location.items)
                        player.location.items = []
                    # picks up single item
                    elif choice[1].lower() in player.location.items:
                        # checks if user choice is in room
                        for item in player.location.items:
                            # there's a match
                            if item == choice[1].lower():
                                # adds to user inventory
                                player.pickUp(item)
                                # removes item from room
                                player.location.items.remove(item)
                    # prints error
                    else:
                        printError()
            # player drops item
            elif prompt[0].lower() == "drop":
                if prompt[1] in player.inventory:
                    for item in player.inventory:
                        if item == prompt[1]:
                            player.dropItem(item)
                            player.location.items.append(item)
                elif prompt[1].lower() == "all":
                    player.location.items.extend(player.inventory)
                    player.dropAll()
            # returns player info
            elif prompt[0].lower() == "player":
                print(
                    f'\n*** Player Info ***\n\n{player}\n\n\n*** Player Info End ***\n')
             # exit prompt
            elif prompt[0].lower() == "help":
                printCommands()
            elif prompt[0].lower() == "q":
                print("Goodbye! Thanks for playing!")
                break
            else:
                printError()

        except ValueError:
            print('error')
