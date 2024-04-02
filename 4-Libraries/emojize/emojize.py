import emoji


def emojize():
    Unemojized = input("What do you want to make an emoji? ")
    emojized = emoji.emojize(Unemojized)
    print(emojized)


if __name__ == "__main__":
    emojize()
