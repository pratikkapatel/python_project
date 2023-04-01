from demo9_inheritance.employee_module import ContractEmployee, PermanentEmployee

emp=ContractEmployee(10001)

# emp.__emp_id=101
emp.emp_name="John-Contract"
emp.contract_duration=5

emp.display_employee_record()
emp.calculate_salary()

emp1=PermanentEmployee(1001)
emp1.emp_id=1001
emp1.emp_name="Peter"
emp1.employee_type="P"

emp1.display_employee_record()
emp1.calculate_salary()