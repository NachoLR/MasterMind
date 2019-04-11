from MasterMindGame.MasterMindGameLogic import MasterMindGameLogic
from MasterMindGame.DTOs.GameStatDTO import GameStatDTO

import unittest


class MasterMindLogic_Tests(unittest.TestCase):


    def test_When_Creates_New_GameStatDTO(self):

        game_dto = GameStatDTO()

        self.assertIsInstance(game_dto, GameStatDTO)
        self.assertEquals(len(game_dto.GetKeyPattern()), 4)


    def test_GameStatDTO_data_consistend(self):

        id = 10
        key_pattern = ["red", "yellow", "green", "violet"]
        player_move = ["red", "red", "red", "red"]
        move_result = "XOXX"

        game_dto = GameStatDTO()
        game_dto.SetIdGame(id)
        game_dto.SetKeyPattern(key_pattern)

        game_dto.AddPlayerMove(player_move)
        game_dto.AddMoveResult(move_result)

        game_dto.IncrementAttemps()
        game_dto.IncrementAttemps()
        game_dto.IncrementAttemps()
        game_dto.IncrementAttemps()

        self.assertIsInstance(game_dto, GameStatDTO)
        self.assertEquals(game_dto.id, id)
        self.assertEquals(game_dto.GetKeyPattern(), key_pattern)
        self.assertEquals(game_dto.GetMoveResults(), [move_result])
        self.assertEquals(game_dto.GetAttemps(), 4)
        self.assertFalse(game_dto.GameIsFinished())

        game_dto.FinishGame()

        self.assertTrue(game_dto.GameIsFinished())



if __name__ == '__main__':
    unittest.main()