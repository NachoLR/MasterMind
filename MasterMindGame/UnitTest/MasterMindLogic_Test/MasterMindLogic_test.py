from MasterMindGame.MasterMindGameLogic import MasterMindGameLogic
from MasterMindGame.DTOs.GameStatDTO import GameStatDTO

import unittest


class MasterMindLogic_Tests(unittest.TestCase):


    def test_When_Creates_New_Game_With_new_pattern_and_creates_newGameStatDTO(self):
        game = MasterMindGameLogic()
        game_dto = game.GetGameStats()

        self.assertIsInstance(game,MasterMindGameLogic)
        self.assertIsInstance(game_dto,GameStatDTO)
        self.assertEquals(len(game_dto.GetKeyPattern()), 4)


    def test_When_Creates_New_Game_With_with_existing_GameStatDTO(self):

        game_dto = self._createGameStatDTO()
        game = MasterMindGameLogic(game_dto)
        game_dto_processed = game.GetGameStats()

        self.assertIsInstance(game, MasterMindGameLogic)
        self.assertIsInstance(game_dto_processed, GameStatDTO)
        self.assertEquals(game_dto, game_dto_processed)
        self.assertEquals(game_dto.GetKeyPattern(), game_dto_processed.GetKeyPattern())
        self.assertEquals(len(game_dto.GetMoveResults()), 2)
        self.assertFalse(game_dto.GameIsFinished())


    def test_When_player_do_a_move(self):

        player_move = ["red"," yellow", "blue","green"]
        result_move = "XO"
        game = MasterMindGameLogic(self._createGameStatDTO())
        game_dto = game.PlayMove(player_move)

        self.assertEquals(result_move, game_dto.GetMoveResults()[2])
        self.assertEquals(3, int(game_dto.GetAttemps()))
        self.assertIn(result_move, game_dto.player_moves)
        self.assertEquals(3, len(game_dto.player_moves))



    def _createGameStatDTO(self):

        id = 10
        attempts = 2
        key_pattern = ["red", "yellow", "green", "violet"]
        player_move_1 =["red","red","red","red"]
        player_move_2 =["red","blue","green","yellow"]
        is_finished_game = False
        move_result_1 = "XOX"
        move_result_2 = "XOXX"

        game_dto = GameStatDTO()
        game_dto.SetIdGame(id)
        game_dto.SetKeyPattern(key_pattern)

        game_dto.AddPlayerMove(player_move_1)
        game_dto.AddPlayerMove(player_move_2)
        game_dto.AddMoveResult(move_result_1)
        game_dto.AddMoveResult(move_result_2)

        return  game_dto





if __name__ == '__main__':
    unittest.main()