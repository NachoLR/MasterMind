# coding=utf-8

#Default imports
import os
import sys
import json
from DBManager import DBManager
from DTOs.GameStatDTO import GameStatDTO
from Serializers.JsonSerializer import JsonSerializer


class MasterMind(object):

    # ========================================
    #               Constructor
    # ========================================

    def __init__(self):
        self._db = DBManager()


    # ========================================
    #           Public Methods
    # ========================================

    def NewGame(self,move):
        """TODO: Implement new game logic"""
        self._db.InsertData(str(move))
        return "New Game Create"

    def GetExistingGame(self,id_game):
        game_data = self._db.GetData(id_game)
        if game_data is not None:
            return game_data
        else:
            return "Game not found"

    def PlayerMove(self,id, move):

        """TODO:Implement game move"""
        return "Player Move!!!"


    def DumpDataBase(self):
        """TODO: Implement DB delete"""


