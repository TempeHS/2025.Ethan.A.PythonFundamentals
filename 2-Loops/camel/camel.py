def main():
    camelCase = input("Write something in camelCase: ")
    for c in camelCase:
        if c.islower():
            print(c, end="")
        else:
            print("_" + c.lower(), end="")


main()
