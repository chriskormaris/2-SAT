# 2-SAT
An algorithm that given a set of CNF (conjuctive normal form) clauses using n=3 variables with 2 variables per clause (2-Satisfiability), outputs a solution (if it exists), which is an assignemnt for the truth variables that satisfies all the given CNF clauses. Written in Python.

*CNF clause example: (x1 + x2') * (x1 + x3) * (x2 + x3') * (x1' + x2') * (x1 + x2)*

*A, a set of satisfiable assignment of truth variables for the given CNF clause: x1 = True, x2 = False, x3 = False*

Note that the algorithm is guaranteed to find a solution, if it exists, in:

**(n_variables ^ 2) * (1 + 4 * math.sqrt(2/3)) = (3 ^ 2) * (1 + 4 * math.sqrt(2/3)) ~= 38** iterations.


**See *Sheldon Ross: Introduction to Probability Models* book, page 242**
