import Token
import json
from requests import get

obtain_token = Token.get_token()


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    header = Token.get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"

    query_url = f"{url}?{query}"
    result = get(query_url, headers=header)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None

    return json_result


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = Token.get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


result_clean = search_for_artist(obtain_token, "ACDC")
artist_id = result_clean[0]["id"]
songs = get_songs_by_artist(obtain_token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']} -> Popularity {song['popularity']}")
