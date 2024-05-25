import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd
import os

api_client_id = ""
api_client_secret = ""


# Set cache path inside class3 directory
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

initial_artist = "3Zyph9kkkEfTKaMQrLotUV"

artist_list = []
def get_related(artist_id):
    response = spotify.artist_related_artists(artist_id)
    return response

result = get_related(initial_artist)

related_list = []

for artist in result["artists"]:
    artist_info = {}
    artist_info["id"] = artist["id"]
    artist_info["source"] = "Ven'nus"
    artist_info["target"] = artist["name"]
    artist_info["genres"] = artist["genres"]

    related_list.append(artist_info)

    result_2 = get_related(artist_info["id"])

    for related_artist in result_2["artists"]:
        related_artist_info = {}
        related_artist_info["id"] = related_artist["id"]
        related_artist_info["source"] = artist_info["target"]
        related_artist_info["target"] = related_artist["name"]
        related_artist_info["genres"] = related_artist["genres"]

        related_list.append(related_artist_info)

tuple_list = []

for item in related_list:
    source = item["source"]
    target = item["target"]
    genres = item["genres"]
    tuple_info = (source, target, genres)
    tuple_list.append(tuple_info)

df = pd.DataFrame(tuple_list, columns=["source", "target", "genres"])

print(df)

df.to_csv("class3/graf_related.csv", sep=",", index=False)
