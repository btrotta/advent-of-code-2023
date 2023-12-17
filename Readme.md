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

## Day 15
This is a shortest path problem so we can use Dijkstra's algorithm. However, because of the constraints on distance 
travelled in each step, and on changing direction, the graph is slightly more complicated. Define a node of the graph 
to be a tuple `(position, direction)` where direction is the direction (vertical or horizontal, indicated by `"v"` or `"h"`) 
that was travelled to arrive at that position. The edges of the graph connect points having different values for `direction`, and where 
the difference in position is between 1 and 3 (part a) or between 4 and 10 (part b). The edge weight is given by the sum of 
the array values between the current and new positions (excluding the current position).
