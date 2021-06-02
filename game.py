class Game(object):
    def __init__(self):
        self.board = ['-', '-', '-','-', '-', '-','-', '-', '-',]
        self.game_still_going = True
        self.winner = None
        self.current_player = "X"


    def display_board(self):
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
        
    def run(self):
        print('Welcome to Terminal Tic Tac Toe')
        self.display_board()

        while self.game_still_going:
            self.turn()
            self.change_player()

if __name__ == "__main__":
    print('Creating game object...')
    game = Game()
    game.run()