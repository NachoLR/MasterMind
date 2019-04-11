# coding=utf-8
#!flask/bin/python
from flask import Flask
from flask import request


"""
REST API what responses to requests

  Request -->   Request params    -->      Action               --> Response

  GET     -->       1 int id_game         -->    Check if game exists   --> JSON  
                                                and return it if exits  
                                          
  POST    -->        None           -->  Creates new game         --> JSON  
  
  PUT     -->     1 int id_game     -->  Do a player attempt move      --> JSON
                  4 string move  

Move string color supported:
 "green"
 "yellow"
 "red"
 "blue"
 "violet",        
"""


from MasterMindGame.MasterMind import MasterMind

app = Flask(__name__)
master_mind = MasterMind()



@app.route('/MasterMind', methods=['GET'])
def get_game():
    """
    Get an older game if exists through game id provided in previous game.
    Game id is the same id which was created as primary key in DB

    if game not exits return an error into a json
    :return: Json
    """
    id_game = request.args.get('id')
    return master_mind.GetExistingGame(id_game)


@app.route('/MasterMind', methods=['POST'])
def create_game():
    """
    Create new game and return json with a new game stat
    :return: Json
    """
    return master_mind.NewGame()


@app.route('/MasterMind', methods=['PUT'])
def player_move():
    """
    Process a player move and return a json withs new game stat

    :return: Json
    """
    id_game = request.args.get('id')
    move = request.args.getlist('move')
    return master_mind.PlayerMove(id_game, move)



if __name__ == '__main__':
    app.run(debug=True)