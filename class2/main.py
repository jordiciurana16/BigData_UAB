import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

initial_artist = "3Zyph9kkkEfTKaMQrLotUV"

related = spotify.artist_related_artists(initial_artist)

artists = related["artists"]

# create list before the FOR loop

artist_list = []
i = 0
for a in artists:
    i += 1

    name = a["name"]
    followers = a["followers"]["total"]
    link = a["external_urls"]["spotify"]
    artist_id = a["id"]
    popularity = a["popularity"]

    frame = pd.DataFrame({
        "seed": initial_artist,
        "name": name,
        "followers": followers,
        "link": link,
        "id": artist_id,
        "popularity": popularity,
    }, index=[i])
    artist_list.append(frame)

    related_2 = spotify.artist_related_artists(artist_id)
    artists_2 = related_2["artists"]

    for a_2 in artists_2:
        i += 1
        name = a_2["name"]
        followers = a_2["followers"]["total"]
        link = a_2["external_urls"]["spotify"]
        id_2 = a_2["id"]
        popularity = a_2["popularity"]

        frame = pd.DataFrame({
            "seed": artist_id,
            "name": name,
            "followers": followers,
            "link": link,
            "id": id_2,
            "popularity": popularity,
        }, index=[i])
        artist_list.append(frame)

# Save the JSON file in the class2 directory
with open('class2/data.json', 'w', encoding='utf-8') as f:
    json.dump(related, f, indent=4)

# Save the Excel file in the class2 directory
final = pd.concat(artist_list)
print(final)

final.to_excel("class2/dataset.xlsx")
