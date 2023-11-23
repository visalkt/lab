#this is list containing a group of numbers
l=[5,10,15,20,25]
#this is a dictionary that stores info about a student
b=input('enter your name: ')
a=int(input('enter your age: '))
student={'name':b,'age': a,'course':'Django Malayalam Course'}
if student['age']<18:
    print('\n This student is a minor')
else:
    print('This student is an adult')
print('\n The list before appending :',l)
l.append(30)#adding a new number to the list.
print('\n The list after appending :',l)
print('\n The details before adding grade',student)
g=input('\n Enter the grade of the student: ')
student['grade']=g#adding grade to the students information.
print('\n the details after adding grade',student)

if student['grade']=='A':
    print('\n This student has an excellent grade!')
else:
    print("This student is doing well but not at the top")