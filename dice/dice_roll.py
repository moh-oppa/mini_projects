import random


def dice_roll():
    #loop through the function
    while True:
        roll = input(f"Do you want to roll the dice(y/n): ").lower()
        #state conditions
        if roll == "y":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            result = print({dice1, dice2})

        elif roll == "n":
            result = print("Goodbye")
            return result

        else:
            result = print("Enter a valid option")

    


dice_roll()
