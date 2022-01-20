# Map-Coloring-Problem

Visualization using GeoPanda Library:

![MapColoringProblem](https://github.com/smitanannaware/Map-Coloring-Problem/blob/main/animation.gif)
## Constraint satisfaction problems
- A CSP is a problem composed of a finite set of variables X<sub>i</sub>, each of which has a finite domain values D<sub>i</sub> and a set of constraints C<sub>m</sub>.
- A set of constraints, i.e. relations that are assumed to hold between the values of the variables. These relations can be given intentionally, i.e. as a formula, or extensionally, i.e. as a set, or procedurally, i.e. with an appropriate generating or recognising function.
- The constraint satisfaction problem is to find, for each i from 1 to n, a value in Di for xi so that all constraints are satisfied i.e. goal test is a set of constraints specifying allowable combinations of values for subsets of variables.
- General purpose CSP problem use the graph structure to speed up the search
- Binary CSP: each constraint relates two variables
- Constraint graph:
    - Nodes are variables
    - Edges are constraints

## Map Colouring
- The Map colouring problem is similar to the graph colouring problem.
- In map colouring, the constraint is that states which are adjacent to each other i.e. share a border should not have the same colour.
- Consider the fig 3 for map colouring
![image](https://user-images.githubusercontent.com/93964366/150237559-b68899ff-2f93-4fe6-b837-8a68e4b33b8d.png)

## Map Colouring Solution Approaches
There are 3 approaches used in this project
1. Depth first search
2. Depth first search + forward checking
3. Depth first search + forward checking + propagation through singleton domains

### Depth first search
- Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree
- DFS assigns the colors to state following a order and satisfying the constraints. If any particular state does not have valid domain then it backtracks and process other available domain values for the previous states.

### Depth first search + forward checking
- This method also uses the DFS with backtracking methid. In addition to this it uses forward checking method.
- The basic idea of forward checking(FC) is that, if suppose value ‘a’ has been selected for vertex A then FC will remove value ‘a’ from domain of all the vertices which are adjacent to A.

### Depth first search + forward checking + propagation through singleton domain
- Here the algorithm checks among all possibilities of next states and choses the one with domain value equal to 1 and propagates to the next unassigned variables from the one with domain = 1. Number of backtracks are further reduced and the algorithm is relatively faster.

## Heuristic Function used:-
There are 3 functions used:
1. Minimum Remaining Values
2. Degree heuristic
3. Least Constraint Value
### Minimum Remaining Values
- In this heuristic propagation follows in the order of those nodes with least number of values in its domain .
- With respect to map colouring problem If one state has 2 permissible values in its domain and another state has 3 then the state with 2 values would be chosen first , here permissible refers to reducing domain size because of constraints imposed that adjacent states cannot have same color.

### Degree heuristic
- The idea here is assign a value to the variable that is involved in the largest number of constraints on other unassigned variables.
- It is often used as a means to reduce the number of same next possibilities ie as a tie breaker with Minimum remaining values heuristic to choose the best next when all next nodes have the same number of domain values after a variable assignment is done using MRV.

### Least Constraint Value
- Here the chosen heuristic rules out the fewest values in the remaining variables.
