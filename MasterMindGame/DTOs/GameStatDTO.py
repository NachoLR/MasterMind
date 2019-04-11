

class GameStatDTO(object):
    """
    Class GameStatDTO
    This class is a DTO (Data Transfer Object.

    This class is exempt from the logic and operations
    of Set and Get. It's mission is to be used
    as an encapsulation of data


    """

    def __init__(self):
        self.id = None
        self.attempts = 0
        self.key_pattern = []
        self.player_moves = []
        self.is_finished_game = False
        self.move_result = []


    def SetIdGame(self, id):
        self.id = id

    def SetKeyPattern(self, pattern):
        self.key_pattern = pattern

    def GetKeyPattern(self):
        return self.key_pattern

    def IncrementAttemps(self):
        self.attempts += 1

    def GetAttemps(self):
        return self.attempts

    def FinishGame(self):
        self.is_finished_game = True

    def GameIsFinished(self):
        return self.is_finished_game

    def AddPlayerMove(self, player_move):
        self.player_moves.append(player_move)

    def AddMoveResult(self, result):
        self.move_result.append(result)

    def GetMoveResults(self):
        return self.move_result




