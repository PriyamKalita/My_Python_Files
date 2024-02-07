
"""
class employee:
    no_of_leaves = 8

    def printdetails(self):
        return f"name is {self.name}, slary is {self.salary}, and role is {self.role} "

harry = employee()
rohan = employee()

harry.name = "Harry"
harry.salary = 399
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 199
rohan.role = "student"

print(rohan.printdetails())
print(harry.printdetails())

print(rohan.no_of_leaves) """

from OOPS3 import employee, harry


class employee:
    no_of_leaves = 8

    def __init__(self, aname,asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return  f"the name is {self.name}. salary is{self.salary} .and role is {self.role}"

harry = employee("Harry", 255, "Instructor")


print(harry.salary)





