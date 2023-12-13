import itertools, random
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print("You got:")
for i in range(5):
      print(deck[i][0], "of", deck[i][1])


///////////////////////////////////////////////////////////////

# beforeshuffel and aftershuffel.
import random 
s=["ace",1,2,3,4,5,6,7,8,9,"king","joker","queen"] 
h=["ace",1,2,3,4,5,6,7,8,9,"king","joker","queen"] 
l=["ace",1,2,3,4,5,6,7,8,9,"king","joker","queen"] 
d=["ace",1,2,3,4,5,6,7,8,9,"king","joker","queen"] 
print("\nBefore shuffle\n")
print(s)
print(h) 
print(l)
print(d)
print("\nAfter shuffle\n") 
shuf=random.shuffle(s)
print(s) 
shuf=random.shuffle(h)
print(h) 
shuf=random.shuffle(l) 
print(l) 
shuf=random.shuffle(d)
print(d)

