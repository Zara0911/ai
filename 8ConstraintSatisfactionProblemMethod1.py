#Constraint satisfaction problem 


def add_constraint(var):
    constraints[var] = []
    for i in range(9):
        if i != var[0]:
            constraints[var].append((i, var[1]))
        if i != var[1]:
            constraints[var].append((var[0], i))
    sub_i, sub_j = var[0] // 3, var[1] // 3
    for i in range(sub_i * 3, (sub_i + 1) * 3):
        for j in range(sub_j * 3, (sub_j + 1) * 3):
            if (i, j) != var:
                constraints[var].append((i, j))
                  
constraints = {}
for i in range(9):
    for j in range(9):
        add_constraint((i, j))
          
print(constraints)



'''Explanation:
Constraint Satisfaction Problem (CSP) is a fundamental topic in artificial intelligence (AI) that deals with
solving problems by identifying constraints and finding solutions that satisfy those constraints.CSP has a
wide range of applications, including scheduling, resource allocation, and automated reasoning.
CSP is a specific type of problem-solving approach that involves identifying constraints that must be
satisfied and finding a solution that satisfies all the constraints. CSP has been used in a variety of
applications, including scheduling, planning, resource allocation, and automated reasoning'''
