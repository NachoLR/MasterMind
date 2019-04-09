# coding=utf-8
#!flask/bin/python
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/MasterMind', methods=['GET'])
def get_game():
    id_game = request.args.get('id')
    return "RETURN NEW GAME " + str(id_game)


@app.route('/MasterMind', methods=['POST'])
def create_game():
    return "NEW GAME"


@app.route('/MasterMind', methods=['PUT'])
def player_move():
    id_game = request.args.get('id')
    move = request.args.getlist('move')
    for i in move:
        print i
    return "NEW MOVEMENT"



if __name__ == '__main__':
    app.run(debug=True)