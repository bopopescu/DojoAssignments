class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health += 1
        return self

    def display_health(self):
        return self.health

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Rocky", 150)
    
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("Drogon", 170)
        #'super(ChildClassName, self).parent_method()'.  
        super(Dragon, self).display_health()
        print "I am a Dragon"
    
    def fly(self):
        self.health -= 10
        return self


animal_one = Animal("Tom", 100)
animal_one.walk().walk().walk().run().run()

print animal_one.display_health()

dog_one = Dog()
dog_one.walk().walk().run().run().pet()

print dog_one.display_health()

dragon_one = Dragon()
dragon_one.fly().fly().fly().walk()

print dragon_one.display_health()

animal_two = Animal("Lee", 100)
#animal_two.pet().fly()

print animal_two.display_health()