def main():

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    price = 0
    try:
        while True:
            order = input("What do you want to order? ")
            if order in menu:
                price = price + menu[order]
                print(f"${price}")
    except EOFError:
        pass


main()
