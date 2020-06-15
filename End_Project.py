HANGMAN_ASCII_ART = ("""  _    _                                         
         | |  | |                                        
         | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
         |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
         | |  | | (_| | | | | (_| | | | | | | (_| | | | |
         |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                              __/ |                      
                             |___/""")
MAX_TRIES = 6
HANGMAN_PHOTOS = {0: """x-------x
""", 1: \
    ("""x-------x
|
|
|
|
|"""), 2: \
                      (""" x-------x
|        |
|        0
|
|
|"""), 3: \
                      (""" x-------x
|        |
|        0
|        |
|
|"""), 4: \
                      (""" x-------x
|        |
|        0
|       /|\\
|
|"""), 5: \
                      (""" x-------x
|        |
|        0
|       /|\\
|       /
|"""), 6: \
                      (""" x-------x
|        |
|        0
|       /|\\
|       / \\
|""")}
WIN_LOSE_DICT = {True: "WIN", False: "LOSE"}


def choose_word(file_path, index):
    """takes the file from the input and the index number.
        :param file_path: file path on the computer
        :param index: number word in the file_path
        :type file_path: str
        :type index: int
        :return: the word after it is chosen
        :rtype: str
        """
    par_file_path = open(file_path, "r")
    z = par_file_path.read()
    sp_file_path = z.split()
    new_file_path = ""
    for word in sp_file_path:
        if word not in new_file_path:
            new_file_path += word + ', '
    p = new_file_path.split()
    len_word = len(p)
    x = len(sp_file_path)
    y = ((index - 1) % x)
    word_chosen = sp_file_path[y]
    return word_chosen


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """checks if the letter  was chosen is 1 letter and only a letter ana not used.
        :param letter_guessed: the letter guessed in the input
        :param old_letters_guessed: the old letters that were guessed already
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: True if the letter is not in old letters return False if the letter has been chosen
        :rtype: str
        """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print('X')
    z = sorted(old_letters_guessed)
    print("-> ".join(z))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """ when you choose the correct letter show where it is.
        :param secret_word: the secret word from the file
        :param old_letters_guessed: old letters guessed already
        :type secret_word: str
        :type old_letters_guessed: list
        :return: the word with thw new letter
        :rtype: str
        """
    new_letters = ""
    for item in secret_word:
        if item in old_letters_guessed:
            new_letters += item
        else:
            new_letters += '_ '
    return new_letters


def check_right_letter(letter_guessed, secret_word, old_letters_guessed, num_of_tries):
    """check if the letter guessed is in the secret word.
        :param letter_guessed: the letter guessed in the input
        :param secret_word: the secret word from the file
        :param old_letters_guessed: the old letters that already guessed
        :param num_of_tries: number of tries to guess a mistaken letter
        :type letter_guessed: str
        :type secret_word: str
        :type old_letters_guessed: list
        :type num_of_tries: int
        :return right_letter: the right letter in the secret word
        :return num_of_tries: num of tries that the player got the letter mistake
        :rtype right_letter: str
        :rtype num_of_letter: int
        """
    right_letter = letter_guessed in secret_word
    if not right_letter:
        print(":-(")
        num_of_tries += 1
        print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letters_guessed))
    return right_letter, num_of_tries


def check_valid_input(letter_guessed, old_letters_guessed):
    """check if the input is one letter and it is not in the old letters.
        :param letter_guessed: letter in input
        :param old_letters_guessed: old letters that where guessed
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: False if it is not a good letter and True if it is good letter
        :rtype: str
        """
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def check_win(secret_word, old_letters_guessed):
    """checks if number of the old letters are in the secret word .
        :param secret_word: the secret word from the file
        :param old_letters_guessed: old letters guessed
        :type secret_word: str
        :type old_letters_guessed: list
        :return: False if all the letters are not in the secret word
        and True if all thr letters are in the secret word
        :rtype: str
        """
    for item in secret_word:
        if item not in old_letters_guessed:
            return False
    return True


def main():
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)
    # put your path file
    file_path = input('insert file path:').replace("\\", "\\\\")
    # put in the index of the path
    index = int(input("Insert number: "))
    print("let's start")
    print(HANGMAN_PHOTOS[0])
    # print the length of the secret word in lines
    len_word = (len(choose_word(file_path, index)))
    word_in_lines = ("_ " * len_word)
    print(word_in_lines)
    # whats the secret word?
    secret_word = choose_word(file_path, index)
    guesses = False
    old_letters_guessed = []
    good_letters = []
    num_of_tries = 0
    # loops of guessing the letter
    while not guesses and num_of_tries < MAX_TRIES:
        # put in your letter
        letter_guessed = input("Guess a letter:").lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            true_letter, num_of_tries = check_right_letter(
                letter_guessed, secret_word, old_letters_guessed, num_of_tries)
            # if the number of False guesses are more then 6 then loose if not keep going on
            guesses = check_win(secret_word, old_letters_guessed)
    print(WIN_LOSE_DICT[guesses])


if __name__ == "__main__":
    main()

