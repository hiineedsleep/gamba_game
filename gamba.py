import random

emojis = ["🍎", "⚽", "🌞"]


def gamble():
    return [random.choice(emojis) for i in range(3)]


# this makes random rolls

def gameplay():
    balance = 0
    turn = 0
    print(
        "Each missed role means 0.5 euros. If you manage to win in the first 5 rolls, your opponent pays you twice the amount of the cost.")
    while True:  # lets the loop go on forever
        input("Press enter to roll.")
        roll = gamble()
        print(roll)
        turn += 1
        print(f"Turn: {turn}")
        if len(set(
                roll)) == 1:  # this basically helps comp understand if all emojis are the same. "set" helps turn the list into set and removes all duplicates, leaving a singular emoji. if only 1 emoji remains, the length is 1.
            print("You won!")
            turn = 0
            balance = 0
            cont = input("Would you like to continue (yes/no)? ")
            if cont != "yes":
                print("See you next time!")
                break  # breaks the loop
        else:
            balance += 0.5
            print(f"Total cost so far: {balance} Euros")


print(gameplay())
