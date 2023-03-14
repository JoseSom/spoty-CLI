import SpotifyAPI
from Token import get_token
from utils import divisor, welcome, segundos_a_segundos_minutos_y_horas

token_obtained = get_token()


def save_songs_process():
    list_songs = []
    flag = False

    while not flag:
        option = input("Te gustaria añadir canciones a tu playlist? (Y/N)")

        if option == "N" or option == "n":
            flag = True
            continue

        id_select_song = int(input("Ingresa el numero de la cancion: "))
        list_songs.append(id_select_song)

    return list_songs


def mostrar_duracion_playlist(top_ten_songs, list_of_songs):
    playlist = []
    duracion = 0
    for index in list_of_songs:
        if index in top_ten_songs:
            duracion += (top_ten_songs[index][2])
            playlist.append(top_ten_songs[index][1])

    return playlist, segundos_a_segundos_minutos_y_horas(duracion)


def invoke_main_menu(option):
    match option:
        case "0":
            exit(1)
        case "1":
            top_ten_songs = get_top_ten_songs_by_artist()
            divisor()
            list_of_songs = save_songs_process()
            divisor()
            playlist, duracion = mostrar_duracion_playlist(top_ten_songs, list_of_songs)
            print(f"Disfruta tus canciones : {playlist} con una duracion de: {duracion}")
        case _:
            "No es una opcion valida"


def print_dictionary_songs(dictionary_songs):
    for index, value in dictionary_songs.items():
        print(f"{index}.{value[1]} -> Popularity {value[0]}")


def get_top_ten_songs_by_artist():
    artist_name = input("Escribe el nombre del artista \n")
    result = SpotifyAPI.search_for_artist(token_obtained, artist_name)
    artist_id = result[0]["id"]
    songs = SpotifyAPI.get_top_ten_songs_by_artist(token_obtained, artist_id)
    sorted_dictionary_songs = SpotifyAPI.sorted_dictionary_of_songs(songs)

    divisor()
    print_dictionary_songs(sorted_dictionary_songs)
    divisor()

    return sorted_dictionary_songs


welcome()
option_menu = input()
invoke_main_menu(option_menu)
