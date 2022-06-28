A common interview task and my version of its solution.

## Problem
Implement the Rectangle class describing a rectangle aligned along the axes. Write a has_intersection(r1, r2) 
function that returns True if two rectangles intersect/overlap, i.e. there are common points. Write tests for 
positive and negative scenarios.

## Solution
The logic is based on Separating Axis Theorem. To check if two rectangles intersect, you need to pass their coordinates of each of them in the following form:
```
    first_rect = Rectangle(x_min, y_min, x_max, y_max)
    second_rect = Rectangle(x_min, y_min, x_max, y_max)
```
where `x_min, y_min` are the coordinates of the lower left corner,
and `x_max, y_max` - the upper right corner.

