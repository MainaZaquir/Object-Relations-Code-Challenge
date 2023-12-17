from customer import Customer
from restaurant import Restaurant
from review import Review

# Creating instances for testing
customer1 = Customer('Maina', 'Zaquir')
restaurant1 = Restaurant('Aroma Avenue')
review1 = Review(customer1, restaurant1, 5)

# Testing the methods
print(customer1.full_name())          # It should print "Maina Zaquir"
print(restaurant1.customers())        # It should print [<customer.Customer object at 0x...>]
print(review1.restaurant().name())    # It should print "Aroma Avenue"
