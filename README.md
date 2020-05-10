# 2-SAT
This is an algorithm that given a Boolean formula with n=3 variables overall and 2 variables per clause (2-Satisfiability), determines the values of the variables that result in the formula being TRUE, or determines that there is no solution and the formula is never TRUE. Written in Python.

*Boolean formula example: (x1 + x2') * (x1 + x3) * (x2 + x3') * (x1' + x2') * (x1 + x2)*

-A Boolean formula is a combination of CNF (conjuctive normal form) clauses.

-*"A"*, is a satisfiable assignment of the variables that result in the formula being TRUE. i.e.: x1 = True, x2 = False, x3 = False*

Note that the algorithm is guaranteed to find a solution, if it exists, in:

**n_variables<sup>2</sup> * (1 + 4 * sqrt(2 / 3)) = 3<sup>2</sup> * (1 + 4 * sqrt(2 / 3)) ~= 38** iterations.


**See *Introduction to Probability Models, 10th Edition, Sheldon Ross* book, page 241**

https://www.academia.edu/7013149/Introduction_to_Probability_Models_-_Sheldon_M-1._Ross
