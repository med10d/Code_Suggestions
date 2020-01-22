print("I'm Pythagoras. I can calculate the Hypotenuse of any right trianagle.")

print("Let's get started!")

x = input("What is the length of the first leg?")

y = input("What is the length of the second leg?")

# Nice Code!  Question: What would happen if the user entered something besides a number for one of the legs of the
# triangle? One idea is to add a "try" and "except" like below.  This could handle any non-numeric input.

#try:
    X = float(x)

    Y = float(y)

    def h(X, Y):
        return (X ** 2 + Y ** 2) ** 0.5


    if X > 0 and Y > 0: # Nice check!
        print(h(X, Y))  # Something like "get_hypotenuse" might be more descriptive here.

    else:

        print("Both Legs Must Be > 0)")

#except ValueError:
#   print("Both Legs Must Be Numbers.")
