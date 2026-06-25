import requests
import time

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_data(url):
    url = f'{base_url}pokemon/{pokemon_name}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()

        print("retriving data...")

        time.sleep(0.5)
        print('...')
        time.sleep(0.5)
        print('...')
        time.sleep(0.5)
        print('...') 
        time.sleep(0.5)


        print(pokemon_data)       

    else:
        print(f"Failed to retrive data {response.status_code}")

pokemon_name = 'pikachu'
get_pokemon_data(pokemon_name)

