def main():
    Fuel = input("Input in a fraction your fuel ")
    (x, y, z) = Fuel.split(" ")
    x_f = float(x)
    z_f = float(z)
    if y == ("/"):
        Fuelcount = (x_f / z_f) * 100
        RFuelcount = int(Fuelcount)
        if 1 <= Fuelcount <= 99:
            print(f"{RFuelcount}% remaining fuel")
        elif Fuelcount <= 1:
            print("E")
        elif Fuelcount >= 99:
            print("F")


try:
    main()
except (ValueError, ZeroDivisionError):
    print("Please input a fraction in x/y format")
