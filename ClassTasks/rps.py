def main():
    player_choice = input("Rock, Paper or Scissors: ").lower

    match player_choice:
        case "rock":
            if generate_random == "paper":
                print("you lose")
            if generate_random == "rock":
                print("you tie")
            if generate_random == "scissors":
                print("you win")
        case "paper":
            if generate_random == "paper":
                print("you tie")
            if generate_random == "rock":
                print("you win")
            if generate_random == "scissors":
                print("you lose")


def generate_random():
    return "rock"
