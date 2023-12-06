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
ranges where distance travelled is greater than the record.
