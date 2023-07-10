from ..game import Game


class AllTimeGame(Game):
    __slots__ = Game.__slots__ + ("_UUID",)
    
    def __init__(
        self,
        *,
        name: str,
        UUID: str,
        xp: int,
        played: int, 
        victories: int,
        first_played: int
    ):
        super().__init__(
            name = name,
            monthly = False,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played    
        )

        self._UUID = UUID

    @property
    def uuid(self) -> str:
        """The Universal Unique Identifier (UUID) of the player.

        Returns:
            str: The UUID of the player.
        """
        return self._UUID
    
    @classmethod
    def from_api(cls, data: dict):
        gathered_data = {h: k for h, k in data.items() if "_" + h in cls.__slots__}
        return cls(
            **gathered_data
        )