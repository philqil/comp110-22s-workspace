"""Structured Wordle."""
__author__ = "730529618"

secret = "codes"


def contains_char(word: str, char: str) -> bool:
    """Check if the char is in the word."""
    assert len(char) == 1
    i = 0
    game_over = False
    while not game_over and i < len(word):
        if char == word[i]:
            game_over = True
        else:
            i += 1       
    if game_over:
        return True
    else:
        return False


WHTIE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(secret: str, guess: str) -> str:
    """Emojify the chars."""
    emoji = ""
    assert len(guess) == len(secret)
    i = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else: 
            if contains_char(guess, secret[i]):
                emoji += YELLOW_BOX
            else:
                emoji += WHTIE_BOX
        i += 1
    return emoji


def input_guess(num: int) -> str:
    """Promting the player to make a guess."""
    guess = input(f"Enter a {num} character word: ")
    while len(guess) != num:
        guess = str(input(f"That wasn't {num} chars! Try again: "))
    if len(guess) == num:
        return guess
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    state = 1
    game_over = False
    while not game_over and state < 7:
        print(f"=== Turn {state}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            game_over = True
        else:
            state += 1
    if game_over:
        print(f"You won in {state}/6 turns!")
        game_over = True
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()