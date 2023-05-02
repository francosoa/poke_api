import json

from flask import Flask, jsonify, request
import requests
from settings.config import get_api, pokedex, request_post, captured_pokemon

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    uri = request.get_json()
    df = get_api(uri)
    return df

@app.route('/pokemon_type/<type>', methods=['GET'])
def get_type(type):

    uri = request.get_json()
    result = get_api(uri)
    pokemon_list = []

    for pokemon in result:
        if pokemon['type_1'] == type or pokemon['type_1'] == type:
            pokemon_list.append(pokemon)
        else:
            pass
    return jsonify(pokemon_list)

@app.route('/pokedex', methods=['GET'])
def show_me_pokemons():
    parameters = request.get_json()
    result = pokedex(parameters)

    return jsonify(result)

@app.route('/captured_pokemon', methods=['POST'])
def post_pokemon(): #pokemon_post
    data = request.get_json()
    endpoint = captured_pokemon(data)

    return endpoint


app.run(port=500, host='localhost')
