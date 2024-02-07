def convert(emoticon):
    print(
        emoticon.replace(":)", "🙂")
        .replace(":(", "🙁")
        .replace(":I", "😐")
        .replace(">:[", "👿")
        .replace("small", "small 🍆")
    )


def main():
    convert(input(str("Type a sentence ")))


main()
