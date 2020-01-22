import random

play = ["rock", "paper", "scissors"]

computer = play[random.randint(0, 2)]

player = False

while player == False:

    player = input("rock, paper or scissors? or q to quit: ")

    if player == "q":
        break

    # Your logic below is fundamentally sound.  However, it is possible to shorten some of your code.
    # One idea is to use a data structure called a "lookup table" to determine the outcome of each game.  You could pass
    # numeric values (0, 1, or 2) for both the computer's move and the player's move to the lookup table.  The lookup
    # table would give you immediately back the result of who won the game. This way, fewer "if" and "elif" conditions
    # would be needed in your code. Here is an example of how a lookup table could be used in this way in your code:
    #
    # OUTCOME = {
    #     (0, 1): "You win! Paper covers rock.",
    #     (0, 2): "You lose! Rock breaks scissors.",
    #     (1, 0): "You lose! Paper covers rock.",
    #     (1, 2): "You win! Scissors cut paper.",
    #     (2, 0): "You win! Rock breaks scissors.",
    #     (2, 1): "You lose! Scissors cut paper.",
    # }
    #
    # By passing the number values (0, 1, or 2) for the computer's play and the user's play like below, the lookup table
    # can give one of the six possible win/lose results above.  The third line of code below prints "Tie!" if
    # the result is not in the lookup.
    #
    # computer_value = play.index(computer)
    # player_value = play.index(player)
    # print(OUTCOME.get((computer_value, player_value), "Tie!") + "Choose Again or Type q to quit")

    elif player == computer:
        print("Tie! Choose Again or Type q to quit")

    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player, "Choose Again or Type q to quit")

        else:
            print("You win!", player, "breaks", computer, "Choose Again or Type q to quit")

    elif player == "paper":
        if computer == "rock":
            print("You win!", player, "covers", computer, "Choose Again or Type q to quit")

        else:
            print("You lose!", computer, "cuts", player, "Choose Again or Type q to quit")

    elif player == "scissors":
        if computer == "paper":
            print("You win!", player, "cuts", computer, "Choose Again or Type q to quit")

        else:
            print("You lose!", computer, "breaks", player, "Choose Again or Type q to quit")

    else:
        print("That's not a play. Check your spelling and try again")

    player = False

    computer = play[random.randint(0, 2)]

