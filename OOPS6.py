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
        # params = string.splkit("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Empolyee("harry", 255, "instructor")
rohan = Empolyee("rohan", 455, "student")
karan = Empolyee.from_dash("karan-480-student")

print(karan.no_of_leaves)


# rohan.change_leaves(34)

# print(harry.no_of_leaves)


