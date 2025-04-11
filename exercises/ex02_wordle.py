"""My own Wordle game!"""

__author__ = "730568756"


def contains_char(secret: str, char_to_find: str) -> bool:
    """Checks if given chracter is present in word"""
    assert len(char_to_find) == 1, f"len('{char_to_find}') is not 1"

    index = 0
    while index < len(secret):
        if secret[index] == char_to_find:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns emojis representing accuracy of the guess compared to the secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    result = ""
    index = 0

    while index < len(guess):
        if guess[index] == secret[index] and contains_char(secret, guess[index]):
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess with the expected length"""
    guess = input("Enter a " + str(expected_length) + " character word: ")

    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0
    won = False

    while turns < 6 and not won:
        turns += 1
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True

    if won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
