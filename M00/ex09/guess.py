import random


def guess(ans, i):
    i += 1
    rep = input("What's your guess between 1 and 99?\n>> ")
    if rep == "exit":
        print("Goodbye!")
        exit()
    if not rep.isdigit():
        print("That's not a number.")
    elif int(rep) > ans:
        print("Too high!")
    elif int(rep) < ans:
        print("Too low!")
    elif int(rep) == ans and i == 1:
        print("The answer to the ultimate question of life,"
              "the universe and everything is 42.\n"
              "Congratulations! You got it on your first try!")
        exit()
    else:
        print("Congratulations, you've got it!\n"
              "You won in "+str(i)+" attempts!")
        exit()
    guess(ans, i)


if __name__ == "__main__":
    ans = random.randint(0, 99)
    print(ans)
    print("This is an interactive guessing game!\n"
          "You have to enter a number between 1 and 99"
          "to find out the secret number.\n"
          "Type 'exit' to end the game.\n"
          "Good luck!")
    guess(ans, 0)
