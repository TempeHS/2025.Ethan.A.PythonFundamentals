def main():
    print(
        f"Choose a menu item",
        "1. Item 1",
        "2. Item 2",
        "3. Item 3",
        "4. exit",
        sep="\n",
    )
    while True:
        User_input = input("")
        if User_input.startswith("1"):
            print("Thankyou For choosing 1")
        elif User_input.startswith("2"):
            print("Thankyou For choosing 2")
        elif User_input.startswith("3"):
            print("Thankyou For choosing 3")
        elif User_input.startswith("4"):
            print("thankyou For using this menu")
            break


main()
