# game_metadata_parser.py

import requests
import pandas as pd

API_KEY = "98b2e16a50fb4ee6a9e2d80af3382471"
BASE_URL = "https://api.rawg.io/api/games"

def fetch_games(page=1, page_size=20):
    params = {
        "key": API_KEY,
        "page_size": page_size,
        "page": page
    }
    response = requests.get(BASE_URL, params=params)
    return response.json().get("results", [])

def parse_game_data(games):
    data = []
    for game in games:
        data.append({
            "Name": game.get("name"),
            "Released": game.get("released"),
            "Rating": game.get("rating"),
            "Genres": ", ".join([g['name'] for g in game.get("genres", [])]),
            "Platforms": ", ".join([p['platform']['name'] for p in game.get("platforms", [])]),
            "Tags": ", ".join([t['name'] for t in game.get("tags", [])])
        })
    return pd.DataFrame(data)

def main():
    all_games = []
    for page in range(1, 4):  # Get data from first 3 pages
        games = fetch_games(page=page, page_size=20)
        all_games.extend(games)

    df = parse_game_data(all_games)
    df.to_csv("game_metadata.csv", index=False)
    print("Saved game metadata to game_metadata.csv")

if __name__ == "__main__":
    main()
