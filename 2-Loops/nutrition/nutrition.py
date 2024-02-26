def main():
    fruit = input("Name a fruit: ")
    fruits = {
        "apple": "130 cal",
        "avacado": "50 cal",
        "banana": "110 cal",
        "cantaloupe": "50 cal",
        "grapefruit": "60 cal",
        "grapes": "90 cal",
        "honeydew melon": "50 cal",
        "kiwifruit": "90 cal",
        "lemon": "15 cal",
        "lime": "20 cal",
        "nectarine": "60 cal",
        "orange": "80 cal",
        "peach": "60 cal",
        "pear": "100 cal",
        "pineapple": "50 cal",
        "plums": "70 cal",
        "strawberries": "130 cal",
        "sweetcherries": "130 cal",
        "tangerine": "130 cal",
        "watermelon": "130 cal",
    }
    if fruit in fruits:
        print(f" A {fruit} has {fruits[fruit]}")
    else:
        print("Invalid")


main()
