from ..game import Game


class BlockDrop(Game):
    """Data for Block Drop"""
    __slots__ = Game.__slots__ + ("_deaths", "_blocks_destroyed", "_powerups_collected", "_vaults_used")

    def __init__(
        self,
        *,
        UUID: str,
        monthly: bool,
        xp: int,
        played: int, 
        victories: int,
        first_played: int,
        deaths: int,
        blocks_destroyed: int,
        powerups_collected: int,
        vaults_used: int
    ):
        super().__init__(
            name = "drop",
            UUID = UUID,
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
        )

        self._deaths = deaths
        self._blocks_destroyed = blocks_destroyed
        self._powerups_collected = powerups_collected
        self._vaults_used = vaults_used

    @property
    def deaths(self) -> int:
        """The number of deaths in the gamemode.

        Returns:
            int: The number of deaths.
        """
        return self._deaths
    
    @property
    def blocks_destroyed(self) -> int:
        """The number of blocks destroyed.

        Returns:
            int: The number of blocks destroyed.
        """
        return self._blocks_destroyed
    
    @property
    def powerups_collected(self) -> int:
        """The number of powerups collected.

        Returns:
            int: The number of powerups collected.
        """
        return self._powerups_collected
    
    @property
    def vaults_used(self) -> int:
        """The number of vaults used.

        Returns:
            int: The number of vaults used.
        """
        return self._vaults_used