# Melody Wang 59907761

import Othello

import tkinter


DEFAULT_FONT = ('Helvetica', 14)




class InitialSettingDialog:
    def __init__(self):

        self._dialog_window = tkinter.Toplevel()


        who_label = tkinter.Label(
            master = self._dialog_window, text = 'Please choose the game setting.',
            font = DEFAULT_FONT)

        who_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_number_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of Rows:',
            font = DEFAULT_FONT)

        row_number_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._StrVar1 = tkinter.StringVar(self._dialog_window, 'select row number')


        self._row_number_menubutton = tkinter.Menubutton(
            self._dialog_window, bg = 'white', activebackground = 'white',
            font = DEFAULT_FONT, textvariable
 = self._StrVar1 )

        self._row_number_menubutton.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        self._row_number_menubutton.menu = tkinter.Menu(self._row_number_menubutton)

        self._row_number_menubutton["menu"] = self._row_number_menubutton.menu

        self._row_number_menubutton.menu.add_command(label='       4 rows      ', font = DEFAULT_FONT, command=self._row4)
        self._row_number_menubutton.menu.add_command(label='       6 rows      ', font = DEFAULT_FONT, command=self._row6)
        self._row_number_menubutton.menu.add_command(label='       8 rows      ', font = DEFAULT_FONT, command=self._row8)
        self._row_number_menubutton.menu.add_command(label='      10 rows      ', font = DEFAULT_FONT, command=self._row10)
        self._row_number_menubutton.menu.add_command(label='      12 rows      ', font = DEFAULT_FONT, command=self._row12)
        self._row_number_menubutton.menu.add_command(label='      14 rows      ', font = DEFAULT_FONT, command=self._row14)
        self._row_number_menubutton.menu.add_command(label='      16 rows      ', font = DEFAULT_FONT, command=self._row16)



        column_number_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of Columns:',
            font = DEFAULT_FONT)

        column_number_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._StrVar2 = tkinter.StringVar(self._dialog_window, 'select column number')


        self._col_number_menubutton = tkinter.Menubutton(
            self._dialog_window, bg = 'white', activebackground = 'white',
            font = DEFAULT_FONT, textvariable
 = self._StrVar2 )

        self._col_number_menubutton.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        self._col_number_menubutton.menu = tkinter.Menu(self._col_number_menubutton)

        self._col_number_menubutton["menu"] = self._col_number_menubutton.menu

        self._col_number_menubutton.menu.add_command(label='       4 columns      ', font = DEFAULT_FONT, command=self._col4)
        self._col_number_menubutton.menu.add_command(label='       6 columns      ', font = DEFAULT_FONT, command=self._col6)
        self._col_number_menubutton.menu.add_command(label='       8 columns      ', font = DEFAULT_FONT, command=self._col8)
        self._col_number_menubutton.menu.add_command(label='      10 columns      ', font = DEFAULT_FONT, command=self._col10)
        self._col_number_menubutton.menu.add_command(label='      12 columns      ', font = DEFAULT_FONT, command=self._col12)
        self._col_number_menubutton.menu.add_command(label='      14 columns      ', font = DEFAULT_FONT, command=self._col14)
        self._col_number_menubutton.menu.add_command(label='      16 columns      ', font = DEFAULT_FONT, command=self._col16)



        move_first_label = tkinter.Label(
            master = self._dialog_window, text = 'Move First:',
            font = DEFAULT_FONT)

        move_first_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._StrVar3 = tkinter.StringVar(self._dialog_window, 'select who will move first')


        self._move_first_menubutton = tkinter.Menubutton(
            self._dialog_window, bg = 'white', activebackground = 'white',
            font = DEFAULT_FONT, textvariable
 = self._StrVar3 )

        self._move_first_menubutton.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        self._move_first_menubutton.menu = tkinter.Menu(self._move_first_menubutton)

        self._move_first_menubutton["menu"] = self._move_first_menubutton.menu

        self._move_first_menubutton.menu.add_command(label='       Black      ', font = DEFAULT_FONT, command=self._blackmovefirst)
        self._move_first_menubutton.menu.add_command(label='       White      ', font = DEFAULT_FONT, command=self._whitemovefirst)



        topleft_label = tkinter.Label(
            master = self._dialog_window, text = 'Top-left Position:',
            font = DEFAULT_FONT)

        topleft_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._StrVar4 = tkinter.StringVar(self._dialog_window, 'select who will be the top-left position')


        self._topleft_menubutton = tkinter.Menubutton(
            self._dialog_window, bg = 'white', activebackground = 'white',
            font = DEFAULT_FONT, textvariable
 = self._StrVar4 )

        self._topleft_menubutton.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        self._topleft_menubutton.menu = tkinter.Menu(self._topleft_menubutton)

        self._topleft_menubutton["menu"] = self._topleft_menubutton.menu

        self._topleft_menubutton.menu.add_command(label='       Black      ', font = DEFAULT_FONT, command=self._blacktopleft)
        self._topleft_menubutton.menu.add_command(label='       White      ', font = DEFAULT_FONT, command=self._whitetopleft)




        how_to_win_label = tkinter.Label(
            master = self._dialog_window, text = 'How the game is won:',
            font = DEFAULT_FONT)

        how_to_win_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._StrVar5 = tkinter.StringVar(self._dialog_window, 'select how the game is won')


        self._how_to_win_menubutton = tkinter.Menubutton(
            self._dialog_window, bg = 'white', activebackground = 'white',
            font = DEFAULT_FONT, textvariable
 = self._StrVar5 )

        self._how_to_win_menubutton.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        self._how_to_win_menubutton.menu = tkinter.Menu(self._how_to_win_menubutton)

        self._how_to_win_menubutton["menu"] = self._how_to_win_menubutton.menu

        self._how_to_win_menubutton.menu.add_command(label='          >         ', font = DEFAULT_FONT, command=self._greater)
        self._how_to_win_menubutton.menu.add_command(label='          <         ', font = DEFAULT_FONT, command=self._less)


        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)


        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False


    def _row4(self):
        self._row_number = 4
        self._StrVar1.set('     4 rows     ')

    def _row6(self):
        self._row_number = 6
        self._StrVar1.set('     6 rows     ')

    def _row8(self):
        self._row_number = 8
        self._StrVar1.set('     8 rows     ')

    def _row10(self):
        self._row_number = 10
        self._StrVar1.set('     10 rows     ')

    def _row12(self):
        self._row_number = 12
        self._StrVar1.set('     12 rows     ')

    def _row14(self):
        self._row_number = 14
        self._StrVar1.set('     14 rows     ')

    def _row16(self):
        self._row_number = 16
        self._StrVar1.set('     16 rows     ')


    def _col4(self):
        self._col_number = 4
        self._StrVar2.set('     4 columns     ')

    def _col6(self):
        self._col_number = 6
        self._StrVar2.set('     6 columns     ')

    def _col8(self):
        self._col_number = 8
        self._StrVar2.set('     8 columns     ')

    def _col10(self):
        self._col_number = 10
        self._StrVar2.set('     10 columns     ')

    def _col12(self):
        self._col_number = 12
        self._StrVar2.set('     12 columns     ')

    def _col14(self):
        self._col_number = 14
        self._StrVar2.set('     14 columns     ')

    def _col16(self):
        self._col_number = 16
        self._StrVar2.set('     16 columns     ')

    def _blackmovefirst(self):
        self._move_first = 'B'
        self._StrVar3.set('Black will move first')

    def _whitemovefirst(self):
        self._move_first = 'W'
        self._StrVar3.set('White will move first')

    def _blacktopleft(self):
        self._topleft = 'B'
        self._StrVar4.set('Black will be the top-left position')

    def _whitetopleft(self):
        self._topleft = 'W'
        self._StrVar4.set('White will be the top-left position')

    def _greater(self):
        self._how_to_win = '>'
        self._StrVar5.set('More discs will win')

    def _less(self):
        self._how_to_win = '<'
        self._StrVar5.set('Less discs will win')

    

    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    def was_ok_clicked(self) -> bool:
        return self._ok_clicked


    def get_game_setting(self) -> 'setting':
        setting = (self._row_number, self._col_number, self._move_first, self._topleft, self._how_to_win)     
        return setting


    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._setting_tuple = self.get_game_setting()
        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()




class OthelloGameBoard:
    def __init__(self, game_state : Othello.Othello_game_state, top_left):
        
        self._top_left = top_left
        self._game_state = game_state
        self._game_state.initial_game_state(top_left)

        self._root_window = tkinter.Tk()


        self._game_state_frame = tkinter.Frame(master = self._root_window,
                                               relief = tkinter.RIDGE, bd = 6)

        self._game_state_frame.grid(
            row = 0, column = 0, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._blackscore = tkinter.StringVar(self._root_window, '0')
        

        blackscore_label = tkinter.Label(
            self._game_state_frame, textvariable = self._blackscore,
            font = ('Helvetica', 25), bg = 'black', fg = 'white', bd = 5)

        blackscore_label.grid(
            row = 0, column = 0, padx = 10, pady = 5,
            sticky = tkinter.W)


        self._currentturn = tkinter.StringVar(self._root_window, '...')

        currentturn_label = tkinter.Label(
            self._game_state_frame, textvariable = self._currentturn,
            font = ('Helvetica', 25), bg = 'yellow', fg = 'black', bd = 5)

        currentturn_label.grid(
            row = 0, column = 1, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        self._whitescore = tkinter.StringVar(self._root_window, '0')

        whitescore_label = tkinter.Label(
            self._game_state_frame, textvariable = self._whitescore,
            font = ('Helvetica', 25), bg = 'white', fg = 'black', bd = 5)

        whitescore_label.grid(
            row = 0, column = 2, padx = 10, pady = 5,
            sticky = tkinter.E)


        self._game_state_frame.rowconfigure(0, weight = 1)
        self._game_state_frame.columnconfigure(0, weight = 1)
        self._game_state_frame.columnconfigure(1, weight = 1)
        self._game_state_frame.columnconfigure(2, weight = 1)


        self._canvas = tkinter.Canvas(
            master = self._root_window, 
            background = '#006000')
        
        self._canvas.grid(
            row = 1, column = 0, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.redraw_game_board()

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)


        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def redraw_game_board(self):

        self._canvas.delete(tkinter.ALL)
        if self._game_state.game_not_over() == False:
            self._currentturn.set('Winner: ' + self._game_state.get_winner()+ '!')
        else:
            if self._game_state._game_turn == 'B':
                self._currentturn.set('Black\'s Turn')
            else:
                self._currentturn.set('White\'s Turn')

        self._blackscore.set(self._game_state.black_score())
        self._whitescore.set(self._game_state.white_score())

        row_num = self._game_state._game_board_row
        column_num = self._game_state._game_board_column

        self._root_window.update()
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        col_width = width/ (column_num +2)
        row_height = height/ (row_num + 2)

        n = 0
        x = 0
        while n != int(row_num + 1):
            self._canvas.create_line(
                    col_width , row_height + n*row_height,
                    col_width + column_num*col_width, row_height + n*row_height,
                    fill = '#050505')
            n += 1

        while x != int(column_num + 1):
            self._canvas.create_line(
                    col_width + x*col_width , row_height,
                    col_width + x*col_width, row_height + row_num*row_height,
                    fill = '#050505')
            x += 1



        self._tuple_to_pixel = dict()

        for x in range(row_num):
            for y in range(column_num):
                self._tuple_to_pixel[(x,y)] = (
                    col_width + y*col_width, row_height + x*row_height,
                    col_width + (y+1)*col_width, row_height + (x+1)*row_height)

        for row in range(row_num):
            for col in range(column_num):
                if self._game_state._game_board[row][col] == 'B':
                    self._canvas.create_oval(
                        self._tuple_to_pixel[(row,col)][0],
                        self._tuple_to_pixel[(row,col)][1],
                        self._tuple_to_pixel[(row,col)][2],
                        self._tuple_to_pixel[(row,col)][3],
                        fill = 'black')
                if self._game_state._game_board[row][col] == 'W':
                    self._canvas.create_oval(
                        self._tuple_to_pixel[(row,col)][0],
                        self._tuple_to_pixel[(row,col)][1],
                        self._tuple_to_pixel[(row,col)][2],
                        self._tuple_to_pixel[(row,col)][3],
                        fill = 'white')
                else:
                    pass


    def _on_canvas_resized(self, event: tkinter.Event):
        self.redraw_game_board()
        self._game_state_frame.rowconfigure(0)
        self._game_state_frame.columnconfigure(0)


    def _on_canvas_clicked(self, event: tkinter.Event):

        row_num = self._game_state._game_board_row
        column_num = self._game_state._game_board_column
        
        self._root_window.update()
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        for row in range(row_num):
            for col in range(column_num):
                if self._tuple_to_pixel[(row,col)][0] <= event.x <= self._tuple_to_pixel[(row,col)][2] and self._tuple_to_pixel[(row,col)][1] <= event.y <= self._tuple_to_pixel[(row,col)][3]:
                    if self._game_state.valid_move(row,col) != False:
                        flip_list = self._game_state.valid_move(row,col)
                        self._game_state.make_move(row,col,flip_list)
                        self._game_state.reverse_turn()
                        self.redraw_game_board()
                    else:
                        pass
                else:
                    pass

        if self._game_state.game_not_over() == False:
            self._currentturn.set('Winner: ' + self._game_state.get_winner()+ '!')
            

    def start(self):
        self._root_window.mainloop()





class OthelloGameApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._game_setting = ()

        self._TopButtonStrVar = tkinter.StringVar(self._root_window, 'Start a New Game')

        
        StartGame_button = tkinter.Button(
            master = self._root_window, textvariable = self._TopButtonStrVar,
            font = DEFAULT_FONT, command = self._get_game_setting)

        StartGame_button.grid(
            row = 0, column = 0, padx = 10, pady = 5,
            sticky = tkinter.S)


    def start(self):
        self._root_window.mainloop()

        

    def _get_game_setting(self) -> None:

        dialog = InitialSettingDialog()
        dialog.show()

        if dialog.was_ok_clicked():
            self._game_setting = dialog.get_game_setting()
            self._TopButtonStrVar.set('Enjoy the Game')
            row, col, first, topleft, win = self._game_setting
            newgame = Othello.Othello_game_state(col,row,first,win)
            OthelloGame = OthelloGameBoard(newgame, topleft)





if __name__ == '__main__':
    OthelloGameApplication().start()

