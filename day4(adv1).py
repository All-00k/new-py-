class father:
    def feature1(self):
        print("Feature 1 of father")

    def feature2(self):
        print("Feature 2 of father")


class mother():
    def feature3(self):
        print("Feature 3 of mother")

    def feature4(self):
        print("Feature 4 of mother")


class child(father, mother):
    def feature5(self):
        print("Feature 5 of child")

    def feature6(self):
        print("Feature 6 of child")




f = father()
f.feature1()
f.feature2()



m = mother()
m.feature3()
m.feature4()



c = child()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()
