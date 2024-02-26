def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid_check = True
    digit_count = 0
    # Check the length in the string
    if len(s) < 2 or len(s) > 6:
        valid_check = False
        return valid_check
    if s[0].isdigit() or s[1].isdigit():
        valid_check = False
        return valid_check
    for char in s:
        # Make sure only valid characters are in the string, no special char or spaces
        if not char.isalnum():
            valid_check = False
            return valid_check
        # check to see if numbers are in the middle of the string
        if digit_count > 1 and char.isalpha():
            valid_check = False
            return valid_check
        # count the number of digits in the string
        if char.isdigit():
            digit_count += 1
        # Make sure the first number is not 0
        if digit_count == 1 and char == "0":
            valid_check = False
            return valid_check
    else:
        return valid_check


main()
