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
        game_result.SetIdGame(id_new_game)
        return JsonSerializer.SerializeObject(game_result)

    def GetExistingGame(self, id_game):
        """
        Returns existed game stat

        :param id_game: int
        :return: json string
        """
        game_data = self._db.GetData(id_game)
        if game_data is not None:
            return JsonSerializer.DeserializeJson(game_data)
        else:
            return "{Game not found}"

    def PlayerMove(self,id, move):
        """
        Make a player move and return a Json with updated states

        :param id: int
        :param move: list
        :return:
        """
        """TODO:Implement game move"""
        return "Player Move!!!"




