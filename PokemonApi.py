import requests

def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        pokemon_name = data["name"].capitalize()
        pokemon_id = data['id']
        height = data['height']
        weight = data['weight']

        print(f"Pokemon: {pokemon_name} (ID: {pokemon_id})")
        print(f"Height: {height/10} m")
        print(f"Weight: {weight/10} kg")

        print("Stats:")
        for stat in data['stats']:
            stat_name = stat["stat"]["name"]
            stat_value = stat["base_stat"]
            print(f"\t{stat_name}: {stat_value}")

    else:
        print("No pokemon found.")

if __name__ == "__main__":
    get_pokemon("pikachu")