# my_lambdata/polos.py

# identity

# attributes/properties


# behaviors/methods

class Polo():
    #Class definition
    def __init__(self, color, size, price, style='Normal Fit'):
    # Defining attributes/properties within the class
    #
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
    # Defining behaviors and methods in the class
    # By default, all the methods inside the class take self
    # as their first parameter. This allows the methods to
    # to reach out to other method and properties that have
    # been defined on the instance
    # Within any method inside the class, we refer to the
    # instance as self ( just as we did in the constructor
    # above)
        print(
            f'Folding the {self.size.upper()} {self.color.upper()} Polo here')

if __name__ == '__main__':
    # This condition is for code that will be run
    # when we execute our file from the command line
    polo = Polo('Blue', 'Large', 99.99)
    print(type(polo))
    print(polo.color, polo.size, polo.price)
    polo.fold()

    polo2 = Polo(color='Yellow', size='Small', price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color='Green', size='Medium',
                 price=69.99, style='Fit Cut')
    print(polo3.color, polo3.size, polo3.price)
    polo3.fold()
