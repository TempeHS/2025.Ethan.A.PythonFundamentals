def main():
    mealtime = input("What time is it? ")
    mealtime = convert(mealtime)
    if 7.0 <= mealtime <= 8.0:
        print("Breakfast time")
    elif 12.0 <= mealtime <= 13.0:
        print("Lunch time")
    elif 18.0 <= mealtime <= 19.0:
        print("Dinner time")
    else:
        print("Its not time to eat")


def convert(time):
    hours, minutes = time.split(":")
    f_minutes = float(minutes) / 60
    f_hours = float(hours)
    return f_hours + f_minutes


if __name__ == "__main__":
    main()
