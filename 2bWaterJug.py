def pour (jug1, jug2):
    max1, max2, fill = 5, 7, 4
    print("%d\t%d"%(jug1, jug2))
    if jug2 is fill:
        return
    elif jug2 is max2:
        pour(0, jug1)
    elif jug1 != 0 and jug2 is 0:
        pour(0, jug1)
    elif jug1 is fill:
        pour(jug1, 0)
    elif jug1 < max1:
        pour(max1, jug2)
    elif jug1 < (max2 - jug2):
        pour (0, (jug1+jug2))
    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)

print("JUG1\tJUG2")
pour(0,0)






'''Water jug problem:
The water jug problem is a classic puzzle that involves two or three jugs and the task
of measuring a specific quantity of water using those jugs.
The constraints of the problem are as follows:
I. You can fill the jugs completely from the water source.
II. You can empty the jugs completely onto the ground.
III. You can transfer water from one jug to another until the source jug is empty
or the target jug is full.'''

