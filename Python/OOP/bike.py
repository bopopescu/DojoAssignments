class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        return self.price, self.max_speed, self.miles

    def ride(self):
        self.miles += 10
        return self
    
    def reverse(self):
        if (self.miles >= 5):
             self.miles -= 5
        return self


numberOne = Bike(400, "30mph", 0)
numberTwo = Bike(75, "10mph", 0)
numberThree = Bike(225, "25mph", 0)

numberOne.ride().ride().ride().reverse()
print numberOne.displayInfo()

numberTwo.ride().ride().reverse().reverse()
print numberTwo.displayInfo()

numberThree.reverse().reverse().reverse()
print numberThree.displayInfo()

#methods that can return self to allow chaining methods: .ride(), .reverse()