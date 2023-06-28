from .game import Game


class PvpGame(Game):
    """Represents any PVP gamemode."""
    __slots__ = Game.__slots__ + ("_kills", "_deaths")

    def __init__(
        self,
        *,
        name: str, 
        UUID: str,
        monthly: bool,
        xp: int,
        played: int, 
        victories: int,
        first_played: int,
        kills: int,
        deaths: int
    ):
        super().__init__(
            name = name,
            UUID = UUID,
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played
        )
        
        self._kills = kills
        self._deaths = deaths
    
    @property
    def kills(self) -> int:
        """The number of players killed by the player in the gamemode.

        Returns:
            int: The number of kills.
        """
        return self._kills
        
    @property
    def deaths(self) -> int:
        """The number of deaths in the gamemode.

        Returns:
            int: The number of deaths.
        """
        return self._deaths
        
    @property
    def kdr(self) -> float:
        """The kills to deaths ratio in the gamemode, rounded to the nearest hundredths. If the player has not died, then the kdr will be the number of kills.

        Returns:
            float: The kills to deaths ratio.
        """
        try:
            return round(self.kills / self.deaths, 2)
        except:
            return self.kills
        
    @property
    def kpr(self) -> float:
        """The kills to played games ratio in the gamemode, rounded to the nearest hundredths.

        Returns:
            float: The kills to played games ratio.
        """
        return round(self.kills / self.played, 2)
        
    @property 
    def dpr(self) -> float:
        """The deaths to played games ratio in the gamemode, rounded to the nearest hundredths.

        Returns:
            float: The deaths to played games ratio.
        """
        return round(self.deaths / self.played, 2)
    
    def __str__(self) -> str:
        return super().__str__() + f"\nKills: {self.kills}\nDeaths: {self.deaths}\nKDR: {self.kdr}\n"