

class GameStatDTO(object):



    def __init__(self):
        self.attempts = 0
        self.key_pattern = []
        self.player_moves = []
        self.is_finished_game = False
        self.move_result = []


    def SetKeyPattern(self, pattern):
        self.key_pattern = pattern

    def GetKeyPattern(self):
        return self.key_pattern

    def IncrementAttemps(self):
        self.attempts +=1

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




