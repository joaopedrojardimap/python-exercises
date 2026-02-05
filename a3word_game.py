"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['DESK', 'TAB', 'RUN'], 'TO')
    False
    """
    valid = False

    for item in wordlist:
        if item == word:
            valid = True

    return valid
    

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['B', 'C', 'G', 'T'], ['A', 'B', 'C']], 1)
    'ABC'
    """
    str_from_row = ''
    for item in board[row_index]:
        str_from_row += item
    return str_from_row


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'B', 'C'], ['D', 'E', 'F']], 0)
    'AD'
    """
    str_from_column = ''
    for sublist in board:
        str_from_column += sublist[column_index]
    return str_from_column

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['O', 'T', 'A', 'B'], ['P', 'C', 'L', 'G']], 'TAB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'T', 'N', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    True
    """
    for line in board:
        for column_index in range(len(line)):
            if word in make_str_from_column(board, column_index):
                return True
    return False    


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'T', 'N', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    True
    """
    if board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word):
        return True
    return False


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('TAB')
    3
    """
    n = len(word)
    for char in word:
        if n < 3:
            multiplier = 0
        elif 3 <= n <= 6:
            multiplier = 1
        elif 7 <= n <= 9:
            multiplier = 2
        elif n >= 10:
            multiplier = 3
    return n * multiplier

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    
    player_info[-1] += word_score(word)
    

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    num = 0
    for word in words:
        if board_contains_word(board, word):
            num += 1
    return num

def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words_list = []
    for line in words_file:
        words_list.append(line.rstrip('\n'))
    return words_list   

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    board_read = []
    for line in board_file:
        line = line.rstrip('\n')
        row = []
        for char in line:
            row.append(char)
        board_read.append(row)
    return board_read
