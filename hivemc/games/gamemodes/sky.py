from ..pvpgame import PvpGame


class Skywars(PvpGame):
    """Data for Skywars"""
    __slots__ = PvpGame.__slots__ + ("_mystery_chests_destroyed", "_ores_mined", "_spells_used")

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
        mystery_chests_destroyed: int,
        ores_mined: int,
        spells_used: int
    ):
        super().__init__(
            name = "sky",
            UUID = UUID,
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._mystery_chests_destroyed = mystery_chests_destroyed
        self._ores_mined = ores_mined
        self._spells_used = spells_used

    @property
    def mystery_chests_destroyed(self) -> int:
        """Number of mystery chests destroyed.

        Returns:
            int: Number of mystery chests destroyed.
        """
        return self._mystery_chests_destroyed
    
    @property
    def ores_mined(self) -> int:
        """Number of ores mined.

        Returns:
            int: Number of ores mined.
        """
        return self._ores_mined
    
    @property
    def spells_used(self) -> int:
        """Number of spells used.

        Returns:
            int: Number of spells used.
        """
        return self._spells_used