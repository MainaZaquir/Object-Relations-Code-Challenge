# Object-Relations-Code-Challenge

This is a simple restaurant review system implemented in Python. It consists of three main classes: `Customer`, `Restaurant`, and `Review`.

## Classes

## Customer

The `Customer` class represents a customer who can write reviews for restaurants. Each customer has a given name, a family name, and a list of reviews they've written.

## Restaurant

The `Restaurant` class represents a restaurant that can be reviewed by customers. Each restaurant has a name and a list of reviews it has received.

## Review

The `Review` class represents a review written by a customer for a restaurant. Each review is associated with a customer and a restaurant, and includes a rating.

## Usage

Here's an example of how to use these classes:

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

## Dependancies

The project uses ipdb for debugging. The required Python version is 3.10. You can install the dependencies using pip

## Credits

This application was created by [Maina Zaquir](https://github.com/MainaZaquir).

## Contributing

Contributions are always welcome! If you have any suggestions for improvement or would like to add new features, please feel free to open an issue or submit a pull request. I will look into it immediately.
