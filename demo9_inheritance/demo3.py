class Father:

    def __init__(self, father_age):
        self.fage = father_age
        self.driver = "chrome"
        print("Father Constructor")

    def father_style(self):
        print("father style!!")


class Son(Father):
    def __init__(self, father_age, son_age):
        super().__init__(father_age)
        self.sage = son_age

        print("Son Constructor ")

    def son_style(self):
        print("Son Style!!!")

    def print_all_variable(self):
        print(self._fage)
        print(self.sage)
        print(self.driver)
        self.father_style()


s = Son(70, 20)
s.print_all_variable()