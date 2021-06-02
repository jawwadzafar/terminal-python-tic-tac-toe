from util import clear
class Game(object):
    def __init__(self):
        self.board = ['-', '-', '-','-', '-', '-','-', '-', '-']
        self.game_still_going = True
        self.winner = None
        self.current_player = "X"


    def display_board(self):
        clear()
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])


    def turn(self):
        print(self.current_player + "'s turn.")
        # TODO: improve to show only available turns
        # TODO: handle exception for non int numbers
        position = input("Choose a position from 1 to 9 ")
        valid = False
        while not valid:
            # TODO: use range instead of list
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Incorrect. Choose a position from 1 to 9 again ")

            position = int(position) - 1

            if self.board[position] == "-":
                valid = True
            else:
                print("Choose another position.")

        self.board[position] = self.current_player
        self.display_board()
    
    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_rows(self):
        row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
        row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
        row_3 = self.board[6] == self.board[7] == self.board[8] != "-"
        #If any row has match, flag there's a win
        if row_1 or row_2 or row_3:
            self.game_still_going = False
        #Return the winner (X or O)
        if row_1:
            return self.board[0]
        elif row_2:
            return self.board[3]
        elif row_3:
            return self.board[6]
        return

    def check_columns(self):
        set_1 = self.board[0] == self.board[3] == self.board[6] != "-"
        set_2 = self.board[1] == self.board[4] == self.board[7] != "-"
        set_3 = self.board[2] == self.board[5] == self.board[8] != "-"
        #If any row has match, flag there's a win
        if set_1 or set_2 or set_3:
            self.game_still_going = False
        #Return the winner (X or O)
        if set_1:
            return self.board[0]
        elif set_2:
            return self.board[1]
        elif set_3:
            return self.board[2]
        return

    def check_diagonals(self):
        #Check if any of these diagonals have the same value
        diagonal_1 = self.board[0] == self.board[4] == self.board[8] != "-"
        diagonal_2 = self.board[6] == self.board[4] == self.board[2] != "-"
        #If any diagonal has match, flag there's a win
        if diagonal_1 or diagonal_2 :
            self.game_still_going = False
        #Return the winner (X or O)
        if diagonal_1:
            return self.board[0]
        elif diagonal_2:
            return self.board[6]
        return
    def check_if_tie(self):
        if "-" not in self.board:
            self.game_still_going = False
        return

    def check_game_status(self):
        #check tie
        self.check_if_tie()
        
        #Check rows
        row_winner = self.check_rows()

        #Check columns
        column_winner = self.check_columns()

        #Check diagonals
        diagonal_winner = self.check_diagonals()

        if row_winner:
            self.winner = row_winner
        elif column_winner:
            self.winner = column_winner
        elif diagonal_winner:
            self.winner = diagonal_winner
        else:
            self.winner = None

        return
        
    def run(self):
        print('Welcome to Terminal Tic Tac Toe')
        self.display_board()

        while self.game_still_going:
            self.turn()
            self.change_player()
            self.check_game_status()

        #End of the game
        if self.winner == "X" or self.winner == "O":
            print(self.winner + " won.")
        elif self.winner == None:
            print("Tie. ")

if __name__ == "__main__":
    print('Creating game object...')
    game = Game()
    game.run()