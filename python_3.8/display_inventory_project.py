# inventory.py

"""Fantasy Game Inventory"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("inventory: \n")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items : ' + str(item_total))

display_inventory(stuff)

print()

"""Combine a List of loot to a player inventory"""
def add_loot_to_inventory(inventory, loot_list):
    for loot in loot_list:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)

inv = {'gold coin': 50, 'rope': 4}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_loot_to_inventory(inv, dragon_loot)
display_inventory(inv)
