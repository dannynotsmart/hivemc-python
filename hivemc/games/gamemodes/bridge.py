from ..pvpgame import PvpGame

{
  "UUID": "c2805b17-7714-39d4-89ca-9b135ed6df1b",
  "xp": 51284,
  "played": 4,
  "victories": 3,
  "first_played": 1654297120,
  "deaths": 10,
  "goals": 6,
  "kills": 10
}

class TheBridge(PvpGame):
    """Data for The Bridge"""
    __slots__ = PvpGame.__slots__ + ("_goals",)

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
        goals: int
    ):
        
        super().__init__(
            name = "bridge",
            UUID = UUID,
            monthly = monthly,
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
        return super().__str__() + f"\nGoals: {self.goals}\n"