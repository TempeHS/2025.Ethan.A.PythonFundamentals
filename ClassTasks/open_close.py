def main():
    with open("number.txt", "r") as file:
        for line in file:
            number = int(line)
            new_number = number + 1
    with open("number.txt", "w") as file:
        file.write(f"{new_number}")


main()
