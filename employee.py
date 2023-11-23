from person import Person
class Employee(Person):
    def __init__(self,name,age,mobile_number,address,salary):
        super().__init__(name,age,address,mobile_number)
        self.salary=salary
    def print_details(self):
       print(f'Name:{self.name}\nAge:{self.age}\nAddress:{self.address}\nMobile number:{self.mobile_number}\nSalary:{self.salary}')
    
a=Employee('visal',22,'poovathodi',9048305602,5000)