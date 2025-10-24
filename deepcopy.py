import copy

# Original nested object
original = {
    'name': 'Mohammed',
    'skills': ['Python', 'Django', 'FastAPI'],
    'profile': {'github': 'farhan-dev', 'location': 'Hyderabad'}
}

# Deep copy
cloned = copy.deepcopy(original)

# Modify the clone
cloned['skills'].append('SQL')
cloned['profile']['location'] = 'Bangalore'

# Print both to compare
print("Original:", original)
print("Cloned:", cloned)