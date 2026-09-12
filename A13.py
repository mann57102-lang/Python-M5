# Class 1
class Japan():

    def capital(self):
        print("Tokyo is the capital of Japan.")

    def language(self):
        print("Japanese is the primary language of Japan.")

    def type(self):
        print("Japan is a developed country.")


# Class 2
class Brazil():

    def capital(self):
        print("Brasilia is the capital of Brazil.")

    def language(self):
        print("Portuguese is the official language of Brazil.")

    def type(self):
        print("Brazil is a developing country.")


# Object Creation
obj_japan = Japan()
obj_brazil = Brazil()


# Common Interface
for country in (obj_japan, obj_brazil):
    country.capital()
    country.language()
    country.type()
