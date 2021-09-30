class TicTacToe:
    
    def __init__(self, end=False, board=list(), iswinner=str, players=list(), crntPlayer=str(), move=None):
        self.board = board
        self.players = players
        self.end = end
        self.iswinner = iswinner
        self.crntPlayer = crntPlayer
        self.move = move
    
    def reset(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.defPlayer()
    
    def defPlayer(self):
        self.players = ['X', 'O']
        self.crntPlayer = input('X or O? ').upper()
        if self.crntPlayer not in self.players:
            print('Please enter X or O')
            self.defPlayer()
    
    def doMoves(self):
        try:
            self.printBoard()
            self.move = input(self.crntPlayer + ', Where do you want to go? (1-9): ')
            if 'end' in self.move:
                exit()
            else:
                if isinstance(int(self.move), int) == False: print ('[ERROR] Please select a number!')
                else:
                    if int(self.move) > 0 and int(self.move) <= 9:
                        if isinstance(self.board[int(self.move) - 1], int):
                            self.board[int(self.move) - 1] = self.crntPlayer
                            self.checkWin()
                            if self.crntPlayer == self.players[0]: self.crntPlayer = self.players[1]
                            else: self.crntPlayer = self.players[0]
                        else:
                            print('Tile has been taken, try another!')
                    else:
                        print('Please select a number on the board!')
        except:
            print('[ERROR] Incorrect input, please try again!')
    
    def checkRow(self, move1, move2, move3):
        moves = [self.board[int(move1) - 1], self.board[int(move2) - 1], self.board[int(move3) - 1]]
        if len(set(moves)) == 1:
            self.iswinner = self.crntPlayer
            return True
    
    def winner(self):
        if isinstance(self.iswinner, str):
            self.printBoard()
            print('Player ' + self.iswinner + ' wins!')
            result = input('Play again? (yes or no): ').lower()
            if result in ['y', 'yes']:
                self.reset()
            else:
                self.end = True
                print('Thanks for playing!')
    
    def checkWin(self):
        win_rows = ['1,2,3', '4,5,6', '7,8,9', '1,4,7', '1,5,9', '2,5,8', '3,6,9', '3,5,6', '7,5,3']
        for i in win_rows:
            x = i.split(',')
            if self.checkRow(int(x[0]), int(x[1]), int(x[2])): self.winner()

    def printBoard(self):
        print('''
                Tic Tac Toe
               -------------
               | %s | %s | %s |
               -------------
               | %s | %s | %s |
               -------------
               | %s | %s | %s |
               -------------
            
            ''' % (self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6], self.board[7], self.board[8]))

game = TicTacToe()
game.reset()
while True:
    if game.end == True:
        break
    game.doMoves()