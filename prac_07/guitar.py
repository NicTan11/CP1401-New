class Guitar:
    """A class to represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        Args:
            name (str): the name of the guitar (default is "").
            year (int): the year the guitar was made (default is 0).
            cost (float): the cost of the guitar (default is 0).
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        """Compare guitars by year."""
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar in years.

        Returns:
            int: The age of the guitar in years.
        """
        from datetime import date
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 or more years old).

        Returns:
            bool: True if the guitar is vintage, False otherwise.
        """
        return self.get_age() >= 50
