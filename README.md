# Packman Greedy Search

A terminal simulation of a Packman-style game in Python (NumPy) that demonstrates **greedy search**. Packman starts at a random cell on a 10x10 grid and automatically collects every pizza by always moving toward the **nearest** one.

## What is greedy search?

Greedy search is a strategy that makes the **locally best choice at every step**, without planning the whole route in advance. Here, "best" means "closest":

1. Look at all remaining pizzas and pick the one with the smallest distance to Packman.
2. Look at the neighbouring cells Packman can step into.
3. Take the step that brings Packman closest to the chosen pizza.
4. Repeat until no pizzas are left.

Packman never looks ahead and never backtracks. It just keeps asking: *"What is the closest pizza, and which single step gets me nearer to it?"*

## Distance: Manhattan distance

Packman moves in 4 directions only (up, down, left, right), so the distance between two cells is the Manhattan distance:

```
distance = |row1 - row2| + |col1 - col2|
```

This equals the exact number of steps needed to reach the target on an empty grid.

## Step-by-step example

```
Packman at (2, 2)      Pizzas at (2, 5), (7, 1), (0, 0)

Distances:  (2, 5) -> 3     (7, 1) -> 6     (0, 0) -> 4
Nearest:    (2, 5)

Possible moves: (1,2) (3,2) (2,1) (2,3)
Distance of each move to (2, 5):  4  4  5  2
Best move:  (2, 3)
```

Packman steps to `(2, 3)`, then repeats the same process until it eats the pizza at `(2, 5)`, then picks the next nearest pizza, and so on.

## How the code is organised

| Function | Purpose |
|----------|---------|
| `get_possible_moves(position)` | Returns the valid neighbouring cells (stays inside the board) |
| `calculate_distances(current, targets)` | Manhattan distance from one cell to a list of cells |
| `get_nearest_pizza(position)` | The remaining pizza with the smallest distance to Packman |
| `game(position)` | Main loop: choose target, choose best move, update board, eat pizza |

## Board values

| Value | Meaning |
|-------|---------|
| `0`   | Empty cell |
| `11`  | Packman |
| `99`  | Pizza |

## Requirements

- Python 3.8+
- NumPy

```bash
pip install numpy
```

## Run

```bash
python packman.py
```

Each step prints Packman's position, the target pizza, the updated board, the pizzas left and the number eaten. A `Pizza Eaten!` message appears whenever Packman reaches one.

## Configuration

Edit the constants at the top of `packman.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `N`, `M` | `10` | Board rows and columns |
| `number_of_pizzas` | `5` | How many pizzas to place |
| `packman_value` | `11` | Number that represents Packman on the board |
| `pizza_value` | `99` | Number that represents a pizza on the board |

## Limitations

- **Not always optimal.** Greedy choices can produce a longer total path than the best possible order of pizzas (this is the same idea as the nearest-neighbour heuristic for the Travelling Salesman Problem).
- **Ties are broken arbitrarily.** If two pizzas or two moves have the same distance, the first one found is used.
- **No obstacles.** The grid is empty, so Manhattan distance is always reachable. With walls you would need a pathfinding algorithm such as BFS or A*.
