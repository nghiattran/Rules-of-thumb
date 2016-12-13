# A* algorithm

## Introduction

A* is like Dijkstra’s algorithm in that it can be used to find a shortest path. A* is like Greedy Best-First-Search in that it can use a heuristic to guide itself.

A* algorithm determine next visited node by choosing the lowest value from of a vertice using following function:

```
f(n) = g(n) + h(n)

where:
g(n) represents the exact cost of the path from the starting point to any vertex n 
h(n) represents the heuristic estimated cost from vertex n to the goal.
```

## A*’s Use of the Heuristic

The heuristic can be used to control A*’s behavior:
* At one extreme, if h(n) is 0, then only g(n) plays a role, and A* turns into Dijkstra’s algorithm, which is guaranteed to find a shortest path.
* If h(n) is always lower than (or equal to) the cost of moving from n to the goal, then A* is guaranteed to find a shortest path. The lower h(n) is, the more node A* expands, making it slower.
* If h(n) is exactly equal to the cost of moving from n to the goal, then A* will only follow the best path and never expand anything else, making it very fast. Although you can’t make this happen in all cases, you can make it exact in some special cases. It’s nice to know that given perfect information, A* will behave perfectly.
* If h(n) is sometimes greater than the cost of moving from n to the goal, then A* is not guaranteed to find a shortest path, but it can run faster.
* At the other extreme, if h(n) is very high relative to g(n), then only h(n) plays a role, and A* turns into Greedy Best-First-Search.

## Heuristics for grid maps

Use the distance heuristic that matches the allowed movement:

On a square grid that allows 4 directions of movement, use Manhattan distance (L1).
On a square grid that allows 8 directions of movement, use Diagonal distance (L∞).
On a square grid that allows any direction of movement, you might or might not want Euclidean distance (L2). If A* is finding paths on the grid but you are allowing movement not on the grid, you may want to consider <a href="http://www.redblobgames.com/pathfinding/grids/algorithms.html">other representations of the map</a>.
On a hexagon grid that allows 6 directions of movement, use Manhattan distance adapted to <a href="http://www.redblobgames.com/grids/hexagons/#distances">hexagonal grids</a>.

### Manhattan distance

Look at your cost function and find the minimum cost `D` for moving from one space to an adjacent space. In the simple case, you can set `D` to be 1. The heuristic on a square grid where you can move in 4 directions should be `D` times the Manhattan distance:

```
def heuristic(node):
  dx = abs(node.x - goal.x)
  dy = abs(node.y - goal.y)
  return D * (dx + dy)
```

### Diagonal distance

If your map allows diagonal movement you need a different heuristic. The Manhattan distance for (4 east, 4 north) will be 8⨉D. However, you could simply move (4 northeast) instead, so the heuristic should be 4⨉D2, where D2 is the cost of moving diagonally.

```
def heuristic(node):
  dx = abs(node.x - goal.x)
  dy = abs(node.y - goal.y)
  return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
```

Here we compute the number of steps you take if you can’t take a diagonal, then subtract the steps you save by using the diagonal. There are min(dx, dy) diagonal steps, and each one costs D2 but saves you 2⨉D non-diagonal steps.

### Euclidean distance

If your units can move at any angle (instead of grid directions), then you should probably use a straight line distance:

```
def heuristic(node):
  dx = abs(node.x - goal.x)
  dy = abs(node.y - goal.y)
  return D * sqrt(dx * dx + dy * dy)
```

However, if this is the case, then you may have trouble with using A* directly because the cost function `g` will not match the heuristic function `h`. Since Euclidean distance is shorter than Manhattan or diagonal distance, you will still get shortest paths, but A* will take longer to run:

### Breaking ties

In some grid maps there are many paths with the same length. For example, in flat areas without variation in terrain, using a grid will lead to many equal-length paths. A* might explore all the paths with the same f value, instead of only one.

A quick fix is adjusting `g` or `h` values. 

#### Approach 1

One way to break ties is to nudge the scale of `h` by multiplying it with another deterministic value `p` so that:

```
h = h * (1 + p)
```

The factor `p` should be chosen so that `p` <(minimum cost of taking one step)/(expected maximum path length).

#### Approach 2

When the f values are equal, the comparison function would break the tie by looking at h.

#### Approach 3

Another way to break ties is to add a deterministic random number to the heuristic or edge costs. (One way to choose a deterministic random number is to compute a hash of the coordinates.) This breaks more ties than adjusting `h` as above.

#### Approach 4

Prefer paths that are along the straight line from the starting point to the goal:

```
dx1 = current.x - goal.x
dy1 = current.y - goal.y
dx2 = start.x - goal.x
dy2 = start.y - goal.y
cross = abs(dx1*dy2 - dx2*dy1)
heuristic += cross*0.001
```

#### Approach 5

Construct your A* priority queue so that new insertions with a specific f value are always ranked better (lower) than old insertions with the same f value.

#### Sumary

The above modifications to the heuristic are a “band aid” fix to an underlying inefficiency. You can reduce ties to yield better result:

* Alternate map representations can solve the problem by reducing the number of nodes in the graph. Collapsing multiple nodes into one, or by remove all but the important nodes ([Rectangular Symmetry Reduction](http://aigamedev.com/open/tutorial/symmetry-in-pathfinding/), [Hierarchical pathfinding](http://aigamedev.com/open/tutorial/symmetry-in-pathfinding/))
* Some approaches leave the number of nodes alone but reduce the number of nodes visited. ([Jump Point Search](http://aigamedev.com/open/tutorial/symmetry-in-pathfinding/), [Skip Links](http://theory.stanford.edu/~amitp/GameProgramming/MapRepresentations.html#skip-links))
[Fringe Search](http://cswww.essex.ac.uk/cig/2005/papers/p1039.pdf) solves the problem instead by making node processing fast. Instead of keeping the OPEN set sorted and visiting nodes one at a time, it processes nodes in batches, expanding only the nodes that have low f-values.
## Disclaimer

This documentation is my personal note derived directly from http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html