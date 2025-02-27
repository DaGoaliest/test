potions = { "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] }

for potion in potions:
    print(potion)

choosePotion = input("Please chose a potion from the list above: ")

if choosePotion in potions:
    print("Ingredients needed:", potions[choosePotion])
else:
    print("Potion not found. Please choose a potion from the list.")

if choosePotion in potions:
    ingredients = potions[choosePotion]
    while ingredients:
        buy = input(f"Do you want to buy {ingredients[0]}? (yes/no): ")
        if buy.lower() == 'yes':
            print(f"Bought {ingredients.pop(0)}")
        else:
            print("Shopping stopped.")
            break
    if not ingredients:
        print("Congratulations! You have bought all the ingredients for the", choosePotion)
