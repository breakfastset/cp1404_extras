
class Dog:

    def __init__(self, name="", age=0, breed=""):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"Dog {self.name} of breed {self.breed} - {self.age} years old."

    def __repr__(self):
        return self.__str__()