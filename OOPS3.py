class employee:
    no_of_leaves = 8
    pass

harry = employee()
rohan = employee()

harry.name = "Harry"
harry.salary = 399
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 199
rohan.role = "student"

print(employee.no_of_leaves)
print(employee.__dict__)
employee.no_of_leaves = 9
print(employee.__dict__)
print(employee.no_of_leaves)


# instance's don't change class variables