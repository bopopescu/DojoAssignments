class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        if (self.price > 10000):
            self.tax = .15
        else:
            self.tax = .12
        self.display_all
    
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}mpg".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return ""
    
carOne = Car(10000, 65, "Full", 30)
carTwo = Car(17000, 80, "Not full", 27)
carThree = Car(6000, 45, "Kind of full", 10)
carFour = Car(500, 12, "Full", 40)
carFive = Car(12000, 55, "Not full", 25)
carSix = Car(7500, 70, "Full", 36)

carOne.display_all()
carTwo.display_all()
carThree.display_all()
carFour.display_all()
carFive.display_all()
carSix.display_all()