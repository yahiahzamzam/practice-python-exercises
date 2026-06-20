'''
while True:
    player1_input = input("Player 1: Rock - Paper - Scissors")
    player2_input = input("Player 2: Rock - Paper - Scissors")
    if player1_input == "Rock":
        if player2_input == "Paper":
            print("player 2 wins! Paper beats Rock")
        elif player2_input == "Rock":
            print("Its a draw!")
        else:
            print("Player 1 wins! Rock beats scissors")
    if player1_input == "Paper":
        if player2_input == "Scissors":
            print("player 2 wins! Paper beats Rock")
        elif player2_input == "Paper":
            print("Its a draw!")
        else:
            print("Player 1 wins! Rock beats scissors")
    if player1_input == "Scissors":
        if player2_input == "Rock":
            print("player 2 wins! Paper beats Rock")
        elif player2_input == "Scissors":
            print("Its a draw!")
        else:
            print("Player 1 wins! Rock beats scissors")

    select = input("Play again - Quit \nChoose:")

    if select == "Quit":
        break
'''
# Enhanced code
outcomes = {
    "Rock": {"Rock": "draw", "Paper": "loss", "Scissors": "win"},
    "Paper": {"Rock": "win", "Paper": "draw", "Scissors": "loss"},
    "Scissors": {"Rock": "loss", "Paper": "win", "Scissors": "draw"}
}

again = "y"

while again.lower() == 'y':
    # .capitalize() ensures inputs match our dictionary keys exactly
    p1 = input("Player 1 --> Rock, Paper, or Scissors? ").capitalize()
    p2 = input("Player 2 --> Rock, Paper, or Scissors? ").capitalize()
    print()

    # 1. Use a separate variable (result) so we don't overwrite our master dictionary!
    # 2. Add an alternative string default if players type an invalid move
    result = outcomes.get(p1, {}).get(p2, "Invalid choice entered.")

    print(f"Result: {result.upper()}")
    print("-" * 30)

    again = input("Type 'y' to play again, anything else to stop: ")
    print()
