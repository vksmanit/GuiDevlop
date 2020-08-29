class Person : 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # __str__ -- magic method
    def __str__(self):
        return (f"Person {self.name} is {self.age} years old")

    def __repr__(self): 
        return (f"Person {self.name} is {self.age} years old")
        



bob = Person("Bob", 35)
print(bob) ## this will print our object -- not easy to read 

# Hence we need to print the object in beautiful manner this can be done using __str__

