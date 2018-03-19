#Melody Wang 59907761

'''
Othello game logic
'''

black = 'B'
white = 'W'
none=' '



direction_list = [[-1,-1],[-1,0],[-1,1],
                 [0,-1],        [0,1],
                 [1,-1], [1,0], [1,1]]



#main part
class Othello_game_state:
    def __init__(self,column,row,turn:'B or W',how_to_win):

        self._game_board_column = column
        self._game_board_row = row
        self._game_turn = turn
        self._how_to_win = how_to_win
        self._game_board = []
        for i in range(row):
            self._game_board.append([])
            for i in range(column):
                self._game_board[-1].append(none)


    def reverse_turn(self):
        if self._game_turn == black:
            self._game_turn = white
        elif self._game_turn == white:
            self._game_turn = black
        return self._game_turn


    def opposite_player(self):
        if self._game_turn == black:
            opposite_player = white
        elif self._game_turn == white:
            opposite_player = black
        return opposite_player

        
    def initial_game_state(self, top_left):
        if top_left == black:
            top_right = white
        else:
            top_right = black
        self._game_board[int(self._game_board_row/2)-1][int(self._game_board_column/2)-1]= top_left
        self._game_board[int(self._game_board_row/2)-1][int(self._game_board_column/2)]= top_right
        self._game_board[int(self._game_board_row/2)][int(self._game_board_column/2)]= top_left
        self._game_board[int(self._game_board_row/2)][int(self._game_board_column/2)-1]= top_right


    def print_game_board(self):
        print('B: {}  W: {}'.format(self.black_score(), self.white_score()))
        for row in range(self._game_board_row):
            for col in range(self._game_board_column):
                if self._game_board[row][col] == none:
                    pixel = '.'
                elif self._game_board[row][col] == black:
                    pixel = 'B'
                else:
                    pixel = 'W'
                print(pixel, sep='',end=' ')
            print()
        if self.game_not_over():
            print('TURN: {}'.format(self._game_turn))
        else:
            print('WINNER: {}'.format(self.get_winner()))



    def black_score(self):
        bscore = 0
        for row in range(self._game_board_row):
            for col in range(self._game_board_column):
                if self._game_board[row][col] == black:
                    bscore += 1

        return bscore

    def white_score(self):
        wscore = 0
        for row in range(self._game_board_row):
            for col in range(self._game_board_column):
                if self._game_board[row][col] == white:
                    wscore += 1

        return wscore



    def blank_list(self):
        blank_list = []
        for row in range(self._game_board_row):
            for col in range(self._game_board_column):
                if self._game_board[row][col] == none:
                    blank_list.append([row,col])
        return blank_list


    def valid_move(self, selected_x, selected_y):
        
        if not [selected_x, selected_y] in self.blank_list():
            return False
        
        flip_list = []
        
        for x_dire, y_dire in direction_list:
            x = selected_x
            y = selected_y
            x += x_dire
            y += y_dire
            if self.On_board(x,y):
                if self._game_board[x][y]==self.opposite_player():
                    while self._game_board[x][y]==self.opposite_player():
                        x += x_dire
                        y += y_dire
                        if not self.On_board(x,y):
                            break
                    if not self.On_board(x,y):
                        continue
                    if self._game_board[x][y] == self._game_turn:
                        while True:
                            x -= x_dire
                            y -= y_dire
                            if x == selected_x and y == selected_y:
                                break
                            flip_list.append([x,y])
                            
        
        if len(flip_list) == 0:
            return False

        return flip_list

    def valid_move_list(self):
        valid_move_list = []
        blank_list = self.blank_list()
        for x,y in blank_list:
            if self.valid_move(x, y) != False:
                valid_move_list.append([x,y])
        return valid_move_list


    def On_board(self, x_coord, y_coord):
        if 0 <= x_coord < self._game_board_row and 0 <= y_coord < self._game_board_column:
            return True
        else:
            return False

    def make_move(self, selected_x, selected_y, flip_list):
        self._require_valid_column_number(selected_y)
        self._require_valid_row_number(selected_x)
        self._require_game_not_over()
        
        self._game_board[selected_x][selected_y] = self._game_turn
        for [x,y] in flip_list:
            self._game_board[x][y] = self._game_turn


    def game_not_over(self):
        if len(self.valid_move_list()) == 0:
            return False
        else:
            return True

    def get_winner(self):
        black_score = self.black_score()
        white_score = self.white_score()
        if black_score == white_score:
            winner = 'NONE'
        else:
            if self._how_to_win == '>':
                if black_score > white_score:
                    winner = 'BLACK'
                else:
                    winner = 'WHITE'

            elif self._how_to_win == '<':
                if black_score > white_score:
                    winner = 'WHITE'
                else:
                    winner = 'BLACK'
        return winner


    def _require_valid_column_number(self, column_number):
        if type(column_number) != int or not self._is_valid_column_number(column_number):
            raise ValueError('column_number must be even int between 0 and {}'.format(self._game_board_column - 1))

    def _require_valid_row_number(self, row_number):
        if type(row_number) != int or not self._is_valid_row_number(row_number):
            raise ValueError('row_number must be even int between 0 and {}'.format(self._game_board_row - 1))


    def _require_game_not_over(self) -> None:
        if len(self.valid_move_list()) == 0:
            raise GameOverError()



    def _is_valid_column_number(self, column_number) -> bool:
        return 0 <= column_number < self._game_board_column



    def _is_valid_row_number(self, row_number) -> bool:
        return 0 <= row_number < self._game_board_row



class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass

class InvalidRowOrColumn(Exception):
    '''Raised whenever an invalid row or column is entered'''
    pass

class GameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    pass

