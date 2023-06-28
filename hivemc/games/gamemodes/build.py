from ..game import Game


class JustBuild(Game):
    """Data for Just Build"""
    __slots__ = Game.__slots__ + ("_rating_good_received", "_rating_love_received", "_rating_meh_received", "_rating_okay_received", "_rating_great_received")

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
        rating_good_received: int,
        rating_love_received: int,
        rating_meh_received: int,
        rating_okay_received: int,
        rating_great_received: int
    ):
        super().__init__(
            name = "build",
            UUID = UUID,
            monthly = monthly,
            xp = xp,
            played = played,
            victories = victories,
            first_played = first_played,
        )

        self._rating_good_received = rating_good_received
        self._rating_love_received = rating_love_received
        self._rating_meh_received = rating_meh_received
        self._rating_okay_received = rating_okay_received
        self._rating_great_received = rating_great_received

        self.ratings = {
            "good": rating_good_received,
            "love": rating_love_received,
            "meh": rating_meh_received,
            "okay": rating_okay_received,
            "great": rating_great_received
        }

    @property
    def good(self) -> int:
        """Amount of `Good` ratings received.

        Returns:
            int: Amount of `Good` ratings received.
        """
        return self._rating_good_received
    
    @property
    def love(self) -> int:
        """Amount of `Love` ratings received.

        Returns:
            int: Amount of `Love` ratings received.
        """
        return self.rating_love_received
    
    @property
    def meh(self) -> int:
        """Amount of `Meh` ratings received.

        Returns:
            int: Amount of `Meh` ratings received.
        """
        return self.rating_meh_received
    
    @property
    def okay(self) -> int:
        """Amount of `Okay` ratings received.

        Returns:
            int: Amount of `Okay` ratings received.
        """
        return self.rating_okay_received
    
    @property
    def great(self) -> int:
        """Amount of `Great` ratings received.

        Returns:
            int: Amount of `Great` ratings received.
        """
        return self.rating_great_received
    
    def getRating(self, rating: str) -> int:
        """Get the amount of specific rating received.

        Args:
            rating (str): The rating (e.g. Good)

        Returns:
            int: The amount of rating received for that rating.
        """
        return self.ratings.get(rating.lower())