# class Mass:
#     def __init__(self,kg=0, g=0):
#         self.kg = kg
#         self.g = g
#     def __add__(self,other):
#         total_kg = self.kg + other.kg
#         total_g = self.g + other.g
#
#         if total_g>=1000:
#             total_kg += total_g // 1000
#             total_g = total_g % 1000
#
#         return Mass(total_kg, total_g)
#
#     def __repr__(self):
#         return f"{self.kg} kg and {self.g} g"
#
#
#
# mass1 =Mass(2,500)
# mass2= Mass(1,750)
#
# mass3 = mass1 + mass2
# print(mass3)





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Months:
    def __init__(self, month, year):
        self.month = month
        self.year = year

    def __add__(self, other):
        total_month = self.month + other.month
        total_year = self.year + other.year

        if total_month >= 12:
            total_year += total_month // 12
            total_month = total_month % 12
        return Months(total_month, total_year)

    def __repr__(self):
        return f"{self.month} month and {self.year} year"

test1 = Months(36,2)
test2 = Months(36,2)
test3 = Months(36,2)
print(test1+test2+test3)



#`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~`























