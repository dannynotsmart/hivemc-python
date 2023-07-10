from .pvpgame import AllTimePvpGame


class GroundWars(AllTimePvpGame):
    """Data for Ground Wars"""
    __slots__ = AllTimePvpGame.__slots__ + ("_blocks_destroyed", "_blocks_placed", "_projectiles_fired")

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
        blocks_destroyed: int,
        blocks_placed: int,
        projectiles_fired: int,
    ):
        super().__init__(
            name = "ground",
            UUID = UUID,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._blocks_destroyed = blocks_destroyed
        self._blocks_placed = blocks_placed
        self._projectiles_fired = projectiles_fired

    @property
    def blocks_destroyed(self) -> int:
        """Number of blocks destroyed.

        Returns:
            int: Number of blocks destroyed.
        """
        return self._blocks_destroyed
    
    @property
    def blocks_placed(self) -> int:
        """Number of blocks placed.

        Returns:
            int: Number of blocks placed.
        """
        return self._blocks_placed
    
    @property
    def projectiles_fired(self) -> int:
        """Number of eggs thrown by player.

        Returns:
            int: Number of projectiles fired.
        """
        return self._projectiles_fired
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nBlocks Destroyed: {self.blocks_destroyed}\n"
            f"Blocks Placed: {self.blocks_placed}\n"
            f"Projectiles Fired: {self.projectiles_fired}\n"
        )