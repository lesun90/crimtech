This contain the code to sovle the puzzle given by THE CIMPRESS TECH CHALLENGE
(http://cimpress.com/techchallenge/)
The code is written in Python, test and run in Ubuntu 14.04 system

-------------------
Contact Infomation:
-------------------
Author : Duong Le
Email  : lesun90@gmail.com
Phone  : +1 202 621 3319
Country: US

----------------
How To Run
----------------
To solve one single puzzle:
    python finalSolution.py
To solve 600 puzzles:
    ./submit.sh

-----------------------
Algorithm Explanation:
-----------------------
Let consider this simpler problem, how many squares can fit into a grid?
The solution is quite simple. Find the largest square in the grid, take it 
out of the grid, repeat until the grid is empty. Count how many squares have to
be removed.

To find a largest square, I start at a position in the grid, and expand from that 
position until I could not expand anymore. My observation is that in order to have 
the largest square, a square should be started at a corner of the grid and expand 
from that corner. Choosing difference kind of corner will affect the size of 
squares and finally, affect the final number of squares we can fit in a grid

There are 4 directions of expansion:
- column goes right, row goes down (direction 1)
- column goes left, row goes down (direction 2)
- column goes right, row goes up (direction 3)
- column goes left, row goes up (direction 4)

And possible 8 kinds of corners in the grid.
- Possilbe of the 2 corners at the top left, which can only expand in direction 1
- Possilbe of the 2 corners at the top right, which can only expand in direction 2
- Possilbe of the 2 corners at the bottom left, which can only expand in direction 3
- Possilbe of the 2 corners at the bottom right, which can only expand in direction 4

From this observation, I came up with my first algorithm which is quite simple.
Pseudocode:
    For each kind of corner:
        While grid is not empty:
            From the same kind corner of grid, find the largest square, remove it from the grid
            Store the info of that square
    From the solutions of using each kind of corner, choose the best solution 
    (solution with fewest squares)

I call this algorithm 'The deep search algorithms' since it only 'digging' in one 
direction until it found a solution (the grid is empty). This algorithm only uses one
kind of corner each time, find the largest square from that corner and remove it 
in the grid until the grid is empty. Although this algorithm still produces the 
correct solution, but, obviously, it cannot give best solution for the puzzle. 
However, this algorithm can still provide an estimated minimum number of squares 
that can fit into the grid. The best solution of the puzzle cannot have more squares 
than the number of squares in the solution from this algorithm. In addition, since 
this algorithm is very simple and straight forward, it solves puzzle very quickly. 
These features of this algorithm will become very useful for my final algorithms.

The solution of the puzzle can be described as a sequence of squares that will be 
removed from the grid until the grid is empty. The question is, for each time we 
remove a square from grid, square from which corner will be removed?

This problem can be formulated as a search problem. This search problem can be 
described as following:
    Initial node: the original grid
    Operator    : choose a corner of grid, find the largest square from that corner, 
                  remove that square from grid
    Goal node   : empty grid.
    (From a node, apply operators will generate its child nodes)

To solve this search problem, I implemented the A Star (A*) Algorithm. 
A* algorithm uses a knowledge-plus-heuristic cost function of node x (denoted f(x)) 
to determine the order in which the search visits nodes in the tree. The cost 
function is a sum of two functions:
    g(x): the past cost function, the number of squares had been removed from original 
          grid to get the current grid. (let call it number_past_squares)
    h(x): the future cost function, an estimated minimum possible number of square 
          that can fit into the current grid (let call it number_future_squares)
          h(x) score is from evaluate the current grid using the 'The deep search algorithms'
          to get the estimated minimum number of squares that can fit into the grid
and f(x) = g(x) + h(x)
The f value at the goal node is the minimum number of square have to be removed to 
reach the goal. In other words, f value of the goal node is the minimum number of 
squares that can fit into the grid.

A* Pseudocode:
function solveAStar(grid)
    g = 0    //current squares in solution
    h = number_of_least_possible_square(grid) * 1.1
    f = g + h
    startNode['grid'] = grid
    startNode['f'] = f
    startNode['solution'] = empty    
    frontier = PiorityQueue()
    frontier.put(startNode)
    while frontier is not empty
        currentNode = the node in frontier having the lowest f value
        if currentNode['grid'] = empty
            return currentNode['solution']
        remove currentNode from frontier
        for each corner in currentNode['grid']
        Find largest square from that corner
        newNode['grid'] = Remove largest square from currentNode['grid']
        newNode['solution'] = currentNode['solution'] add the largest square
        new_g = number of square in new_solution
        new_h = number_of_least_possible_square(new_grid) * 1.1
        newNode['f'] = new_g + new_h
        frontier.put(newNode) 

A* algorithm uses a priority queue of nodes to keep tracking which node will be 
expanded next. A node with lower f score has higher priority. At each step of the 
algorithm, the node with the lowest f(x) value is removed from the priority queue, 
and then apply the operators to generate its child nodes. The f score of each 
child nodes will be calculated, as well as the squares had been removed to get to 
this node. After that, these neighbors are added to the queue. The algorithm 
continues until it reaches a goal node (grid is empty). Goal nodes may be passed 
over multiple times if there remain other nodes with lower f values, as they may 
lead to a shorter path to a goal. Therefor, A* algorithm guarantees to give the 
best solution for the puzzle (fewest number of squares).

------------
Improvement:
------------
There is a frequent case is that when a square is removed (which mean g increase by 1), 
the number_future_squares is decreased by 1 (h decreases by 1). Which leads to the problem 
that many nodes have the same f value (since f = g+h). To break the tie, I slightly 
scale h upwards (by multiple h by 1.1) which will help the A* algorithm prefer to 
expand from the node which has fewer number_future_squares. By doing this, it helps A* 
found the solution faster, saving computation cost and computation time.

