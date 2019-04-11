# coding=utf-8

#Default imports
import os
import sys
import json
from DBManager import DBManager
from DTOs.GameStatDTO import GameStatDTO
from Serializers.JsonSerializer import JsonSerializer
from MasterMindGameLogic import MasterMindGameLogic


class MasterMind(object):

    """
    MasterMind Class

    This class works like core which contains operations needed to manage the game.

    """

    # ========================================
    #               Constructor
    # ========================================

    def __init__(self):
        self._db = DBManager()


    # ========================================
    #           Public Methods
    # ========================================

    def NewGame(self):
        """
        Creates new game and return Json with game params
        :return:
        """
        game = MasterMindGameLogic()
        game_result = game.GetGameStats()
        id_new_game = self._db.InsertData(JsonSerializer.SerializeObject(game_result))
        game_result.SetIdGame(int(id_new_game))
        return JsonSerializer.SerializeObject(game_result)


    def GetExistingGame(self, id_game):
        """
        Returns existed game stat

        :param id_game: int
        :return: json string
        """
        game_data = self._db.GetData(int(id_game))
        if game_data is not None:
            return game_data
        else:
            return "{\"ERROR\":\"Provided code game not exits\"}"


    def PlayerMove(self,id_game, move):
        """
        Make a player move and return a Json with updated states

        :param id: int
        :param move: list
        :return:
        """
        game_data = self._db.GetData(int(id_game))

        player_move = []
        for color in move:
            player_move.append(str(color).replace("\"",""))

        game_stat_dto = JsonSerializer.DeserializeJson(game_data.encode('utf-8'), GameStatDTO())
        game = MasterMindGameLogic(game_stat_dto)
        game_stat_dto = game.PlayMove(player_move)

        if game_stat_dto is not None:
            game_stat_dto.id = int(id_game)
            json_response = JsonSerializer.SerializeObject(game_stat_dto)
            self._db.UpdateData(int(id_game), json_response)

            return json_response
        else:
            return "{\"ERROR\":\"Selected color not exits in games\"}"




