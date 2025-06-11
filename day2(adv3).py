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







#
#
# class c_omputer:
#     company = "dell"
#     # count = 2
#     def __init__(self, ram, processor, rom):
#         self.ram = ram
#         self.processor = processor
#         self.rom = rom
#     def system(self):
#         print("computer is running")
#         print(self.ram, self.processor, self.rom)
# c1 = c_omputer(8,10, 100)
# c2 = c_omputer(16,90, 100)
# c3 = c_omputer(16,100, 100)
# c1.system()
# c2.system()
# c3.system()




# car design

class Car_Design:
    def __init__(self, model, color, year, ):
        self.model = model
        self.color = color
        self.year = year


    def car_info(self):
        print("Model:", self.model,",Color:",self.color,",Size:", self.year)


c1 = Car_Design("Hyundai","Blue",2002)
c2 = Car_Design("Marutii", "Red",2001)
c1.car_info()
c2.car_info()

