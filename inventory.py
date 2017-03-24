'''
Created on Mar 7, 2017

@author: dalton
'''

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if inventory.get(i, 0) == 0:
            inventory[i] = 1
        else:
            inventory[i] = inventory[i] + 1
    return(inventory)
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)