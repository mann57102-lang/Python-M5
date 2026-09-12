# Create class
class TextProcessor():

    # Constructor to set default value
    def __init__(self):
        self.text = ""

    # Function to get input from user
    def read_Text(self):
        self.text = input("Enter Text : ")

    # Function to print the text in upper case
    def show_Text(self):
        print("Converted Text is :", self.text.upper())


# Object creation
text_obj = TextProcessor()

# Call functions
text_obj.read_Text()
text_obj.show_Text()
