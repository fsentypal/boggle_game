
from BoggleFunctions import BoggleBoardGenerator
from BoggleWordlist import BoggleWordlist


class GameBoard():

    def __init__(self, game_size=4):
        self.edge_length = game_size
        self.board_letters = BoggleBoardGenerator(game_size)

    def __len__(self):

        return self.edge_length

    def __str__(self):
        # create an empty list
        board_str = ""
        # iterate over each row in the list of board letters
        for row in self.board_letters:
            # join the letter with a space and add a new line
            board_str += " ".join(row) + "\n"
        # return the string
        return board_str


class BoggleGame():

    def __init__(self, game_size=4):
        # default board size is 4x4
        self.gameboard = GameBoard(game_size)  # GameBoard object
        self.board_size = game_size
        self.wordlist = BoggleWordlist().words  # all valid words
        self.words_already_used = []  # begin with empty list
        self.score = 0  # score begins at zero

    def compute_word_score(self, word):
        # find the length of the word
        word_length = len(word)
        # determine the score based on the word length
        if word_length == 3 or word_length == 4:
            return 1
        elif word_length == 5:
            return 2
        elif word_length == 6:
            return 3
        elif word_length == 7:
            return 5
        elif word_length >= 8:
            return 11
        # else return 0
        else:
            return 0

    def is_valid_guess(self, word):
        # if the length is less than 3
        if len(word) < 3:
            # return False
            return False
        # if the word isn't the wordlist
        if word.lower() not in self.wordlist:
            # return False
            return False
        # if the word has already been used
        if word in self.words_already_used:
            # return False
            return False
        # for every letter in the word
        for letter in word:
            # assign locations to the letter on the game board
            locations = self.find_letter_on_board(letter)
            # iterate over loc in locations
            for loc in locations:
                # check to see if the word can be made starting from that location and if the word can be found
                if self.check_string_starting_at(word, self.gameboard.board_letters, loc[0], loc[1]):
                    # add it to words_already_used
                    self.words_already_used.append(word)
                    # update the score
                    self.score += len(word)
                    # return True
                    return True
        # if the word can't be played, return False
        return False

    def find_letter_on_board(self, letter):
        # create an empty list
        result = []
        # iterate through each row on the board
        for row in range(len(self.gameboard.board_letters)):
            # iterate through each column on the board
            for col in range(len(self.gameboard.board_letters[0])):
                # if the letter in the current position matches the target letter
                if self.gameboard.board_letters[row][col] == letter:
                    # append the row and column to the result list
                    result.append((row, col))
        # return result list
        return result

    def is_in_bounds(self, row, col):
        # get the number of rows
        num_rows = len(self.gameboard.board_letters)
        # get the number of columns
        num_cols = len(self.gameboard.board_letters[0])
        # check if the position is in the bounds of the game board, if so return
        return 0 <= row < num_rows and 0 <= col < num_cols

    def check_string_starting_at(self, string, board, row, col):
        # if the string is empty (base case)
        if not string:
            # return True
            return True
        # if the current position isn't within the boundaries of the board
        if row < 0 or col < 0 or row >= self.board_size or col >= self.board_size:
            # return False
            return False
        # if the letter at the current position doesn't match the first letter of the string
        if board[row][col] != string[0]:
            # return False
            return False
        # create a copy of the board with the current position marked as visited
        board_copy = [row.copy() for row in board]
        board_copy[row][col] = ""
        # assign adjacent_positions to all adjacent positions to the current position
        adjacent_positions = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0)]
        # iterate over the next row and column in the adjacent_positions list
        for next_row, next_col in adjacent_positions:
            # if the remaining string can be found starting from any of the adjacent positions
            if self.check_string_starting_at(string[1:], board_copy, next_row, next_col):
                # return True
                return True
        # return False if none of these work
        return False

    # Students: there is no need to change anything below here
    def play_game(self):
        print("Game board:\n")
        print(self.gameboard)
        print(f"Current score is: {self.score}")

        guessedword = input("Guess a word: ").upper()
        # guessedword will be upper case since the letters on the board are upper case

        while (guessedword != 'Q'):
            if self.is_valid_guess(guessedword):
                print(f"Correct! You get {self.compute_word_score(guessedword)} points.")
                self.score += self.compute_word_score(guessedword)
                self.words_already_used.append(guessedword.lower())
            print(self.gameboard)
            print(f"Current score: {self.score} Correct words: {self.words_already_used}")
            guessedword = input("Guess a word (type q when finished): ").upper()
        print(f"Done, final score: {self.score}")


if __name__ == '__main__':
    game = BoggleGame()
    game.play_game()