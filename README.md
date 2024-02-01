Variables:

Variables represent the unknowns in the matrix. rows and ccolumnswhich we represent with a pair of numbers such as [i,j] and are the 81 cells in the soduko.
Domains:

The domains represent the possible values that each variable can take. which are numbers from 1 to 9.{1, 2, 3, 4, 5, 6, 7, 8, 9}. this domain is same for all variables.
Constraints:

Uniqueness constraint: No number can repeat within a row, a column, or a 3x3 block. This constraint is the same as in classic Sudoku. Sum constraint: The sum of numbers in each cage must be equal to the number in the upper left corner of the cage. This constraint ensures that the sum rule is satisfied.
Formulating the CSP model:

The CSP model consists of the variables, domains, and constraints. In this case, we have 81 variables (X[i, j] for i from 1 to 9 and j from 1 to 9), each with the domain {1, 2, 3, 4, 5, 6, 7, 8, 9}. The constraints include the uniqueness constraint (no repetitions in rows, columns, or 3x3 blocks) and the sum constraint for each cage.