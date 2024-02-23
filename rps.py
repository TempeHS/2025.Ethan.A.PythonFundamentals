def computer_choice():
    return "rock"


def player_choice():
    games_played = 0
    while games_played < 3:
        games_played = games_played + 1
        player_choice = input("Choose rock, paper or scissors:   ").lower()
        match computer_choice():
            case "rock":
                if player_choice == "rock":
                    print("You Tie")
                elif player_choice == "paper":
                    print("You Win")
                elif player_choice == "scissors":
                    print("You Lose")
            case "scissors":
                if player_choice == "rock":
                    print("You Win")
                elif player_choice == "paper":
                    print("You Lose")
                elif player_choice == "scissors":
                    print("You Tie")
            case "paper":
                if player_choice == "rock":
                    print("You Lose")
                elif player_choice == "paper":
                    print("You Tie")
                elif player_choice == "scissors":
                    print("You Win")


player_choice()
