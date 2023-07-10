from .pvpgame import AllTimePvpGame


class TheBridge(AllTimePvpGame):
    """Data for The Bridge"""
    __slots__ = AllTimePvpGame.__slots__ + ("_goals",)

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
        goals: int
    ):
        
        super().__init__(
            name = "bridge",
            UUID = UUID,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
            kills = kills,
            deaths = deaths
        )

        self._goals = goals

    @property
    def goals(self) -> int:
        """Number of goals scored by player.

        Returns:
            int: Number of goals scored by player.
        """
        return self._goals
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nGoals: {self.goals}\n"
        )