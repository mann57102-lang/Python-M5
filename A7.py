# PART 1: Create the parent class with common family traits
class ParentMember:
    def __init__(self, hair_color, height_cm):
        self.hair_color = hair_color
        self.height_cm = height_cm

    def display_traits(self):
        print("Hair Color:", self.hair_color)
        print("Height (cm):", self.height_cm)


# PART 2: Create the child class that inherits from ParentMember
class Child(ParentMember):

    # PART 3: Give Child its own details along with inherited traits
    def __init__(self, name, age, hair_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(hair_color, height_cm)


    # PART 4: Override display_traits to include child's details
    def display_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().display_traits()


    # PART 5: Add a new method that only Child has
    def favorite_activity(self, activity):
        print(self.name, "enjoys", activity)


# PART 6: Create a Child object with family trait values
child_obj = Child("Arjun", 12, "black", 150)


# PART 7: Call the overridden method and the new method
child_obj.display_traits()
child_obj.favorite_activity("football")


# PART 8: Check whether Child is a subclass of ParentMember
print(
    "Is Child a subclass of ParentMember?",
    issubclass(Child, ParentMember)
)
