# hivemc-python
A simple API wrapper for the Minecraft server [The Hive's API](https://api.playhive.com/api/documentation#/).

## Goals/Expected Features of this project
- Provide a simple, object-oriented interface to interact with The Hive's API without needing to manually request anything.
- Handle ratelimiting.
- Provide additional statistics inlcuded such as kill-death ratio, levels, and more.
- Personal Goal: This project will be used in another project. So this project is sort of like a pre-requisite.

## How can I use this?
Currently, the library is not able to be used in software.

## TODO:
- Create `player.py` --> Holds profile data
- Create `leaderboards.py` --> Holds leaderboard data (both monthly and all-time)
- Create `client.py` --> Handles all requests; the user will end up using this.