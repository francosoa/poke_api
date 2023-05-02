import json
import requests
import logging
import pandas as pd



def get_api(parameters):

    uri = parameters[0]['endpoint']
    endpoint = f'https://pokemonapi.franciscovaldec.repl.co/{uri}'
    response = requests.get(endpoint)

    if response.status_code == 200:
        response_json = response.json()
    elif response.status_code == 400:
        response_json = response.status_code
    elif response.status_code == 500:
        response_json= response.status_code
    else:
        response_json = response.status_code

    return response_json

def request_post(parameters):
    uri = parameters[0]['endpoint']
    endpoint = f'https://pokemonapi.franciscovaldec.repl.co/{uri}'

    return endpoint

def captured_pokemon(parameters):
    endpoint = request_post(parameters)
    pokemons = parameters[1]["captured_pokemon"]

    for info in pokemons:
        response = requests.post(endpoint, json=info)
        response = response.json()

    return response


def pokedex(parameters):

    data = requests_api(parameters)
    pokemon_type = parameters[1]['type']
    pokemon_total = parameters[1]['total']

    pokedex = []
    for pokemon in data:
       if pokemon['total'] >= pokemon_total:
            pokedex.append(pokemon)

    else:
        pass

    return pokedex

