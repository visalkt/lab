from employee import Employee

employees=[]

n=int(input('enter the number of employee : '))

for _ in range(n):
    name=input('name: ')
    age=int(input("age: "))
    address=input('address: ')
    mobile_number=int(input("mobile number: "))
    salary=float(input('salary: '))
    empolyee=Employee(name,age,mobile_number,address,salary)
    employees.append(empolyee)

search_name=input('\nEnter a name to search')

found = False
for employee in employees:
    if employee.name == search_name:
        employee.print_details()
        found=True
        break
if not found:
    print("employees not found")


    