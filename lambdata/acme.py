
class Product():
    def __init__(self, name, price, weight, flammability, identifier):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000,9999999)

    def stealability(self):
        '''
        calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return
        "Not so stealable...",if it is greater or equal to 0.5
        but less than 1.0 return "Kinda stealable.",and otherwise
        return "Very stealable!"
        '''
        ratio_p = self.price / self.weight
        if ratio_p < 0.5:
            return ('Not so stealable...')
            if (0.5 =< ratio_p < 1.0):
                return ('Kinda stealable.')
            else:
                return('Very stealable!')

    def explode(self):
        '''
        calculates the flammability times the weight, and then returns
        a message: if the product is less than 10 return "...fizzle.",
        if it is greater or equal to 10 but less than 50 return
        "...boom!", and otherwise   return "...BABOOM!!"
        '''
        flam_weight = self.flammability * self.weight
        if flam_weight < 10:
            return ('...fizzle')
            if (10 =< flam_weight < 50):
                return ('...boom!')
            else:
                return('...BABOOM!!')


class BoxingGlove(Product):# designates the BoxingGlove class should inherit from the Product class
    def __init__(self, name, price, weight, flammability, identifier):
        # can invoke parent class methods via super()
        super().__init__(name, price, weight, flammability, identifier)
        self.weight = 10

    # can overwrite parent class methods
    def explode(self):
        print('...it' s a glove.')

    def punch(self):
        if self.weight < 5:
            return ('That tickles.')
            if (5 =< self.weight < 15):
                return ('Hey that hurt!')
            else:
                return('OUCH!')


if __name__ == "__main__":

    prod = Product('A Cool Toy')
    prod.stealability()
    prod.explode()

    glove = BoxingGlove('Punchy the Third')
    glove.price
    glove.weight
    glove.punch()
    glove.explode()
