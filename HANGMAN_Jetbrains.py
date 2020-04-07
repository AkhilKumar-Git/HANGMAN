import random

word_list = ['python', 'java', 'kotlin', 'javascript']
true_word = random.choice(word_list)
game_word = "-" * len(true_word)       # displaying whole word as hyphens

true_word_list = list(true_word)
game_word_list = list(game_word)
user_typed_list = []

lives = 8
print("H A N G M A N")
wish = input('Type "play" to play the game, "exit" to quit: ')
while wish != "exit":
    while lives != 0:
        print()
        print(game_word)

        if set(game_word_list) == set(true_word_list):
            print("You guessed the word")
            print("You survived!")
            break

        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should print a single letter")

        elif not letter.islower():
            print("It is not an ASCII lowercase letter")

        elif (letter in true_word_list) and (letter not in game_word_list) and (letter not in user_typed_list):     # checking it's occurence
            user_typed_list.append(letter)
            for item in range(len(true_word)):
                if letter == true_word_list[item]:
                    game_word_list[item] = letter   # replacing the input letter into the hyphen string
            game_word = ''.join(game_word_list)

        elif letter not in true_word_list and letter not in user_typed_list:
            user_typed_list.append(letter)
            print("No such letter in the word")
            lives -= 1

        else:
            print("You already typed this letter ")

    else:
        print("You are hanged!")
    wish = input('Type "play" to play the game, "exit" to quit: ')
