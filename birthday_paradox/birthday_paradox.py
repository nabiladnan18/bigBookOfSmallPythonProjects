import random
import datetime
from datetime import timedelta


def validate_input(user_input) -> int:
    try:
        user_input = int(user_input)
    except ValueError:
        print("Enter a number.")
        return False
    else:
        if user_input > 100 or isinstance(user_input, float):
            print("Enter an integer less than or equal to 100.")
            return False
    return True


def get_birthdays(number_of_birthdays: int) -> list:
    birthdays = []
    start = datetime.date(1990, 1, 1)
    for i in range(1, number_of_birthdays):
        birthdays.append(start + timedelta(random.randint(-(20 * 365), (30 * 365))))
    return birthdays


def readable_birthdays(date: datetime.date) -> str:
    date = date.strftime("%B %d")
    return date


def make_readable(list_of_dates):
    return list(map(lambda x: readable_birthdays(x), list_of_dates))


def matching_birthday(birthdays: list):
    if len(birthdays) == len(set(birthdays)):
        return False
    # Check every birthday with the others to see if they match
    birthdays = sorted(birthdays)
    while birthdays:
        checking = birthdays.pop()
        for day in birthdays:
            if day == checking:
                return checking


def main():
    correct_input = False
    while not correct_input:
        number_of_birthdays = input(
            "How many birthdays shall I generate? (Max 100): \n"
        )
        if not validate_input(number_of_birthdays):
            continue
        else:
            correct_input = True

    number_of_birthdays = int(number_of_birthdays)
    birthdays = make_readable(get_birthdays(number_of_birthdays))

    print(f"Here are {number_of_birthdays} birthdays: \n")
    print(", ".join(birthdays))

    print("In this simulation, ", end="")
    if matching_birthday(birthdays):
        print(f"multiple people have a birthday on {matching_birthday(birthdays)}")
    else:
        print("there are no matching birthdays")

    print(f"Generating {number_of_birthdays} random birthdays 100,000 times...")
    input("Press Enter to begin...")
    print("Let's run another 100,000 simulations")

    matched = 0
    for i in range(1, 100_000):
        birthdays = make_readable(get_birthdays(number_of_birthdays))
        if matching_birthday(birthdays):
            matched += 1
        if i % 10_000 == 0:
            print(f"{i} simulations run.")
    print("100000 simulations run.")

    probability = round(matched / 100_000 * 100, 2)
    print(
        f"""Out of 100,000 simulations of {number_of_birthdays} people, there was a matching birthday in that group {matched} times. This means that {number_of_birthdays} people have a {probability}% chance of having a matching birthday in their group. That's probably more than you think!"""
    )


if __name__ == "__main__":
    main()
