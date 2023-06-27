from .gameinfo import GameInfo
from datetime import datetime

import math

    
gamemodes = {
    "wars": GameInfo("Treasure Wars", "wars", 150, 52, 100),
    "dr": GameInfo("Deathrun", "dr", 200, 42, 75),
    "hide": GameInfo("Hide And Seek", "hide", 100, 100, 50),
    "sg": GameInfo("Survival Games", "sc", 150, 150, 30),
    "murder": GameInfo("Murder Mystery", "murder", 100, 82, 100),
    "sky": GameInfo("Skywars", "sky", 150, 52, 75),
    "ctf": GameInfo("Capture The Flag", "ctf", 150, 150, 20),
    "drop": GameInfo("Block Drop", "drop", 150, 22, 25),
    "ground": GameInfo("Ground Wars", "ground", 150, 150, 20),
    "build": GameInfo("Just Build", "build", 100, 100, 20),
    "party": GameInfo("Block Party", "party", 150, 150, 25),
    "bridge": GameInfo("Bridge", "bridge", 0, 0, 20)
}

class Game:
    """Base class for any gamemode. Ideally, `from_api` should always be used in child classes, and this class should not be manually instantiated."""

    __slots__ = (
        "_name",
        "_UUID",
        "_monthly",
        "_xp",
        "_played",
        "_victories",
        "_first_played"
    )
    def __init__(
        self,
        *,
        name: str,
        UUID: str, 
        monthly: bool, # True if data is monthly, False if data is alltime
        xp: int,
        played: int, 
        victories: int,
        first_played: int
    ):
        self._name = name
        self._UUID = UUID
        self._gamemode = gamemodes.get(name)
        self._monthly = monthly
        self._xp = xp
        self._played = played
        self._victories = victories
        self._first_played = first_played
        self._dt_first_played = datetime.from_timestamp(first_played)
        
    @property
    def name(self) -> str:
        """The abbreviated name of the gamemode, used in /queue (e.g. ctf)

        Returns:
            str: The abbreviated name of the gamemode
        """
        return self._name
    
    @property
    def uuid(self) -> str:
        """The Universal Unique Identifier (UUID) of the player.

        Returns:
            str: The UUID of the player.
        """
        
    @property
    def gamemode(self) -> GameInfo:
        """Information about the gamemode

        Returns:
            GameInfo: Holds information about the gamemodes
        """
        return self._gamemode
        
    @property
    def monthly(self) -> bool:
        """Whether the data is monthly or all-time.

        Returns:
            bool: True if monthly, False if all-time.
        """
        return self._monthly
        
    @property
    def xp(self) -> int:
        """The amount of xp in this gamemode.

        Returns:
            int: The amount of xp.
        """
        return self._xp
        
    @property
    def played(self) -> int:
        """The number of played games.

        Returns:
            int: The number of played games.
        """
        return self._played
        
    @property
    def victories(self) -> int:
        """The number of victories.

        Returns:
            int: The number of victories.
        """
        return self._victories
        
    @property
    def first_played(self) -> str:
        """Formal format of the date and time of when the gamemode is first played. (e.g. Saturday, June 10, 2023 | 12:30:00 AM)

        Returns:
            str: Formal format of the date and time of when the gamemode is first played
        """
        return self.dt_first_played.strftime("%A, %B %-m, %Y | %-I:%M:%S %p")
        
    @property
    def dt_first_played(self) -> datetime:
        """Datetime object of when they first played.

        Returns:
            datetime: Datetime object of when they first played.
        """
        return self._dt_first_played
        
    @property
    def abbr_first_played(self) -> str:
        """Abbreviated format of the date and time of when the gamemode is first played, formatted as month/day/year | time (e.g. 06/10/2023 | 00:30:00)

        Returns:
            str: Abbreviated format of the date and time of when the gamemode is first played
        """
        return self.dt_first_played.strftime("%m/%d/%Y | %H:%M:%S")
        
    @property
    def type(self) -> str:
        """Whether data is monthly, or alltime.

        Returns:
            str: "Monthly" if data is monthly, else "All-Time"
        """
        return "Monthly" if self.monthly else "All-Time"
        
    @property
    def losses(self) -> int:
        """The number of losses.

        Returns:
            int: The number of losses.
        """
        return self.played - self.victories
        
    @property
    def wlr(self) -> float:
        """The win lose ratio, rounded to the hundredths. If there are no losses, then it will be 1. 

        Returns:
            float: The win lose ratio.
        """
        try:
            return round(self.victories / self.losses, 2)
        except:
            return 1
    
    def __str__(self) -> str:
        return f"{self.type} Statistics for {self.gamemode}\nFirst Played: {self.first_played}\nXP Gained: {self.xp}\nLevel: {self.getLevel()}\n\nTotal Games Played: {self.played}\nVictories: {self.victories}\nLosses: {self.losses}\nWLR: {self.wlr}\n" 
        
    def getLevel(self) -> float:
        """The approximate lexel the player is in the gamemode.

        Returns:
            float: The approximate level the player is in the gamemode.
        """
        xp = self.xp
        name = self.gamemode.name
        increment = self.gamemode.increment
        increment_cap = self.gamemode.increment_cap
        
        if name == "bridge":
            last_xp = 0
            current_xp = 300
            increment = 300
            additional_increment = 300
            
            i = 2
            while True:
                if xp == current_xp:
                    return i
                    
                elif xp < current_xp:
                    return i + (xp - last_xp) / (current_xp - last_xp) - 1
                
                additional_increment = math.floor(additional_increment * 1.08)
                increment += additional_increment
                last_xp = current_xp
                current_xp += increment
                i += 1
        
        increment = increment / 2
        flatten_level = increment_cap
        
        level = (-increment + math.sqrt(math.pow(increment, 2) - 4 * increment * -xp)) / (2 * increment) + 1
        
        if flatten_level and level > flatten_level:
            level = flatten_level + (xp - (increment * math.pow(flatten_level - 1, 2) + (flatten_level - 1) * increment)) / ((flatten_level - 1) * increment * 2)
        
        return level
    
    @classmethod
    def from_api(cls, name: str, monthly: bool, data: dict):
        """Returns a `Game` instance from the data provided by the API

        Args:
            name (str): The abbreviated name of the gamemode.
            monthly (bool): Whether the data is monthly or all-time.
            data (dict): The raw data provided by the API.

        Returns:
            Game: `Game` instance that holds the data.
        """
        gathered_data = {h: k for h, k in data.items() if "_" + h in cls.__slots__}
        return cls(
            name = name, 
            monthly = monthly,
            **gathered_data
        )