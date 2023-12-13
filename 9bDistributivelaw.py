import random

def demonstrate_distributive_law():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    left_hand_side = a * (b + c)
    right_hand_side = (a * b) + (a * c)

    print(f"Using the distributive law for a = {a}, b = {b}, c = {c}:")
    print(f"Left-hand side (a * (b + c)): {a} * ({b} + {c}) = {left_hand_side}")
    print(f"Right-hand side ((a * b) + (a * c)): ({a} * {b}) + ({a} * {c}) = {right_hand_side}")

    if left_hand_side == right_hand_side:
        print("The distributive law holds true.")
    else:
        print("The distributive law does not hold true.")

# Demonstrate the distributive law
demonstrate_distributive_law()


'''Distributive law, also called distributive property, in mathematics, the law relating
the operations of multiplication and addition, stated symbolically as a(b + c) = ab
+ ac; that is, the monomial factor a is distributed, or separately applied, to each
term of the binomial factor b + c, resulting in the product ab + ac. From this law it
is easy to show that the result of first adding several numbers and then
multiplying the sum by some number is the same as first multiplying each
separately by the number and then adding the products.'''
