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
        game_data = self._db.GetData(id_game)
        if game_data is not None:
            return JsonSerializer.DeserializeJson(game_data)
        else:
            return "{Game not found}"

    def PlayerMove(self,id, move):
        """TODO:Implement game move"""
        return "Player Move!!!"


    def DumpDataBase(self):
        """TODO: Implement DB delete"""


