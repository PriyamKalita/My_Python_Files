class Empolyee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"the name is {self.name}. salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good" + string)


class programmer(Empolyee):
    no_of_leaves = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"the programmer's name is {self.name}. salary is {self.salary} and role is {self.role}. the languages are {self.languages}"


harry = Empolyee("harry", 255, "instructor")
rohan = Empolyee("rohan", 455, "student")

shubham = programmer("shubham", 555, "programmer", ["python"])
karan = programmer("karan", 777, "programmer", ["python", "cpp"])

print(karan.no_of_leaves)



