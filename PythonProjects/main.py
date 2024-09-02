import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='9cc7c07d245561f74666e34db31371c9'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_username = {
    "pokemon_id": "66555",
    "name": "Luna",
    "photo_id": 1
}

body_catch = {
    "pokemon_id": "66555"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_username = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_username)
print(response_username.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
