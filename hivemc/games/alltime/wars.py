from .pvpgame import AllTimePvpGame


class TreasureWars(AllTimePvpGame):
    """Data for Treasure Wars"""
    __slots__ = AllTimePvpGame.__slots__ + ("_final_kills", "_treasure_destroyed", "_prestige")

    def __init__(
        self,
        *,
        UUID: str,
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
            UUID = UUID,
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
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nFinal Kills: {self.final_kills}\n"
            f"FKDR: {self.fkdr}\n"
            f"Treasures Destroyed: {self.treasure_destroyed}\n"
            f"Prestige: {self.prestige}\n"
        )