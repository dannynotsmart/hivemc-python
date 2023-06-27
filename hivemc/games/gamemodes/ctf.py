from ..pvpgame import PvpGame


class CaptureTheFlag(PvpGame):
    """Data for Capture The Flag"""
    __slots__ = PvpGame.__slots__ + ("_assists", "_flags_captured", "_flags_returned")

    def __init__(
        self,
        *,
        UUID: str,
        monthly: bool,
        xp: int,
        played: int, 
        victories: int,
        first_played: int,
        kills: int,
        deaths: int,
        assists: int,
        flags_captured: int,
        flags_returned: int,
    ):
        super().__init__(
            name = "ctf",
            UUID = UUID,
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._assists = assists
        self._flags_captured = flags_captured
        self._flags_returned = flags_returned

    @property
    def assists(self) -> int:
        """Number of assisted kills.

        Returns:
            int: Number of assisted kills.
        """
        return self._assists
    
    @property
    def flags_captured(self) -> int:
        """Number of flags captured by player.

        Returns:
            int: Number of flags captured by player.
        """
        return self._flags_captured
    
    @property
    def flags_returned(self) -> int:
        """Number of flags returned by player.

        Returns:
            int: Number of flags returned by player.
        """
        return self._flags_returned