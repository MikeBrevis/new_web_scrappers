inventory = [
    {
        "name": "car", 
        "quantity": 3, 
        "category": "toys"
        },
    {
        "name": "car",
        "quantity": 2,
        "category": "toys"
        },

]

# extracting values from a particular dictionary
print(inventory[0])

for x, i in inventory[0].items():
    print("{} : {}".format(x, i))

# Print values of a dictionary 
print(inventory[1].values())

# i represent each dictionay in the list
for i in inventory : 
    print(i["name"])

# Create a copy o the dictionary
my_copy = inventory.copy()
print(my_copy)


