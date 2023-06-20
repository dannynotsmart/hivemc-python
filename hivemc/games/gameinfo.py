class GameInfo:    
    """Holds information about the gamemodes"""

    __slots__ = (
        "_display_name",
        "_name",
        "_increment",
        "_increment_cap",
        "_max"
    )
    
    def __init__(
        self,
        display_name: str,
        name: str,
        increment: int,
        increment_cap: int,
        max: int
    ):
        self._display_name = display_name
        self._name = name
        self._increment = increment
        self._increment_cap = increment_cap
        self._max = max
        
    @property
    def display_name(self) -> str:
        """The official name of the gamemode (e.g. Capture The Flag)

        Returns:
            str: The official name of the gamemode
        """
        return self._display_name
        
    @property
    def name(self) -> str:
        """The abbreviated name of the gamemode, used in /queue (e.g. ctf)

        Returns:
            str: The abbreviated name of the gamemode
        """
        return self._name
        
    @property
    def increment(self) -> int:
        return self._increment
        
    @property
    def increment_cap(self) -> int:
        return self._increment_cap
        
    @property
    def max(self) -> int:
        """The max level you can be in the gamemode.

        Returns:
            int: The max level you can be in the gamemode.
        """
        return self._max
    
    def __str__(self) -> str:
        return self.display_name