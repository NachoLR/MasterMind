# coding=utf-8
#!flask/bin/python
from flask import Flask, jsonify
from flask import request


from MasterMindGame.MasterMind import MasterMind

app = Flask(__name__)
master_mind = MasterMind()

@app.route('/MasterMind', methods=['GET'])
def get_game():
    id_game = request.args.get('id')
    return master_mind.GetExistingGame(id_game)


@app.route('/MasterMind', methods=['POST'])
def create_game():
    return master_mind.NewGame()


@app.route('/MasterMind', methods=['PUT'])
def player_move():
    id_game = request.args.get('id')
    move = request.args.getlist('move')
    return master_mind.PlayerMove(id_game,move)



if __name__ == '__main__':
    app.run(debug=True)