class Employee:
    def __init__(self, fname, lname, employee_id):
        self.fname = fname
        self.lname = lname
        self.employee_id = employee_id
    
    def __str__(self):
        return f'Employee: {self.fname} {self.lname} ({self.employee_id})'

class WageEmployee(Employee):
    def __init__(self, fname, lname, employee_id, hourly_wage, weekly_hours):
        super().__init__(fname, lname, employee_id)
        self.hourly_wage = hourly_wage
        self.weekly_hours = weekly_hours
    
    def weekly_earnings(self):
        weekly_earnings = self.hourly_wage * self.weekly_hours
        return format(weekly_earnings, '.2f')

    def __str__(self): 
        return 'Wage' + super().__str__() + f' WEEKLY EARNINGS: ${self.weekly_earnings()}'

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, employee_id, yearly_salary):
        super().__init__(fname, lname, employee_id)
        self.yearly_salary = yearly_salary
    
    def weekly_earnings(self):
        weekly_earnings = self.yearly_salary / 52
        return format(weekly_earnings, '.2f')

    def __str__(self):
        return 'Wage' + super().__str__() + f' WEEKLY EARNINGS: ${self.weekly_earnings()}'    

my_employee1 = Employee("Ronnie", "McDonnie", 200117240)
my_employee2 = WageEmployee("Johnny", "McDonnie", 200117240, 13.00, 35)
my_employee3 = SalaryEmployee("Donnie", "McDonnie", 200117240, 25000)

print(my_employee1)
print(my_employee2)
print(my_employee3)
