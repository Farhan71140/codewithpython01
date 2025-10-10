# Initialize an empty set
s = set()

# Add an integer
s.add(20)
print("After adding 20:", s)

# Add a float with the same value
s.add(20.0)
print("After adding 20.0 (float):", s)

# Add a string with the same digits
s.add('20')
print("After adding '20' (string):", s)

# Final length of the set
print("Final length of set:", len(s))