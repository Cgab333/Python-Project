from random import randint
def choose_word(file_path, index):
    """
       choosing a word from a txt file.
       the index is calling the word the player will try to guess
       :param file_path: the path to the file
       :param index: the number used to chose the word
       :type index: int
       :type file_path: str
       :return:str word for the game
       """
    file = open ( file_path, "r" )
    cd_data = file.read ( )

    cd_items = cd_data.split ( " " )
    cd_items1 = []
    for i in cd_items:
        if i in cd_items1:
            continue
        else:
            cd_items1.append(i)
    lengh=len(cd_items1)
    return (len(cd_items1),cd_items[index-1])

def print_hangman(num_of_tries):
    """
    showing the status of the hangman
    :param num_of_tries: the number showing what is the status of the hangman
    :type num_of_tries: int
    :return: str picture of the hangman
    """
    photo_dict = {1: """
        x-------x
        """, 2: """
        x-------x
        |
        |
        |
        |
        |
         """, 3: """
        x-------x
        |       |
        |       0
        |
        |
        |
        """, 4:  """
        x-------x
        |       |
        |       0
        |       |
        |
        |
    """, 5: """
        x-------x
        |       |
        |       0
        |      /|\ 
        |
    """, 6: """
        x-------x
        |       |
        |       0
        |      /|\ 
        |      / \ 
        |
        """}
    return photo_dict[num_of_tries]

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    checks if the letter is valid and if he already used the same latter
    :param letter_guessed: the letter the player trying
    :param old_letter_guessed: the list of letters the player try
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return:true/false
    """
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(letter_guessed) > 1 or (letter_guessed not in abc) or letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def check_win(secret_word, old_letters_guessed):
    """
    check if the player won the game
    :param secret_word: str
    :param old_letters_guessed:list
    :type secret_word: the secret word of the game
    :type old_letters_guessed: the list of letters the player try
    :return: True/False
    """
    score = 0
    for i in secret_word:
        if i not in old_letters_guessed:
            score += 1
    return score == 0




def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, num_of_tries):
    """
    using check valid input func to check the letter value, if she is'nt it replies: "X".
    if she is valued its adding the latter to the old letters list.
    now she check if the letter is in the secret word.
    if she is'nt she replies: ":(" and adding to the numbers of tries anther try.
    :param letter_guessed: the letter the player trying
    :param old_letters_guessed: the list of letters the player try
    :param secret_word: the secret word of the game
    :param num_of_tries: the number showing what is the status of the hangman
    :type letter_guessed: str
    :type old_letters_guessed: list
    :type secret_word: str
    :type num_of_tries: int
    :return: the number of tries the player used
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        if letter_guessed not in secret_word:
            print(" :( ")
            num_of_tries = num_of_tries + 1
    else:
        print("X")
    return num_of_tries



def show_hidden_word(old_letters_guessed, secret_word):
    """
    shows the letters index the player needs to guess and how many left
    :param old_letters_guessed: the list of letters the player try
    :param secret_word: the secret word of the game
    :type old_letters_guessed: list
    :type secret_word: str
    :return: str the hidden word
    """
    hidden_word = secret_word
    for i in secret_word:
        if i in old_letters_guessed:
            continue
        elif i not in old_letters_guessed:
            hidden_word = hidden_word.replace(i, "_")
    hidden_word = " ".join(hidden_word)
    return hidden_word

# no need because you want this project in one file
# def main():
#     check_win()
#     choose_word()
#     print_hangman()
#     show_hidden_word()
#     check_valid_input()
#     try_update_letter_guessed()
#
# if __name__ == "__main__":
#     main()

HANGMAN_ASCII_ART = """" _    _                                           
 | |  | |                                           
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_  \   
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |  
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     
                      __/ |                         
                     |___/"""""
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, """
You have only""", MAX_TRIES, "tries")
# printing the opening sing of the game

file_path = input("Enter file path: ")
index = int(input("Enter index: "))
# asking for the file location and number, in order to chose a word for the game

secret_word_tuple = choose_word(file_path, index)
secret_word = secret_word_tuple[1]
hidden_word = show_hidden_word([], secret_word)
num_of_tries = 1
# changing the word to be hidden

print("Let's start!", print_hangman(num_of_tries))
print(hidden_word)
# printing the hangman and the hidden word

old_letters_guessed = []
while True:
    win = check_win(secret_word, old_letters_guessed)
    if win == True:
        print("WIN")
        break
# checking if you won the game

    else:
        letter_to_guessed = (input("Guess a letter: ")).lower()
        num_of_tries = try_update_letter_guessed(letter_to_guessed, old_letters_guessed, secret_word, num_of_tries)
        print(print_hangman(num_of_tries))
        print("the letters you tried: ", old_letters_guessed)
        hidden_word = show_hidden_word(old_letters_guessed, secret_word)
        print(hidden_word)
        # asking for a letter from the player and then checking if she is valid or not, if she is its checking if its in
        # the secret word and return the new hidden word and the status of the hangman.

        if num_of_tries == MAX_TRIES:
            print("Lose")
            break
            # checking if you lose the game
