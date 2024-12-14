# Connect to an API

# Package manager for API request or else
import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(pokemon_name):
    url = f"{URL}/{pokemon_name}"
    # Object
    response = requests.get(url)
    if response.status_code == 200:
        # Convert into a 'json'
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


def main():
    pokemon_name = input("Enter a pokemon name: ").lower()
    # pokemon_name = "charizard"
    pokemon_info = get_pokemon_info(pokemon_name)


    if pokemon_info:
        print(f"Name: {pokemon_info.get('name').capitalize()}")
        print(f"Id: {pokemon_info.get('id')}")
        print(f"Height: {pokemon_info.get('height')}")
        print(f"Weight: {pokemon_info.get('weight')}")
        print(f"Abilities: {pokemon_info.get('abilities')}")

if __name__ == '__main__':
    main()

