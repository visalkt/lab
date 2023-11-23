#this is list containing a group of numbers
l=[5,10,15,20,25]
#this is a dictionary that stores info about a student
student={'name':'visal','age': 22,'course':'Django Malayalam Course'}
if student['age']<18:
    print('\n This student is a minor')
else:
    print('This student is an adult')
print('\n The list before appending :',l)
l.append(30)#adding a new number to the list.
print('\n The list after appending :',l)

student['grade']='A'#adding grade to the students information.

if student['grade']=='A':
    print("\n This student has an excellent grade!")
else:
    print("This student is doing well but not at the top")