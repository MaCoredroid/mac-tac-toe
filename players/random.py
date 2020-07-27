import random

from engine import MainBoardCoords, SubBoardCoords, SubBoard
from players.stdout import StdOutPlayer


class Random(StdOutPlayer):
    def __init__(self):
        super().__init__()

    def get_my_move(self):  # -> Tuple[MainBoardCoords, SubBoardCoords]
        main_board_coords = self.pick_next_main_board_coords()
        sub_board = self.main_board.get_sub_board(main_board_coords)
        sub_board_coords = self.pick_random_sub_board_coords(sub_board)
        return main_board_coords, sub_board_coords

    def pick_next_main_board_coords(self) -> MainBoardCoords:
        if self.main_board.sub_board_next_player_must_play is None:
            # if self.main_board.is_blank():
            #     return MainBoardCoords(1,1)
            little_board= SubBoard(3)
            for x in range(0, 3):
                for y in range(0,3):
                    sub_board= self.main_board.get_sub_board(MainBoardCoords(x,y))
                    if sub_board.is_finished: 
                        if sub_board.winner== 1:
                            little_board.add_my_move(SubBoardCoords(sub_board.row,sub_board.col))
                        if sub_board.winner== 2:
                            little_board.add_opponent_move(SubBoardCoords(sub_board.row,sub_board.col))
            for main_board_coords in self.main_board.get_playable_coords():
                copy_little_board=little_board
                copy_little_board.add_my_move(main_board_coords)
                if(copy_little_board.is_finished):
                    if self.main_board.get_sub_board(main_board_coords).is_dangerous:
                        return main_board_coords
            for main_board_coords in self.main_board.get_playable_coords():      
                copy_little_board=little_board
                copy_little_board.add_opponent_move(main_board_coords)
                if(copy_little_board.is_finished):
                    if self.main_board.get_sub_board(main_board_coords).is_dangerous:
                        return main_board_coords
            return random.choice(self.main_board.get_playable_coords())
        else:
            return self.main_board.sub_board_next_player_must_play

    @staticmethod
    def pick_random_sub_board_coords(sub_board: SubBoard) -> SubBoardCoords:
        # if sub_board.is_blank():
        #     return SubBoardCoords(1,1)
        for sub_board_coords in sub_board.get_playable_coords():
            copy_board=sub_board
            copy_board=copy_board.add_my_move(sub_board_coords)
            if copy_board.is_finished:
                return sub_board_coords   
        for sub_board_coords in sub_board.get_playable_coords():
            copy_board=sub_board
            copy_board=copy_board.add_opponent_move(sub_board_coords)
            if copy_board.is_finished:
                return sub_board_coords       
        return random.choice(sub_board.get_playable_coords())

    def timeout(self):
        return

    def game_over(self, winLoseTie: str, main_board_coords: MainBoardCoords, sub_board_coords: SubBoardCoords):
        return

    def match_over(self, winLoseTie: str, main_board_coords: MainBoardCoords, sub_board_coords: SubBoardCoords):
        return
