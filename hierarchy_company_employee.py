class Employee:
    def __init__ (self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        raise NotImplementedError


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__ (self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id) 
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(FullTimeEmployee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)    
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

class Contractor(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


full_time_employee = FullTimeEmployee("Navaneedh", 101, 50000)
part_time_employee = PartTimeEmployee("Vinoth", 102, 20, 25)
manager = Manager("Akash", 103, 100000, 25000)
contractor = Contractor("Praveen", 104, 30, 40)

print("Full time Employee Salary:" ,(full_time_employee.calculate_salary()))
print("Part time Employee Salary:" ,(part_time_employee.calculate_salary()))
print("Manager Salary:" ,(manager.calculate_salary()))
print("Contractor Salary:" ,(contractor.calculate_salary()))


