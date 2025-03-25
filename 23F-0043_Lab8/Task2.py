from AC3 import AC3

domains = {
    'WA': ['R'],
    'NT': ['G'],
    'SA': ['R', 'G', 'B'],
    'Q': ['R' ,'G', 'B'],
    'NSW': ['R', 'G', 'B'],
    'V': ['R', 'G', 'B'],
    'T': ['R', 'G', 'B']
}

constraints = [
    ['SA', '!=', 'WA'],
    ['SA', '!=', 'NT'],
    ['SA', '!=', 'Q'],
    ['SA', '!=', 'NSW'],
    ['SA', '!=', 'V'],
    ['WA', '!=', 'NT'],
    ['NT', '!=', 'Q'],
    ['Q', '!=', 'NSW'],
    ['NSW', '!=', 'V']
]

ac3 = AC3(domains, constraints)
print(ac3.ac3_algorithm())
print(ac3.domains)