def main():
    twitter = input("Write a sentence ").lower()
    vowels = ["a", "e", "i", "o", "u"]

    for x in twitter:
        if x.lower() not in vowels:
            print(x, end="")


main()
