#    1 2 3
#    4   5
#    6 7 8
DIRECTIONS = (((-1, -1), (1, 1)), ((0, -1), (0, 1)),
                ((-1, 0), (1, 0)), ((-1, 1), (1, -1)))
from model.position import Position
class Board(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.pieces = {}  # { Key : value } -> { Position : Piece }
        self.ord_pieces = []
        self.last_piece_played = None

    def inbounds(self, position):
        if (position[0] <= 14 and position[0] >= 0) and (position[1] <= 14 and position[1] >= 0):
            return True
        return False

    def _get_last_move(self):
        return self.last_piece_played

    def get_pieces(self):
        return self.pieces.copy()

    def put_piece(self, piece):
        pos = piece.get_position()
        out_of_bounds = (pos[0] < 0 or pos[0] > 14) or (pos[1] < 0 or pos[1] > 14)
        if pos in self.pieces.keys() or out_of_bounds:
            return False
        self.pieces[pos] = piece
        self.last_piece_played = piece
        self.ord_pieces.append(piece)
        return True

    def get_ord_pieces(self):
        return self.ord_pieces.copy()

    def piece_at(self, position):
        if position in self.pieces.keys():
            return self.pieces[position]
        else:
            return None

    def color_at(self, position):
        aux = self.piece_at(position)
        if aux is not None:
            aux = aux.get_color()
        return aux

    def verify_game_over(self):
        base_pos, color = self.last_piece_played.get_position(), self.last_piece_played.get_color()
        for vector in DIRECTIONS:
            backside, frontside = base_pos, base_pos
            bs_continue, fs_continue = True, True
            total = 1
            for i in range(4):  # @UnusedVariable
                backside += vector[0]
                frontside += vector[1]
                if self.color_at(backside) == color and bs_continue:
                    total += 1
                else:
                    bs_continue = False
                if self.color_at(frontside) == color and fs_continue:
                    total += 1
                else:
                    fs_continue = False
            if total == 4:
                return "four"
            if total >= 5:
                return "end"
        return False
