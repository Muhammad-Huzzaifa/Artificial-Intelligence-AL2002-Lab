from AC3 import AC3

domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

constraints = [
    ['A', '>', 'B'],
    ['B', '=', 'C']
]

as3 = AC3(domains, constraints)
print(as3.ac3_algorithm())
print(as3.domains)