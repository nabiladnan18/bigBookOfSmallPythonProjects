import random

MAX_DIGITS = 3
MAX_GUESSES = 10
GAME_WON_TEXT = "You got it!"


def secret_number() -> int:
    secret_set = {}
    while len(secret_set) != MAX_DIGITS:
        secret = random.randint(100, 999)
        secret_set = set(str(secret))
    return secret


def users_guess(guess_no) -> str:
    guess = input(f"Guess #{guess_no}:\n")
    try:
        guess = int(guess)
    except ValueError:
        print("\nType in an integer.")
    if guess // 100 >= 10:
        print("\nChoose a 3 digit number.")
        return None

    return guess


def get_hint(secret, guess) -> str:
    hint = "Bagels"
    if secret == int(guess):
        return GAME_WON_TEXT
    for index, digit in enumerate(list(str(guess))):
        if digit in str(secret):
            hint = hint.replace("Bagels", "")
            if index == str(secret).find(digit):
                hint += "Fermi "
            else:
                hint += "Pico "
    return hint.rstrip()


def game():
    print(f"""Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {MAX_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: Pico; That means: One digit is correct but in the wrong position.
    When I say: Fermi; That means: One digit is correct and in the right position.
    When I say: Bagels; That means: No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.""")
    user_wants_to_play = True
    while user_wants_to_play:
        secret = secret_number()
        guess_no = 1

        while guess_no <= MAX_GUESSES:
            guess = users_guess(guess_no)
            if guess is None:
                guess_no += 1
                continue

            hint = get_hint(secret, guess)
            print(hint)
            if hint == GAME_WON_TEXT:
                break
            else:
                guess_no += 1
                continue

        user_wants_to_play = input("Do you want to play again? (yes or no): ")
        if user_wants_to_play.lower() == "no":
            user_wants_to_play = False
            print("Thanks for playing!")
            break
        continue
