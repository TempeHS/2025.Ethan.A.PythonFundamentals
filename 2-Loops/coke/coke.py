def main():
    print("please pay 50c")
    total_cost = 50
    coins_paid = 0

    while True:
        insert_money = int(input("Insert a 5c, 10c or 25c coin: "))
        if insert_money == 25 or insert_money == 10 or insert_money == 5:
            total_cost = total_cost - insert_money
            coins_paid = coins_paid + insert_money
        if coins_paid >= 50:
            print("Thankyou for purchasing our coke")
            return False
        else:
            print("please pay", total_cost)


main()
