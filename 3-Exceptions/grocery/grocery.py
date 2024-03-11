def main():
    shopping_list = {}
    while True:
        try:
            item = input().upper().strip()
            if item not in shopping_list:
                shopping_list[item] = 1
            else:
                shopping_list[item] = +1
        except EOFError:
            sorted_dict = dict(sorted(list(shopping_list.items())))
            for item in sorted_dict:
                print(sorted_dict[item], item, sep=" ")
        except KeyError:
            pass


main()
