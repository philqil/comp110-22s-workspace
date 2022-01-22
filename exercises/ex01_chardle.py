"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730529618"

word: str = str(input("Enter a 5-character word: "))

if len(word) != 5:
    print('Error: Word must contain 5 characters')
    exit()
else:
    character_guess: str = str(input("Enter a single character: "))
    if len(character_guess) != 1:
        print('Error: Character must be a single character.')
        exit()
    else:
        print("Searching for " + str(character_guess) + " in " + word)
        count = 0
        if len(word) == 5:
            if character_guess == word[0]:
                print(character_guess + " found at index 0")
                count = count + 1
            if character_guess == word[1]:
                print(character_guess + " found at index 1")
                count = count + 1
            if character_guess == word[2]:
                print(character_guess + " found at index 2")
                count = count + 1
            if character_guess == word[3]:
                print(character_guess + " found at index 3")
                count = count + 1
            if character_guess == word[4]:
                print(character_guess + " found at index 4")
                count = count + 1
        else:
            print('Word must contain 5 characters')

        if count == 1:
            print('1 instance of ' + character_guess + ' found in ' + word)
        if count == 2:
            print('2 instances of ' + character_guess + ' found in ' + word)
        if count == 3:
            print('3 instances of ' + character_guess + ' found in ' + word)
        if count == 4:
            print('4 instances of ' + character_guess + ' found in ' + word)
        if count == 5:
            print('5 instancess of ' + character_guess + ' found in ' + word)
        if count == 0:
            print('No instances of ' + character_guess + ' found in ' + word)