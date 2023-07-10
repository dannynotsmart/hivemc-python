from .pvpgame import AllTimePvpGame


class HideAndSeek(AllTimePvpGame):
    """Data for Hide and Seek"""
    __slots__ = AllTimePvpGame.__slots__ + ("_hider_kills", "_seeker_kills")

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
        hider_kills: int,
        seeker_kills: int
    ):
        super().__init__(
            name = "hide",
            UUID = UUID,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._hider_kills = hider_kills
        self._seeker_kills = seeker_kills

    @property
    def hider_kills(self) -> int:
        """Number of seekers killed as a hider.

        Returns:
            int: Number of kills as hider.
        """
        return self._hider_kills
    
    @property
    def seeker_kills(self) -> int:
        """Number of hiders killed as a seeker.

        Returns:
            int: Number of kills as seeker.
        """
        return self._seeker_kills
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nKills as Hider: {self.hider_kills}\n"
            f"Kills as Seeker: {self.seeker_kills}\n"
        )
    
    @classmethod
    def from_api(cls, data: dict):
        """Returns a `Game` instance from the data provided by the API

        Args:
            name (str): The abbreviated name of the gamemode.
            monthly (bool): Whether the data is monthly or all-time.
            data (dict): The raw data provided by the API.

        Returns:
            Game: `Game` instance that holds the data.
        """
        data["kills"] = data["hider_kills"] + data["seeker_kills"]
        return super().from_api(data)