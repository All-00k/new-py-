class Apple_design:
    count = 0
    def __init__(self, cpu, ram):  #constructer
        self.cpu = cpu
        self.ram = ram


    def mobile(self):
        print(type(self))
        print("this apple phhone1")
        print(self.cpu, self.ram)


# create a object
m1 = Apple_design(3.5, 8)
m2 = Apple_design(4.5, 16)
m1.mobile()
m2.mobile()
print(id(m1))
print(id(m2))

