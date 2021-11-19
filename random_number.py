import random


def guess(x):
    random_num = random.randint(1, x)
    your_guess = 0
    while your_guess != random_num:
        your_guess = int(input("Guess a number between 1 and " + str(x) + ": "))
        if your_guess < random_num:
            print("Go higher")
        elif your_guess > random_num:
            print("Your guess is too high, try lower")
    print("You guessed it right!")


# guess(10)


def computer_guess(x):
    low = 1
    high = x
    response = ''

    while response != 'c':
        computers_guess = random.randint(low, high)
        print("Computer's guess is: " + str(computers_guess))
        response = input("What's your response - h, l or c: ")
        if response == 'h':
            high = computers_guess - 1
        elif response == 'l':
            low = computers_guess + 1
    print("Computer guessed correctly!")


computer_guess(500)
