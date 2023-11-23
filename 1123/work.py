class Employee:
  
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self._name = emp_name
        self._id = emp_id
        self._salary = emp_salary
        self._department = emp_department
   
    def assign_department(self, new_department):
        self._department = new_department
    
    def print_employee_details(self):
        print(f'NAME={self._name}')
        print(f'ID={self._id}')
        print(f'SALARY={self._salary}')
        print(f'DEPARTMENT={self._department}')

    def calculate_emp_salary(self, hours_worked):   
        base_salary = self._salary  
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (base_salary / 50))
            total_salary = base_salary + overtime_amount
        else:
            total_salary = base_salary
        return total_salary

Emp1 = Employee('ADAMS','E7876',50000,'ACCOUNTING')
Emp2 = Employee('JONES','E7499',45000,'RESEARCH')
Emp3 = Employee('MARTIN','E7900',50000,'SALES')
Emp4 = Employee('SMITH','E7698',55000,'OPERATIONS')

Emp1.assign_department('SALES')
Emp1.print_employee_details()
ADAMS_salary=Emp1.calculate_emp_salary(55)
print(f'ADAMS TOTAL SALARY:{ADAMS_salary}')





