import Token
import json
from requests import get


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


def get_top_ten_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = Token.get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


def sorted_dictionary_of_songs(songs):
    map_songs = {}

    for idx, song in enumerate(songs):
        map_songs[idx + 1] = (song['popularity'], song['name'] , song['duration_ms'])

    # En algunas ocasiones no trae la lista de forma ordenada.
    sorted_map_songs = {key: value for key, value in sorted(map_songs.items(), key=lambda item: item[1], reverse=True)}

    return sorted_map_songs
