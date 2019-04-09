# coding=utf-8

#Default imports
import os
import sys
import sqlite3


class DBManager(object):
    """
    This class manage all operations over DB
    """


    _sql_create_table = """ CREATE TABLE `games` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            `game_data`	TEXT NOT NULL
                        );"""


    # ========================================
    #               Constructor
    # ========================================

    def __init__(self):
        """
        In the beginning, it is checked if the database exists

        """
        self.db_path = os.path.join(os.getcwd(), "MasterMindGame/db/MasterMindDb.db")

        if not os.path.exists(self.db_path):
            #If the database does not exist, we proceed to create it and create the necessary tables
            self._createTable()

    # ========================================
    #           Private Methods
    # ========================================

    def _connectDB(self):
        return sqlite3.connect(self.db_path)

    def _createTable(self):
        """
        If Local Db was created on runtime
        create tables needed

        :return: None
        """
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(self._sql_create_table)

    # ========================================
    #           Public Methods
    # ========================================

    def InsertData(self,game_data):
        """
        Try to insert data into a DB
        :return:
        """
        sql = '''INSERT INTO games(game_data) VALUES(?)'''
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(sql, (str(game_data),))
        conn.commit()



    def UpdateData(self, id, game_data):
        """Try update data into DB"""
        sql = '''UPDATE games set game_data = ? where id = ?'''
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(sql, (str(game_data),id))
        conn.commit()

    def GetData(self, id):
        """
        Try to get data from DB

        :return:
        """
        sql = '''SELECT game_data from games where id = ?'''
        conn = self._connectDB()
        c = conn.cursor()
        query_result = c.execute(sql, (id,))
        for result in query_result.fetchall():
            return result[0]
        else:
            return None


