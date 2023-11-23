class Person:
    def __init__(self,name,age,mobile_number,address):
        self.name=name
        self.age=age
        self.mobile_number=mobile_number
        self.address=address
    def __str__(self):
        return Person.name
