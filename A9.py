class Laptop:

    def __init__(self):
        self.__maxprice = 75000

    def display_price(self):
        print("Selling Price: {}".format(self.__maxprice))

    def update_price(self, price):
        self.__maxprice = price


laptop = Laptop()

laptop.display_price()

# Try to change the price directly
laptop.__maxprice = 80000
laptop.display_price()

# Change the price using setter function
laptop.update_price(80000)
laptop.display_price()
