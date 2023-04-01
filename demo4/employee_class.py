import math


class Employee:
    company_name = None  # static variable or class variable
    company_location = None
    __company_password = "tt&"

    def __init__(self):
        self.emp_id = None  # non-static variable or instance variable
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None
        self.employee_type = "C"
        self.__company_code = 0

    # getter method
    def get_company_code(self):
        return self.__company_code

    # setter method
    def set_company_code(self, company_code):
        if company_code > 100:
            self.__company_code = company_code
        else:
            print("Invalid company code so it remains 0")

    """ get property """

    @property
    def get_company_code_p(self):
        return self.__company_code

    """ set property """

    @get_company_code_p.setter
    def set_company_code_p(self, company_code):
        if company_code > 100:
            self.__company_code = company_code
        else:
            print("Invalid company code so it remains 0")

    @staticmethod
    def print_author_name():
        print("Author Name: ", "Balaji Dinakaran")

    def display_employee_record(self):
        print(35 * "-")
        print(self)
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Performance:", self.emp_performance)
        print("Company Name:", Employee.company_name)
        print("Company Location:", Employee.company_location)
        print("Company Code: ", self.__company_code)
        print(35 * "-")

    def calculate_bonus(self):
        if self.emp_performance == "A":
            self.emp_salary = self.emp_salary + ((10 / 100) * self.emp_salary)
        elif self.emp_performance == "B":
            self.emp_salary = self.emp_salary + ((5 / 100) * self.emp_salary)
        elif self.emp_performance == "C":
            self.emp_salary = self.emp_salary + ((2 / 100) * self.emp_salary)
        else:
            print(self.emp_name, " - no bonus")