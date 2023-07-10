from .pvpgame import AllTimePvpGame


class Deathrun(AllTimePvpGame):
    """Data for Deathrun"""
    __slots__ = AllTimePvpGame.__slots__ + ("_checkpoints", "_activated")

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
        checkpoints: int,
        activated: int
    ):
        super().__init__(
            name = "dr",
            UUID = UUID,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._checkpoints = checkpoints
        self._activated = activated

    @property
    def checkpoints(self) -> int:
        """Number of checkpoints the player has passed through.

        Returns:
            int: Number of checkpoints.
        """
        return self._checkpoints
    
    @property
    def activated(self) -> int:
        """Number of traps activated by the player.

        Returns:
            int: Number of traps activated.
        """
        return self._activated
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCheckpoints Passed: {self.checkpoints}\n"
            f"Traps Activated: {self.activated}\n"
        )