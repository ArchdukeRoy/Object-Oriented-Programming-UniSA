"""
Problem Statement
You and your partner will need to make a “guess the word” style game. This game should take
hidden words from a text file which has been provided for you (Resource 1). These words can
later be replaced to a theme of your choice.
The game is simple. Upon starting, a random word should be chosen from the file. You then
take turns guessing until the word is revealed. You have unlimited turns and should keep track
of your turns. Once the game has ended, the word is revealed and how many turns it took to
guess it.
This type of exercise will test your knowledge of opening and closing files, random, lists,
strings, and while loops. You can implement this in any way you like but it should be authentic
to you and your partners level of knowledge. You do not need to implement this with classes
or objects (It is only week 1 for goodness sake). Each function and its responsibilities are listed
below.
"""


def choose_word_list(file_path):
    # opening a txt file and setting it to a variable to be modified
    # splitting the txt file's line into a list (seperated by ', ')
    with open(file_path, "r") as file:
        word_list = file.read()
    word_list = word_list.lower()
    word_list = word_list.split(", ")
    return word_list


def display_word():
    pass


def play_game():
    pass


# pokemon_txt = 'week_1\Workshop\pokemon.txt'
# pokemon_list = choose_words(pokemon_txt)
# print(pokemon_list)

# print(len(pokemon_list))
