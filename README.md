N-Queens Problem Solver

Description

This Python script solves the N-Queens problem using a backtracking approach. The N-Queens problem is a classic combinatorial problem where the goal is to place N queens on an N×N chessboard such that no two queens threaten each other.

How It Works

The script implements the following functions:

verif_but(etat, n): Checks if a solution is complete by verifying if the length of the current state (etat) is equal to n.

est_valide(etat, colonne, ligne): Determines if a queen can be placed at a given column and row without conflicting with previously placed queens.

succ(etat, n): Generates valid successor states by adding a new queen to the current board configuration.

resolution(n): Recursively finds all possible solutions using a backtracking approach.

How to Run the Code

Ensure you have Python installed on your system.

Copy and paste the script into a Python file (e.g., n_queens.py).

Run the script using: python n_queens.py
The output will display the number of solutions and all valid board configurations.
Example Output :
Number of solutions for 8-Queens: 92
[0, 4, 7, 5, 2, 6, 1, 3]
[0, 5, 7, 2, 6, 3, 1, 4]
...
Complexity

The time complexity of this algorithm is approximately O(N!) in the worst case, making it impractical for very large values of N.

Applications

AI and constraint satisfaction problems

Chess-related problem-solving

Algorithmic optimization and recursion learning

Notes

The algorithm may take longer for larger values of N due to the exponential growth of possibilities.

The current implementation finds all solutions, but can be modified to return only one solution if needed.

Author

This script was written as part of an exercise in solving constraint satisfaction problems using recursion and backtracking.
