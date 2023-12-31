# Advent of code 2023

Python solutions to Advent of Code 2023.

## Day 1

For part a, iterate over the line forwards and backwards until the first integer is found.
For part b, first reverse the line and the spelled words to efficiently iterate backwards.

## Day 2
Iterate over the lines. For part a, use a function to check each line so we can return early if the check fails.

## Day 3
For part a, iterate over the symbols, add each adjacent number to the total,
and then replace its digits with `.` to avoid double-counting. 
For part b, for each `*` symbol, make a list of all the numbers adjacent to it, and calculate gear ratio when there are 
only 2. It is not necessary to replace numbers with `.` in this case.

## Day 4
Part a is straightforward. For part b, maintain an array `num_copies` of the number of copies of each card (starting with all 
values equal to 1). When processing line `i`, if `n` matches are found, increment the number of copies of the next `n` cards 
by `num_copies[i]`

## Day 5
For part a, we can just iterate through all the maps for each seed. For part b, there are too many seeds for this 
to be feasible. Since each mapping just shifts a range of numbers, we know that the list of possible seeds can 
be divided into a relatively small number of ranges, and within each range the lower end of the range will 
correspond to the lowest location number. To identify the ranges, work backwards through the mappings, and for 
each transformation find its inverse image.

## Day 6
For part a, check all the possible times. For part b, this is slow. A more efficient solution is to note that the 
distance travelled is a quadratic function of the charging time, and use the quadratic formula to find the 
range where distance travelled is greater than the record.

## Day 7
For both parts, we need functions to return the strength of a given hand, and the rank of a single card. Once 
we have these, we just sort using these keys. To calculate the strength of a hand, use `collections.Counter` to 
count the multiple occurences of cards. For part b, modify the counter to allocate multiples of "J" to the 
next-most-common card.

## Day 8
For part a, just follow the path. For part b, note that since there are only a finite number of vertices and the 
list of directions is finite, all paths repeat after some time. For each starting node, follow the directions until 
the path repeats, keeping track of the lengths of sub-paths that end in a valid end node. (The path will repeat when 
the same state recurs, where state is defined by the current node and the position in the list of directions.) It turns
out that, for each starting node, only one sub-path ends in a valid end node, and its distance from the 
start is equal to the cycle length for that starting node (this is by design of the problem, it's not true in general). 
Therefore it suffices to find the least common multiple of all the cycle lengths.

## Day 9
For part a, iterate over the array taking diffs until the result is all zeros. Keep track of the last element at each 
step. Then, iterate backwards over the list of last elements. At each step, the value filled at the end of the previous 
line gets added to the last element of the line above. Part b is similar, but subtract from the first element instead.

## Day 10
For part a, enumerate the allowed directions given the current character of the array, and the allowed next characters 
for any direction. Use this to find the valid path. For part b, first replace the ``S`` character by 
its pipe shape character, which we can determine by checking its connecting pipes. Then, iterate over the rows and, for each row, 
iterate over the columns and count the number of vertical loop boundaries (``|``) crossed: if it's an odd number, 
we are inside the loop. A pair of ``F`` followed later by ``J``, or ``L`` followed later by ``7`` also counts as a
vertical boundary. 

## Day 11
For part a, we can just build the expanded array. The distance between any two galaxies is the sum of the vertical 
and horizontal distances. For part b, the array is too large to work with, so instead build a lookup table 
that maps each row of the original array to its row index in the expanded array, and similarly for the columns. Use these 
tables to convert the galaxy coordinates to their equivalents in the expanded array.

## Day 12
This is a dynamic programming problem. For the ith group, for each valid starting position for this group, 
calculate the number of valid arrangements that have the ith group in this position. This is easy for the first group, 
and for subsequent groups, we can use the results of the previous step. When calculating the range of possible starting 
positions to check, use the problem conditions to constrain the range. There must be enough room at the end to fit 
all the remaining groups; there must be a space of at least 1 after the end of the previous group; and the gaps between 
groups (and before/after all the groups) must not contain broken machines.

## Day 13
Iterate over the possible reflection axes. For part a, check whether the left and right parts are exactly the 
same; for part b, check whether the sum of differences equals 1.

## Day 14
For part a, iterate over the columns, and for each column, iterate over rows, keeping track of the northernmost empty
space that a rock could roll to. For part b, write functions to do similar iterations for all the directions. Since 
there are only finitely many rocks and spaces, the state of the rocks must repeat after some number of cycles. Therefore 
we do not need to simulate all the cycles.

## Day 15
Part a is straightforward. For part b, represent each box by a list containing pairs `(label, focal_length)`.

## Day 16
Use a stack to store a list of the beams that need to be followed (described by current position and direction). Use a 
set to keep track of energized points. Initialize the stack with the starting position and direction. 
While the stack is non-empty, pop the top element and follow it until it changes direction or splits. Then, add the 
new position(s) and direction(s) to the stack. Use a set to keep track of visited states (i.e. tuples `(position, direction)`), to 
avoid getting stuck in an infinite loop.

## Day 17
This is a shortest path problem so we can use Dijkstra's algorithm. However, because of the constraints on distance 
travelled in each step, and on changing direction, the graph is slightly more complicated. Define a node of the graph 
to be a tuple `(position, direction)` where direction is the direction (vertical or horizontal, indicated by `"v"` or `"h"`) 
that was travelled to arrive at that position. The edges of the graph connect points having different values for `direction`, and where 
the difference in position is between 1 and 3 (part a) or between 4 and 10 (part b). The edge weight is given by the sum of 
the array values between the current and new positions (excluding the current position).


## Day 18
For part a, calculate the coordinates, and then consider a rectangle that exceeds the coordinates by 1 in every direction.
Starting with the upper-left corner of the rectangle, we can use depth-first search to find the points that are in the 
rectangle but outside the lagoon. Subtract the number of such points from the area of the rectangle to get the area of 
the lagoon. Part b is similar, except that the coordinates are too large to explicitly enumerate the border of the lagoon.
However, since the coordinates of the corners are relatively few, we can use an approach similar to that in Day 11, 
where we project them to smaller coordinates and use a lookup table to find the area of each volume in the original
(large) coordinates.

## Day 19
Represent the sequence of operations as a directed graph. There are no loops, so the graph is a tree. For part a, 
traverse the tree for all the given ratings. For part b, use depth-first search to traverse the tree, and during the 
traversal label each node with its maximum and minimum values for each category. When reaching an acceptance leaf node, 
calculate the product of the category ranges and add to the total number of rating combinations.

## Day 20
For part a, simulate the button presses. For each press, use a queue to keep track of the sent pulses and process them 
first-in first-out. For part b, this is hard to solve in general, because there are too many possible states of the 
system (`2^n`, where `n` is the number of flip-flops). But by plotting the graph we can see that it consists of 4 
parts that are disjoint apart from their inputs from the broadcaster and their outputs. The output of each subgraph is then inverted 
and combined in a conjunction module with outputs to the final `rx` node. Therefore, it suffices to find the minimum number of 
button presses such that all subgraphs output a low signal. Each subgraph contains a relatively small number of nodes, 
so it's possible to enumerate all the possible states, and check when the cycle of states repeats. For each subgraph, 
it turns out that the cycle repeats back to the very first state (i.e. before any button presses), and that a low pulse 
is sent during the last button press of the cycle. Therefore the answer is the lowest common multiple of all the cycle lengths.

## Day 21
First order the bricks in increasing order of lowest edge. Then simulate the falling, using a set to keep track of 
filled locations and a dictionary to map each filled location to its corresponding brick. Then, for each brick, use
this dictionary to determine the set of bricks above and below it and record this information in dictionaries. For part 
a, a brick will cause other bricks to fall if, for each brick above it, there is only one brick below. For part b, 
for each brick use depth-first search to determine the number of bricks above it that will fall.

## Day 22
For part a, use breadth-first search. For part b, note that a point is reachable in exactly the target number of steps 
if it is reachable in fewer steps, and the shortest distance to reach it has the same parity as the target. Also, note 
that (in the non-test data), the central row and column are empty, as are the first and last rows and columns. Therefore, 
to travel from the centre square to a point in any other square, there is a minimal-length path that travels only along 
the central vertical or horizontal columns, or only along borders, apart from the first and last square. Thus we can 
find a diamond-shaped area of squares for which all points within them are reachable in the target number of steps. Then, 
find the distance to travel from the boundary of this area to any other point.

## Day 23
For part a, use breadth-first search. For part b, the number of possible parts becomes very large, but we can speed up 
the search with some optimizations. First, where there is a series of edges of degree 2, replace with a single edge. 
This reduces the number of nodes and edges dramatically. Secondly, when checking the paths, maintain a dictionary that 
maps the pair consisting of the sorted tuple of path edges, and the last path, to the maximum distance of the path. This 
allows us to find the optimal order given a set of path edges and an end point.

## Day 24
For part a, the path crossing point (if any) is the solution to a pair of simultaneous equations. For part b, I used 
the solution outlined here: https://www.reddit.com/r/adventofcode/comments/18pum3b/comment/ker6qsa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
The unknowns are the rock's initial position and its velocity, which are described by 6 numbers. Given any hailstone, 
for each x, y, z dimension, we can get an equation relating its initial coordinates and velocity in that dimension,
the unknown coordinates and velocity in the same dimension, and the intersection time. We get 3 such equations, for the 
3 dimensions, and t is the same in each case. So we can combine these to get 3 equations, containing the x and y, or the 
x and z, or the y and z, coordinates. The equations are not linear in the unknown variables. But if we do the same process for a different 
point, and subtract the corresponding equations, the nonlinear terms cancel. With the original point, plus 2 additional ones, 
we can get 6 simultaneous linear equations and solve for the 6 unknowns. Because the coordinates of the matrices are 
too large to be represented by 64-bit floating point numbers, we cannot use the numpy solver. Instead, we can calculate 
the solution by using Cramer's rule and using the Laplace expansion to calculate the determinants.

## Day 25
To find the edges to cut, check each edge `(x, y)` as follows. Find the shortest path `p` from `x` to `y` excluding the `(x, y)` 
edge. (There must be such a path, because we know we can cut any 2 edges without disconnecting the graph.) Now, for 
each edge `(r, s)` on `p`, find the shortest path `q` from `x` to `y`, excluding both  `(x, y)`  and `(r, s)` edges. (Again, 
such a path must exist.) Finally, check each edge `(u, v)` on `q` in the same way. If no path exists from `x` to `y` 
that excludes the edges `(x, y), (r, s)` and `(u, v)`, then these are the edges we must cut.
