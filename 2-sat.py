# Sheldon Ross: Introduction to Probability Models, page 242

import math
import random

# Inputs: a set of CNF (conjuctive normal form) clauses using n=3 variables with 2 variables per clause
# Outputs: a solution (if exists), which is an assignemnt for the truth variables that satisfies all the given CNF clauses

n_variables = 3  # 3 Boolean variables: x1, x2, x3
k_clauses = 5  # 5 clauses
num_variables_per_clause = 2  # 2: hence the name 2-sat

# _: denotes not
variables_dict = {'x1': True, '_x1': False, 'x2': True, '_x2': False, 'x3': True, '_x3': False}

# A: set of satisfiable assignment of truth variables: x1 = True, x2 = False, x3 = False
A = {'x1': True, 'x2': False, 'x3': False}

# CNF clause example: (x1 + x2') * (x1 + x3) * (x2 + x3') * (x1' + x2') * (x1 + x2)
set_of_clauses = [
    ['x1', '_x2'],
    ['x1', 'x3'],
    ['x2', '_x3'],
    ['_x1', '_x2'],
    ['x1', 'x2']
]

print('CNF clauses: ')
print(set_of_clauses)
print('')

variable_assignment = {'x1': False, 'x2': False, 'x3': False}
y_train = []  # y_train: how much different is A and variable_assignment

print('initial variable assignment of truth variables: ' + str(variable_assignment))
print('a satisfiable assignment of truth variables A: ' + str(A))
print('y_train: ' + str(y_train))
print('')

diffkeys = None
not_true_clause_found = True
stages = 0
max_stages = (n_variables ^ 2) * (1 + 4 * math.sqrt(2/3))
while not_true_clause_found and stages <= int(max_stages):

    not_true_clause_found = False

    for j in range(len(set_of_clauses)):
        clause = set_of_clauses[j]

        # check if clause is true
        true_found = False
        for i in range(len(clause)):
            value = variables_dict[clause[i]]
            if value == variable_assignment[clause[i].replace('_', '')]:
                true_found = True

        if true_found:
            print('clause ' + str(j) + ': ' + str(clause) + ' -> True')
        else:
            print('clause ' + str(j) + ': ' + str(clause) + ' -> False')

        # pick a variable randomly and change its value
        if not true_found:
            not_true_clause_found = True
            rand_index = random.randint(0, 1)
            variable_chosen = clause[rand_index].replace('_', '')

            # change the chosen variable from False to True or from True to False
            if not variable_assignment[variable_chosen]:
                print('setting variable ' + str(variable_chosen) + ' to True!')
                variable_assignment[variable_chosen] = True
            else:
                print('setting variable ' + str(variable_chosen) + ' to False!')
                variable_assignment[variable_chosen] = False

            # break  # Skip the rest of this stage and go to the next stage. NOT VERY EFFICIENT!

    diffkeys = [k for k in A if A[k] != variable_assignment[k]]
    y_train.append(len(diffkeys))

    print('current variable assignment of truth variables: ' + str(variable_assignment))
    print('y_train: ' + str(y_train))

    stages += 1
    print('**********\n')


print('stages done: ' + str(stages))
print('max stages = ceil[(n ^ 2) * (1 + 4 * sqrt(2/3))] = ' + ' ceil[' + str(max_stages) + ']' + ' = ' + str(math.ceil(max_stages)))
print('final variable assignment of truth variables: ' + str(variable_assignment))
print('a satisfiable assignment of truth variables A: ' + str(A))
print('y_train: ' + str(y_train))

if len(diffkeys) == 0:
    print('The algorithm has successfully found a solution for the 2-SAT problem!!!')
else:
    print('The algorithm did NOT find a solution for the 2-SAT problem.')
