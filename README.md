The task from Yandex.Contest.

## Intersections of rectangles
Given a set of rectangles on a plane with sides parallel to the coordinate axes.
For each rectangle, it is necessary to calculate the number of other rectangles with which this rectangle intersects.

Definition: Two rectangles intersect if there is a region of nonzero area belonging to both rectangles. 
The external touch on the side forms a common area of zero area, so it is not an intersection.

### Input format
The first line contains an integer ***n***
<span class="tex-math-text"> (1 ≤ n ≤ 100 000)</span> — the number of rectangles.
The following ***n*** lines contain descriptions of rectangles: 
integers 
<span class="tex-math-text">(-10<sup>9</sup> ≤ x<sub>L</sub>, y<sub>L</sub>, x<sub>R</sub>, y<sub>R</sub> ≤ 10<sup>9</sup>; x<sub>L</sub> &lt; x<sub>R</sub>; y<sub>L</sub> &lt; y<sub>R</sub>)</span> — coordinates of the lower left and upper right corners.

### Output format
In a single line, print ***n*** numbers separated by a space: the ***i***-th number is equal to the number of rectangles 
intersecting with the ***i***-th rectangle in the input order.

## Example

Input
```
6
-2 -4 2 2
-2 -4 0 -1
-2 -1 0 2
0 -4 2 -1
0 -1 2 2
-1 -2 1 0
```
Output
```
5 2 2 2 2 5 
```
