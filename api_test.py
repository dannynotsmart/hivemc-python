from hivemc import TreasureWars as testclass
import requests

# The purpose of this file is to ensure that the API works with the data structures.
# This is NOT how you are supposed to use this library, this file only exists for testing purposes.

username = "DqnnyRocko"
game = "wars"

url = f"https://api.playhive.com/v0/game/all/{game}/{username}"

r = requests.get(url)

api = testclass.from_api(r.json())

print(api)