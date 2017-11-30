class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.price += self.price * tax
        return self

    def return_reason(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "unopened":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price -= round(self.price * .02,2)
        return self

    def display_info(self):
         return self.price, self.item_name, self.weight, self.brand, self.status
        
item = Product(5, "apple", 1, "whole foods", "for sale")
item.sell().add_tax(.08).return_reason("opened")

print item.display_info()