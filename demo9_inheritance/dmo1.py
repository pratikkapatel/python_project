class Father:
    def __init__(self):
        self.f_age = 65
        print("Father Constructor")

    def father_style(self):
        print("father style!123!")


class Son(Father):
    def __init__(self):
        super().__init__()
        self.s_age = 20
        print("Son Constructor ")

    def son_style(self):
        print("Son Style!!!")
        super().father_style()

class GSon(Son):
    def __init__(self):
        super().__init__()
        self.g_age=1
        print("GSon Constructor")

    def gson_style(self):
        print("gSon Style!!!")



s=GSon()

print(s.f_age)
print(s.s_age)
print(s.g_age)
s.father_style()
s.son_style()
s.gson_style()