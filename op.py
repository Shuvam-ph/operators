# Basic arithmetic
print(24 + 9)       # → 33
print(24 - 9)       # → 15
print(24 * 9)       # → 216

# Division always gives float in Python 3
print(9 / 4)        # → 2.25 (float)
print(8 / 2)        # → 4.0 (float, not 4!)

# Floor division — rounds DOWN always
print(23 // 6)      # → 3 (not 3.833...)
print(-23 // 6)     # → -4 (rounds DOWN to -4, not towards zero!)

# Modulus — the remainder after floor division
print(23 % 6)       # → 5 (23 = 3×6 + 5)
print(16 % 4)       # → 0 (16 divides evenly — no remainder)
print(11 % 2)       # → 1 (11 is odd)

# Exponentiation
print(3 ** 5)       # → 243
print(144 ** 0.5)   # → 12.0 (square root)
print(125 ** (1/3)) # → 5.0 (cube root)




# Basic comparisons
print(15 == 15)  # → True
print(20 != 20)  # → False
print(50 > 30)   # → True

# Chained comparisons — unique to Python, reads like maths
val = 8
print(1 < val < 10)   # → True (8 is between 1 and 10)
print(8 <= val <= 12)  # → True (8 is equal to 8 and less than 12)
print(8 < val < 15)   # → False (val is equal to 8, not strictly greater than 8)

# String comparisons — lexicographic (letter by letter)
print("orange" < "apple")  # → False ('o' comes after 'a' in Unicode)
print("Code" == "Code")    # → True (identical case and characters)

# Comparing booleans with numbers
print(0 == True)    # → False (True equals 1, not 0)
print(1 == False)   # → False (False equals 0, not 1)
print(25 == "25")   # → False (int and str are different types)




# Compound assignment operators
points = 80
points += 20  # points is now 100
points *= 3   # points is now 300
points -= 50  # points is now 250
print(points) # → 250

# Multiple assignment — assign several variables in one line
p = q = r = 7 # all three become 7
print(p, q, r) # → 7 7 7

# Tuple unpacking — assign different values in one line
first, second, third = 10, 20, 30
print(first, second, third) # → 10 20 30

# Swap variables — Pythonic way, no temporary variable needed
num1, num2 = 100, 500
num1, num2 = num2, num1 # swap!
print(num1, num2) # → 500 100



# and — both conditions must be True
user_age = 16
has_permission = True
print(user_age >= 18 and has_permission)  # → False (first condition is False)

# or — at least one condition must be True
is_member = False
is_guest = False
print(is_member or is_guest)  # → False (both conditions are False)

# not — inverts the boolean value
is_active = False
print(not is_active)  # → True (inverts False to True)
print(not (10 > 5))   # → False (10 > 5 is True, not inverts it)

# Short-circuit with 'and' — right side skipped if left is False
print((5 < 2) and (10 / 0 == 0))  # → False (no ZeroDivisionError!)

# Short-circuit with 'or' — right side skipped if left is True
print((10 > 2) or (10 / 0 == 0))  # → True (no ZeroDivisionError!)

# Combining logical operators with comparison operators
temperature = 38
print(temperature >= 15 and temperature <= 30)  # → False (out of comfortable range)
print(temperature < 0 or temperature > 35)      # → True (extreme temperature)



# bin() shows the binary representation of any number
print(bin(5)) # → 0b101
print(bin(3)) # → 0b11
# AND — 1 only where both bits are 1
print(5 & 3) # → 1 (0101 & 0011 = 0001)
# OR — 1 where either bit is 1
print(5 | 3) # → 7 (0101 | 0011 = 0111)
# XOR — 1 where bits are different
print(5 ^ 3) # → 6 (0101 ^ 0011 = 0110)
# Left shift — multiply by powers of 2
print(5 << 1) # → 10 (5 × 2)
print(5 << 2) # → 20 (5 × 4)
# Right shift — divide by powers of 2
print(20 >> 1) # → 10 (20 ÷ 2)
print(20 >> 2) # → 5 (20 ÷ 4)



# Membership — checking if a value exists in a sequence
print("py" in "python") # → True
print("Java" in "python") # → False
print("z" not in "hello") # → True
# Identity — == checks value equality, is checks object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b) # → True (same values)
print(a is b) # → False (different objects in memory)
print(a is c) # → True (same object — c points to a)
# The correct way to check for None — always use 'is'
x = None
print(x is None) # → True ✅ correct
print(x == None) # → True ⚠️ works but not recommended



# * before + (same as BODMAS)
print(2 + 3 * 4) # → 14 (* before +)
print((2 + 3) * 4) # → 20 (parentheses first)
# ** is right to left
print(2 ** 3 ** 2) # → 512 (2 ** (3 ** 2) = 2 ** 9)
print((2 ** 3) ** 2) # → 64 (different result with brackets!)
# Comparison before logical operators
print(5 > 3 and 2 < 4) # → True (comparisons first, then and)
print(not True or True) # → True (not binds tighter than or)
# When unsure — always use parentheses for clarity
result = (5 + 3) * (10 - 4)
print(result) # → 48 (clear and unambiguous)