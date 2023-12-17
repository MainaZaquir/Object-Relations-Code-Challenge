class Restaurant:
    def __init__(self, name):
        # Initializing the restaurant attributes
        self._name = name
        self._reviews = []  # A list to store the restaurant's reviews

    @property
    def customers(self):
        return list(set([review.customer for review in self._reviews]))

    def average_star_rating(self):
        if not self._reviews:
            return 0
        return sum([review.rating for review in self._reviews]) / len(self._reviews)
