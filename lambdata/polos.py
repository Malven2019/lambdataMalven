# my_lambdata/polos.py

# identity

# attributes/properties


# behaviors/methods

class Polo():
    def __init__(self, color, size, price, style='Normal Fit'):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
        print(
            f'Folding the {self.size.upper()} {self.color.upper()} Polo here')

        if __name__ == '__main__':

            polo = Polo('Blue', 'Large', 99.99)
            print(type(polo))
            print(polo.color, polo.size, polo.price)
            polo.fold()

            polo2 = Polo(color='Yellow', size='Large', price=69.99)
            print(polo.color, polo.size, polo.price)
            polo2.fold()

            polo3 = Polo(color='Green', size='Medium',
                         price=69.99, style='Fit Cut')
            print(polo.color, polo.size, polo.price)
            polo3.fold()
