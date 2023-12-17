class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.__class__.reviews.append(self)
        self.customer.reviews.append(self)
        self.restaurant.reviews.append(self)

    @classmethod
    def all(cls):
        return cls.reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
