class UserInput(object):
    '''
    classdocs
    '''


    def __init__(self, main_window, game):
        '''
        Constructor
        '''
        self.main_window = main_window
        self.game = game
        self.main_window.set_connections(self)
        pass

    def square_clicked(self):
        if self.game.is_over():
            return
        square = self.main_window.sender()
        position = square.get_position()
        color = self.game.active_player_color()
        if self.game.put_piece_at(position):
            self.main_window.put_piece(position, color)
            result = self.game.check_game_end()
            if result == 'end':
                self.main_window.game_over()
                return
            elif result == 'four':
                self.main_window.four_sequence_warning()
            self.main_window.change_player_turn(self.game.get_active_player())
            self.game.ai_player_move()

    def ai_move(self, position):
        sq = self.main_window.get_square(position)
        sq.clicked.emit()

    def new_game(self):
        self.game.new_game()
        self.main_window.clean()
