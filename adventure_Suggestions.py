class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.moves = 0

# Your code works great for allowing the user to navigate to the different rooms in your adventure game. These comments
# are suggestions for how you could potentially condense your code, allowing you to reuse some parts of your code.

# Instead of creating four different Room classes, you could try creating one Room class. Then, you could initialize
# four room objects, by passing in values to the constructor of the Room class that make each room different. Here is an
# example of how to do this:
#
# class Room():  # Probably do not want to inherit Player in this class, because Room is not a "type of" Player.
#     def __init__(self, room, direction1, neighbor1, direction2, neighbor2):
#         self.room = room
#         self.direction1 = direction1
#         self.neighbor1 = neighbor1
#         self.direction2 = direction2
#         self.neighbor2 = neighbor2
#
#     # The code below uses the class variables defined above in the return message, instead of hardcoding the message.
#     def __repr__(self):
#         return (f"Welcome to Room {self.room}. Use {self.direction1} to move to Room {self.neighbor1}, or "
#                 f"{self.direction2} to move to Room {self.neighbor2}.")
class Room_1(Player):
    def __init__(self):
        self.room = 1

    def __repr__(self):
        return "Welcome to Room 1. Use d to move to Room 2, or s to move to Room 3."


class Room_2(Player):
    def __init__(self):
        self.room = 2

    def __repr__(self):
        return "Welcome to Room 2. Use a to move to Room 1, or s to move to Room 4."


class Room_3(Player):
    def __init__(self):
        self.room = 3

    def __repr__(self):
        return "Welcome to Room 3. Use w to move to Room 1, or d to move to Room 4."


class Room_4(Player):
    def __init__(self):
        self.room = 4

    def __repr__(self):
        return "Welcome to Room 4. Use w to move to Room 2, or a to move to Room 3."


class Game:
    def __init__(self):
        name = input("What is your name, adventurer? ")
        self.player = Player(name, 1)

    def play_game(self):

        # Instead of creating four room variables here, you could create a "rooms" dictionary, as shown below. This
        # would let you access any room object by using its index number. For example, "rooms[1]" would give you the
        # Room object for room 1:
        #
        # rooms = {1: Room(room=1, direction1="d", neighbor1=2, direction2="s", neighbor2=3),
        #          2: Room(room=2, direction1="a", neighbor1=1, direction2="s", neighbor2=4),
        #          3: Room(room=3, direction1="w", neighbor1=1, direction2="d", neighbor2=4),
        #          4: Room(room=4, direction1="w", neighbor1=2, direction2="a", neighbor2=3)}
        # current_room = rooms[1]
        room_1 = Room_1()
        room_2 = Room_2()
        room_3 = Room_3()
        room_4 = Room_4()
        room = room_1.room

        game_active = True

        print("Welcome to Adventure, {}!".format(self.player.name))
        print("There are four rooms that you can explore. The rooms a laid out as follows:")
        print("Top Left:    Room 1     Top Right:    Room 2")
        print("Bottom Left: Room 3     Bottom Right: Room 4")
        print("Your adventure starts in room number 1.")
        print("")

        while game_active:
            move = input("Use w, a, s, and d to move. Type q to quit the game.")
            print("")
            if move == "q".lower():
                print("Game over!")
                print("You made {} moves.".format(self.player.moves))
                game_active = False

            # Lastly, you could replace the "elif" conditions in your code below that start with "elif move == ", by
            # using the commented code below one time. This code uses the "rooms" dictionary from the previous comment.
            #
            # elif move.lower() != current_room.direction1 and move.lower() != current_room.direction2:
            #     print("There's nowhere to go! Try a different direction.")
            #     print("")
            # elif move.lower() == current_room.direction1:
            #     current_room = rooms[current_room.neighbor1]
            #     self.player.moves += 1
            #     print(current_room)
            #     print("")
            # elif move.lower() == current_room.direction2:
            #     current_room = rooms[current_room.neighbor2]
            #     self.player.moves += 1
            #     print(current_room)
            #     print("")
            elif move == "w".lower():
                if room == room_1.room or room == room_2.room:
                    print("There's nowhere to go! Try a different direction.")
                    print("")
                elif room == room_3.room:
                    room = room_1.room
                    self.player.moves += 1
                    print(room_1)
                    print("")
                elif room == room_4.room:
                    room = room_2.room
                    self.player.moves += 1
                    print(room_2)
                    print("")

            elif move == "a".lower():
                if room == room_1.room or room == room_3.room:
                    print("There's nowhere to go! Try a different direction.")
                    print("")
                elif room == room_2.room:
                    room = room_1.room
                    self.player.moves += 1
                    print(room_1)
                    print("")
                elif room == room_4.room:
                    room = room_3.room
                    self.player.moves += 1
                    print("")
                    print(room_3)

            elif move == "s".lower():
                if room == room_3.room or room == room_4.room:
                    print("There's nowhere to go! Try a different direction.")
                    print("")
                elif room == room_1.room:
                    room = room_3.room
                    self.player.moves += 1
                    print(room_3)
                    print("")
                elif room == room_2.room:
                    room = room_4.room
                    self.player.moves += 1
                    print(room_4)
                    print("")

            elif move == "d".lower():
                if room == room_2.room or room == room_4.room:
                    print("There's nowhere to go! Try a different direction.")
                    print("")
                elif room == room_1.room:
                    room = room_2.room
                    self.player.moves += 1
                    print(room_2)
                    print("")
                elif room == room_3.room:
                    room = room_4.room
                    self.player.moves += 1
                    print(room_4)
                    print("")

            else:
                print("That's not a valid input.")
                print("")


game = Game()
game.play_game()
