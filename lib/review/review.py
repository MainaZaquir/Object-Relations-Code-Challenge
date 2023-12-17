class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self.__class__.reviews.append(self)
        self._customer._reviews.append(self)
        self._restaurant._reviews.append(self)

    @classmethod
    def all(cls):
        return cls.reviews

    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
        return self._restaurant

    @property
    def rating(self):
        return self._rating
