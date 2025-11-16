"""
🧾 Question:
Create an Employee class with:
- name and department attributes
- auto-generated employee_id using a class variable
- ID should look like EMP1, EMP2, EMP3, etc.
"""

class Employee:
    id_counter = 1  # Shared across all employees

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.employee_id = "EMP" + str(Employee.id_counter)
        Employee.id_counter += 1

    def show(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Employee ID:", self.employee_id)


# 🧪 Sample Usage
emp1 = Employee("Mohammed Farhan", "Backend")
emp2 = Employee("Aisha Khan", "Frontend")

emp1.show()
print("-----")
emp2.show()