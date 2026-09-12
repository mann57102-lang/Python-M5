# Class creation
class SecretBox:

    # Private variable
    __secretValue = 45

    # Private method
    def __secretMethod(self):
        print("I'm inside class SecretBox")

    # Function to print value of private variable
    def display(self):
        print("Private Variable value:", SecretBox.__secretValue)


# Object creation and method call
box = SecretBox()

box.display()

box.__secretMethod()
