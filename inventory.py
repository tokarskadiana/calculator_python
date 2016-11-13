from collections import Counter
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','dagger']
def add_to_inventory(inventory, items):
    return dict(Counter(inventory) + Counter(items))
def display_inventory(inventory):
    print('Inventory:')
    for key,value in inventory.items():
        print(value, ' ', key)
    print('Total number of items: ', sum(inventory.values()))
def print_table(inventory, order=None):
    print('Inventory:')
    print('\tcount\titem name')
    for k,v in inventory.items():
        print('{:>10} {:>10}'.format(v,k))
    print('Total number of items: ', sum(inventory.values()))
inv = add_to_inventory(inv,loot)
print_table(inv)
