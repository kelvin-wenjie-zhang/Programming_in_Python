#part 1 (4) - List Comprehensions
employees = [('Bob', 40, 18.25), ('Mary', 10, 20.00), ('John', 0, 100.90), ('Carl', 19, 17.21), ('Meg', 60, 22.10)]

#employees[a][0] is the name
#employees[a][1] is the working hours
#employees[a][2] is the hourly wage
#the if statement filter out the case where working hours is zero this week
#the list function would convert the list comprehension into a list so that we can print it out to the concole
print(list([(employees[a][0], employees[a][1]*employees[a][2]) for a in range(len(employees)) if employees[a][1] != 0]))
