#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    should generate a given number of products (default 30),
    randomly, and return them as a list
    '''
    products = []

    products = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)

    for i in ADJECTIVES and j in NOUNS

    # TODO - your code! Generate and add random products.
    return products


def inventory_report(products):
    '''
    takes a list of products, and prints a "nice" summary
    '''
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())

- Number of unique product names in the product list
- Average(mean) price, weight, and flammability of listed products
