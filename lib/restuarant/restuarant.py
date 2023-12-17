class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def customers(self):
        return list(set([review.customer for review in self.reviews]))

    def average_star_rating(self):
        return sum([review.rating for review in self.reviews]) / len(self.reviews)
