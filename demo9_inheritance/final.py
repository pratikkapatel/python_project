class ClassA:
    def father_style(self):
        print("father style!123!")


class ClassB():
    def son_style(self):
        print("Son Style!!!")


class ClassC(ClassA, ClassB):
    def gson_style(self):
        print("gSon Style!!!")


obj = ClassC()
obj.father_style()
obj.son_style()
obj.gson_style()