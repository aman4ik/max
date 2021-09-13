class Employee():
    emp_count=0
    Work_rate=2

    def init(self,name,salary):
        self.something=name
        self.somebody=salary



    def  display_count(self):
        pass

    def display_employee(self):
        print(f"мое имя {self.something}моя зарплата{self.somebody}")

    def change_name(self):
         self.something="RICK"

    def get_total_salary(self):
        print(self.somebody)


p1 = Employee("Rick", 100)
p2 = Employee("Morty", 2000)
p3 = Employee("Peter", 1200)
p4 = Employee("Gwen", 1250)

p1.display_employee()
p1.change_name()
p1.display_employee()
p2.get_total_salary()
