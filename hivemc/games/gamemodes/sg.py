from ..pvpgame import PvpGame


class SurvivalGames(PvpGame):
    """Data for Surival Games"""
    __slots__ = PvpGame.__slots__ + ("_crates", "_deathmatches", "_cows")

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
        deaths: int,
        crates: int,
        deathmatches: int,
        cows: int
    ):
        super().__init__(
            name = "sg",
            UUID = UUID,
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._crates = crates
        self._deathmatches = deathmatches
        self._cows = cows

    @property
    def crates(self) -> int:
        """Number of crates looted.

        Returns:
            int: Number of crates looted.
        """
        return self._crates
    
    @property
    def deathmatches(self) -> int:
        """Number of deathmatches played.

        Returns:
            int: Number of deathmatches played.
        """
        return self._deathmatches
    
    @property
    def cows(self) -> int:
        """Number of cows looted.

        Returns:
            int: Number of cows looted.
        """
        return self._cows