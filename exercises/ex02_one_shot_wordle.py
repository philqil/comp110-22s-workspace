"""EX02 - One shot wordle."""
__author__ = "730529618"

word = "python"
guess = input(f"What is your {len(word)}-letter guess? ")

WHTIE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji = ""
index = 0

while len(guess) != len(word):
    guess = input(f"That was not {len(word)} letters! Try again: ")
while index < len(word):  
    if guess[index] == word[index]:
        emoji = emoji + GREEN_BOX
    else:
        index_2 = 0
        game_over = False
        while not game_over and index_2 < len(word):
            if word[index] == guess[index_2]:
                game_over = True
            else:
                index_2 += 1
        if game_over:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHTIE_BOX   
    index = index + 1
print(emoji)
if guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")