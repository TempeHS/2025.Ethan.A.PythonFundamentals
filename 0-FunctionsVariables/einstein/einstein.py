def main():
    x = int(input("what is the mass? "))
    print("e = ", emc(x))


def emc(n):
    return n * 300000000**2


main()
