from twitchAPI.twitch import Twitch
import json
import time

public = ""
secret = ""

twitch = Twitch(public, secret)
after = None
loop = 0

def get_live_streams(after, loop):
    results = twitch.get_streams(language="es", after=after, first=100)
    print(len(results["data"]))

    with open(f"{loop}.json", 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    try:
        after = results["pagination"]["cursor"]
        print("New page")
        loop += 1
        time.sleep(2)
        get_live_streams(after, loop)
    except KeyError:
        print("end")
        pass

get_live_streams(after, loop)
