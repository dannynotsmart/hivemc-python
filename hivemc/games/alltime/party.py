from .game import AllTimeGame


class BlockParty(AllTimeGame):
    """Data for Block Party"""
    __slots__ = AllTimeGame.__slots__ + ("_powerups_collected", "_rounds_survived")

    def __init__(
        self,
        *,
        UUID: str,
        xp: int,
        played: int, 
        victories: int,
        first_played: int,
        powerups_collected: int,
        rounds_survived: int
    ):
        super().__init__(
            name = "party",
            UUID = UUID,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
        )

        self._powerups_collected = powerups_collected
        self._rounds_survived = rounds_survived

    @property
    def powerups_collected(self) -> int:
        """The number of powerups collected.

        Returns:
            int: The number of powerups collected.
        """
        return self._powerups_collected
    
    @property
    def rounds_survived(self) -> int:
        """The number of rounds survived.

        Returns:
            int: The number of rounds survived.
        """
        return self._rounds_survived
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nPowerups Collected: {self.powerups_collected}\n"
            f"Rounds Survived: {self.rounds_survived}\n"
        )