from ..pvpgame import PvpGame


class TreasureWars(PvpGame):
    """Data for Treasure Wars"""
    __slots__ = PvpGame.__slots__ + ("_final_kills", "_treasure_destroyed", "_prestige")

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
        final_kills: int,
        treasure_destroyed: int,
        prestige: int
    ):
        super().__init__(
            name = "wars",
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._final_kills = final_kills
        self._treasure_destroyed = treasure_destroyed
        self._prestige = prestige

    @property
    def final_kills(self) -> int:
        """Number of final kills.

        Returns:
            int: Number of final kills.
        """
        return self._final_kills
    
    @property
    def treasure_destroyed(self) -> int:
        """Number of treasures destroyed.

        Returns:
            int: Number of treasures destroyed.
        """
        return self._treasure_destroyed
    
    @property
    def prestige(self) -> int:
        """Number of prestiges.

        Returns:
            int: Number of prestiges.
        """
        return self._prestige
    
    @property
    def fkdr(self) -> float:
        """The final kills to deaths ratio, rounded to the nearest hundredths. If the player has not died, then the fkdr will be the number of kills.

        Returns:
            float: The final kills to deaths ratio.
        """
        try:
            return round(self.final_kills / self.deaths, 2)
        except:
            return self.final_kills
        
    @property
    def fkpr(self) -> float:
        """The final kills to played games ratio in the gamemode, rounded to the nearest hundredths.

        Returns:
            float: The final kills to played games ratio.
        """
        return round(self.final_kills / self.played, 2)
        
    def getRawLevel(self) -> float:
        return self.getLevel() + self.prestige * 100