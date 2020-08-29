### 
class Student:
    def __init__(self,name,grades): 
        #self.name = "Rolf"
        self.name = name
        #self.grades = (23, 34, 56, 78, 90)
        self.grades = grades

    def average(self): 
        return sum(self.grades)/len(self.grades)


student = Student("Bob", (23,45,67,89,90))
student2 = Student("Rolf", (25,47,69,93,90))
print(student.name)
# print(student.grades)
print(student.average())
print("================================================")
print("================================================")
print("================================================")
print(student2.name)
print(student2.average())



