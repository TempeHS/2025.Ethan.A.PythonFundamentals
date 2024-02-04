def convert(emoticon):
    print(emoticon.replace(":)", "🙂").replace(":(", "🙁"))


def main():
    convert(input(str("Type a sentence ")))


main()
