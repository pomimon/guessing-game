import random

def read_integer(prompt):
    # TODO: Handle parse error
    return int(input(prompt))

def main():
    # tell user you want to play a game
    print("Let's play a guessing game")

    # ask user for range start
    x_int = read_integer("Enter the start of the range: ")

    # ask user for range end
    y_int = read_integer("Enter the end of the range: ")

    # check if range is valid (lower < upper)
    if y_int < x_int:
        print("I will pick the range")
        # reverse numbers to be in proper range
        x_int, y_int = y_int, x_int
        print("The new range is {start} - {end}".format(start=x_int, end=y_int))
    elif x_int == y_int:
        print("I will pick the range")
        y_int += 20
        print("The new range is {start} - {end}".format(start=x_int, end=y_int))
    else:
        print("Your range is {start} - {end}".format(start=x_int, end=y_int))

    # pick random number in range
    my_number = random.randint(x_int, y_int)

    game_over = False

    while not game_over:
        # ask user for guess
        user_int = read_integer("Enter your guess: ")

        if user_int < my_number:
            print("Your guess is too low")
        elif user_int > my_number:
            print("Your guess is too high")
        else:
            print("""
 __________________
< you won the game! >
 ------------------
\\   ^__^
 \\  (oo)\\_______
    (__)\\       )\\/\\
        ||----w |
        ||     ||
            """)
            break

        # check if guess is same as random number
        #     - if too low, tell user 'your guess is too low'
        #     - if too high, tell user 'your guess is too high'
        #     - if user guesses correctly, print ascii cow
        pass

if __name__ == "__main__":
    main()
