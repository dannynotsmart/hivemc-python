from ..pvpgame import PvpGame


class MurderMystery(PvpGame):
    """Data for Murder Mystery"""
    __slots__ = PvpGame.__slots__ + ("_coins", "_murders", "_murderer_eliminations", "_uncapped_xp", "_prestige")

    def __init__(
        self,
        *,
        monthly: bool,
        xp: int,
        played: int, 
        victories: int,
        first_played: int,
        kills: int,
        deaths: int,
        coins: int,
        murders: int,
        murderer_eliminations: int,
        uncapped_xp: int,
        prestige: int
    ):
        super().__init__(
            name = "murder",
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._coins = coins
        self._murders = murders
        self._murderer_eliminations = murderer_eliminations
        self._uncapped_xp = uncapped_xp
        self._prestige = prestige

    @property
    def coins(self) -> int:
        """Number of coins collected.

        Returns:
            int: Number of coins collected.
        """
        return self._coins
    
    @property
    def murders(self) -> int:
        """Number of kills as murderer.

        Returns:
            int: Number of kills as murderer.
        """
        return self._murders
    
    @property
    def murderer_eliminations(self) -> int:
        """Number of murderers eliminated by player with a bow.

        Returns:
            int: Number of murderers eliminated by player.
        """
        return self._murderer_eliminations
    
    @property
    def uncapped_xp(self) -> int:
        """Uncapped XP.

        Returns:
            int: Uncapped XP.
        """
        return self._uncapped_xp
    
    @property
    def prestige(self) -> int:
        """Number of prestiges.

        Returns:
            int: Number of prestiges.
        """
        return self._prestige
        
    def getRawLevel(self) -> float:
        return self.getLevel() + self.prestige * 100
    
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
        data["kills"] = data["murders"] + data["murderer_eliminations"]
        return super().from_api(name, monthly, data)