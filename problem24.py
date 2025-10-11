# Can we include a list inside a set in Python? Let's test it.

# ❌ Incorrect version: lists are unhashable, so this will raise an error
# s = {8, 7, 12, "Farhan", [1, 2]}  # TypeError: unhashable type: 'list'

# ✅ Correct version: using a tuple instead of a list
s = {8, 7, 12, "Farhan", (1, 2)}
print("Valid set:", s)