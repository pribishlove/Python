import requests
import json

def get_starship_info(starship_name):
    base_url = "https://swapi.dev/api/"
    starships_url = base_url + "starships/"
    response = requests.get(starships_url, params={"search": starship_name})
    starship_data = response.json()["results"][0]

    pilots_data = []
    for pilot_url in starship_data["pilots"]:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        homeworld_response = requests.get(pilot_data["homeworld"])
        homeworld_data = homeworld_response.json()

        pilot_info = {
            "name": pilot_data["name"],
            "height": pilot_data["height"],
            "mass": pilot_data["mass"],
            "homeworld": homeworld_data["name"],
            "homeworld_url": pilot_data["homeworld"]
        }
        pilots_data.append(pilot_info)

    starship_info = {
        "ship_name": starship_name,
        "max_atmosphering_speed": starship_data["max_atmosphering_speed"],
        "starship_class": starship_data["starship_class"],
        "pilots": pilots_data
    }

    return starship_info

def main():
    starship_name = "X-wing"
    starship_info = get_starship_info(starship_name)
    print(json.dumps(starship_info, indent=2))
    with open(f"{starship_name}_info.json", "w") as json_file:
        json.dump(starship_info, json_file, indent=2)

if __name__ == "__main__":
    main()
