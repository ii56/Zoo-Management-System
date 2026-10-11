class Employee:
    def __init__(self, name, employee_id, salary, role):
        self.name = name
        self.employee_id = str(employee_id)
        self.salary = salary
        self.role = role

    # Get employee details
    def get_details(self):
        return f"[{self.employee_id}] {self.name} | Role: {self.role} | Salary: {self.salary}"

    # Salary method
    def get_salary(self):
        return self.salary


class Zookeeper(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary, role="ZooKeeper")

    def feed_animal(self, animal, food_type=None):
        return animal.feeding(food_type)


class Vet(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary, role="Veterinarian")

    def treat_animal(self, animal):
        return animal.heal()
