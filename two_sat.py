# Sheldon Ross: Introduction to Probability Models, page 242

import math
import random

# Inputs: a Boolean formula with n=3 distinct variables and 2 variables per clause
# Outputs: a solution (if it exists),
# which is a satisfiable assignment of the variables that result in the formula being TRUE

n = 3  # n=3 Boolean variables: x1, x2, x3
num_variables_per_clause = 2  # 2: hence the name 2-sat

# A, a set of satisfiable assignment of truth variables: x1 = True, x2 = False, x3 = False
A = {'x1': True, 'x2': False, 'x3': False}

# CNF clause example: (x1 + x2') * (x1 + x3) * (x2 + x3') * (x1' + x2') * (x1 + x2)
# _: denotes not
set_of_clauses = [
    ['x1', '_x2'],
    ['x1', 'x3'],
    ['x2', '_x3'],
    ['_x1', '_x2'],
    ['x1', 'x2']
]

k = len(set_of_clauses)  # k=5 clauses

print('CNF clauses: ')
print(set_of_clauses)
print()

variable_assignment = {'x1': False, 'x2': False, 'x3': False}
Y = []  # Y: how much different "A" is from "variable_assignment"

print(f'Initial variable assignment of truth variables: {variable_assignment}')
print(f'A satisfiable assignment of truth variables A: {A}')
print(f'Y: {Y}')
print()

diff_keys = []
not_true_clause_found = True
stages = 0
max_stages = math.pow(n, 2) * (1 + 4 * math.sqrt(float(2) / 3))
while not_true_clause_found and stages <= int(math.ceil(max_stages)):

    not_true_clause_found = False

    for j in range(k):
        clause = set_of_clauses[j]

        # check if clause is true
        true_found = False
        for i in range(len(clause)):
            # for i in range(num_variables_per_clause):
            value = False if '_' in clause[i] else True
            if value == variable_assignment[clause[i].replace('_', '')]:
                true_found = True

        if true_found:
            print(f'clause {j}: {clause} -> True')
        else:
            print(f'clause {j}: {clause} -> False')

        # pick a variable randomly and change its value
        if not true_found:
            not_true_clause_found = True
            rand_index = random.randint(0, 1)
            variable_chosen = clause[rand_index].replace('_', '')

            # change the chosen variable from False to True or from True to False
            if not variable_assignment[variable_chosen]:
                print(f'setting variable {variable_chosen} to True!')
                variable_assignment[variable_chosen] = True
            else:
                print(f'setting variable {variable_chosen} to False!')
                variable_assignment[variable_chosen] = False

            # Skip the rest of this stage and go to the next stage.
            # FOR DEBUGGING ONLY!
            # break

    diff_keys = [i for i in A if A[i] != variable_assignment[i]]
    Y.append(len(diff_keys))

    print(f'Current variable assignment of truth variables: {variable_assignment}')
    print(f'Y: {Y}')

    stages += 1
    print('**********\n')

print(f'stages done: {stages}')
print(f'max stages = ceil[(n ^ 2) * (1 + 4 * sqrt(2/3))] = ceil[{max_stages}] ~= {int(math.ceil(max_stages))}')
print(f'Final variable assignment of truth variables: {variable_assignment}')
print(f'A satisfiable assignment of truth variables A: {A}')
print(f'Y: {Y}')

if len(diff_keys) == 0:
    print('The algorithm has successfully found a solution for the 2-SAT problem!!!')
else:
    print('The algorithm did NOT find a solution for the 2-SAT problem.')
