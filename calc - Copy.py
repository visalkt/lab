class student:
    def __init__(self,name,age,scores):
        self.name=name
        self.ag=age
        self.scores=scores
    def get_score(self):
        return sum(student.scores)/len(student.scores)
    def __str__(self):
        return student.name
student=student('VISAL',22,[45,46,19,50])
print(f'cgpa of {student} is {student.get_score()}')