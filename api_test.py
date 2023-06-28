from hivemc.games import TheBridge
import requests

# The purpose of this file is to ensure that the API works with the data structures.

username = "DqnnyRocko"
game = "bridge"
monthly = False

url = f"https://api.playhive.com/v0/game/{'monthly' if monthly else 'all'}/{game}/{username}"
print(url)
r = requests.get(url)
print(r.json())
bridge = TheBridge.from_api("bridge", monthly, r.json())

print(bridge)