# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, health=100, score=0, inventory=['pickaxe', 'map', 'bronze_sword', 'compass']):
        self.name = name
        self.location = location
        self.health = health
        self.score = score
        self.inventory = inventory

    # updates the Player's location
    def setLocation(self, location):
        self.location = location

    # drop item
    def dropItem(self, item):
        self.inventory.remove(item)
        print(f'\nYou place the {item} on the ground')
        print(f'{self.inventory}\n')

    # drop all items
    def dropAll(self):
        self.inventory = []
        print(f'\nYou place all your items on the ground')

    # pickup item
    def pickUp(self, item):
        self.inventory.append(item)
        print(f'\nYou place the {item} in your inventory')
        print(f'{self.inventory}\n')

    # pickup all items
    def pickUpAll(self, items):
        self.inventory.extend(items)
        print(f'\nYou place the {items} in your inventory')
        print(f'{self.inventory}\n')

    def __str__(self):
        return f'Name: {self.name} \nLocation: {self.location.name} \nHealth: {self.health} \nScore: {self.score} \nInventory: {self.inventory}'
