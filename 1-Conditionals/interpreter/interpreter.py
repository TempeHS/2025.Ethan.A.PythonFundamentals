def main():
    equation = input("input an equation ")
    (
        x,
        y,
        z,
    ) = equation.split(" ")
    x_f = float(x)
    z_f = float(z)

    if y == ("+"):
        answer = x_f + z_f
    if y == ("-"):
        answer = x_f - z_f
    if y == ("/"):
        answer = x_f / z_f
    if y == ("*"):
        answer = x_f * z_f
    print(round(answer, 2))


main()
