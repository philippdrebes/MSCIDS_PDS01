# Task 1
def first_n_squares(number):
    return [x ** 2 for x in range(1, number + 1)]


a = first_n_squares(3)
print(a)
b = first_n_squares(5)
print(b)


def first_n_squares2(number, sort=False):
    res = [x ** 2 for x in range(1, number + 1)]
    res.sort(reverse=sort)
    return res


c = first_n_squares2(5)
print(c)
d = first_n_squares2(5, False)
print(d)
e = first_n_squares2(5, True)
print(e)

# Task 2

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __repr__(self):  # you don't have to modify this method => only for correct printout!
        return self.__class__.__name__.split(".")[-1] + "(" + \
            ', '.join([str(i) for i in vars(self).values()]) + ")"


class CombustionEngineCar(Car):

    def __init__(self, make, model, price, displacement):
        super().__init__(make, model, price)
        self.displacement = displacement


class ElectricCar(Car):
    def __init__(self, make, model, price, battery_capacity):
        super().__init__(make, model, price)
        self.battery_capacity = battery_capacity


c2 = ElectricCar("Tesla", "Model 3", 35000, 75)
print(c2)  # the expected output is: ElectricCar(Tesla, Model 3, 35000, 75)
c3 = CombustionEngineCar("Ford", "Bronco", 40000, 2000)
print(c3)  # the expected output is: CombustionEngineCar(Ford, Bronco, 40000, 2000)
