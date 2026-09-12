# Create class
class Animal:

    # Class attribute
    category = "Mammal"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Animal class
rocky = Animal("Rocky", 6)
luna = Animal("Luna", 4)


# Access the class attributes
print("{} is a {}".format(rocky.name, rocky.category))
print("{} is also a {}".format(luna.name, luna.category))


# Access the instance attributes
print("{} is {} years old".format(rocky.name, rocky.age))
print("{} is {} years old".format(luna.name, luna.age))
