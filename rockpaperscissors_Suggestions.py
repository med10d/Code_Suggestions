from random import randint


def rps():
    x = ("Rock", "Paper", "Scissors")
    comp = x[randint(0, 2)]
    player = False
    char1 = "p"
    char2 = "q"

    while player == False:  # To make an infinite loop, you can replace this line of code with the commented line below.
    # while True:

        player = input("""Welcome to Rock, Paper, Scissors! Type 'p' to play or 'q' to quit: """)
        # The commented lines below will break out of the infinite loop and end the game, if the user types "q".
        # If the user types something other than "p" or "q", it will ask them the question above again.

        # if player == "q":
        #     break
        # if player != "p":
        #     continue

        player = input("Select Rock, Paper, or Scissors: ")

        if player == comp:
            print("It's a tie! Press ")

        elif player == "Rock" and comp == "Paper":
            print("Computer chose paper, you lose.")
        elif player == "Paper" and comp == "Rock":
            print("Computer chose rock, you win!")
        elif player == "Scissors" and comp == "Paper":
            print("Computer chose paper, you win!")
        elif player == "Paper" and comp == "Scissors":
            print("Computer chose scissors, you lose.")
        elif player == "Rock" and comp == "Scissors":
            print("Computer chose scissors, you win!")
        elif player == "Scissors" and comp == "Rock":
            print("Computer chose rock, you lose.")
        elif player == "Rock" and comp == "Paper":
            print("Computer chose paper, you lose.")
        player = False
        comp = x[randint(0, 2)]


rps()