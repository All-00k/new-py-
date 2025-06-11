
class Cars:
    def __init__(self):
        print("Default Constructor")

    def __init__(self, Models, Colors):
        self.Models = Models
        self.Colors = Colors
        print("Parameterized Constructor")

    def detail_s(self):
        print("Models", self.Models)
        print("Colors", self.Colors)

    def __del__(self):
        print("Destructor called")

# car1 = Cars() # will show error because of the defined function (detail_s) and default need no attributuion

car2 = Cars("Maruti","Red")
# car1.detail_s()
car2.detail_s()