class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        # Initializing the customer attributes
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []  # A list to store the customer's reviews
        Customer.customers.append(self)

    @property
    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.customers

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name == name:
                return customer

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.customers if customer._given_name == name]

    def num_reviews(self):
        return len(self._reviews)
