def moveTower(height, fromPole, toPole, withPole): 
    if height >= 1: 
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole) 
 
def moveDisk(fp, tp): 
    print("Moving Disk from", fp, "to", tp) 
 
moveTower(3, "A", "B", "C") 


'''Tower of Hanoi:
The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number
of disks of different sizes that can slide onto any rod. The objective of the puzzle is to
move the entire stack of disks from one rod to another'''
