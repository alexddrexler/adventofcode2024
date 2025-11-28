"""Solution for https://adventofcode.com/2024/day/15."""
from util import read


TEST_S = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

TEST_L = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def read_grid_and_orders(content=None):
  if content is None:
    content = read.read_input()
  grid_content, order_content = content.split("\n\n")
  grid = [list(row) for row in grid_content.split("\n")]
  orders = []
  for char in order_content:
    if char == "^":
      orders.append(UP)
    elif char == ">":
      orders.append(RIGHT)
    elif char == "v":
      orders.append(DOWN)
    elif char == "<":
      orders.append(LEFT)
  return grid, orders


def find_robot(grid):
  for i, row in enumerate(grid):
    for j, char in enumerate(row):
      if char == "@":
        return (i, j)


def find_boxes(grid):
  boxes = []
  for i, row in enumerate(grid):
    for j, char in enumerate(row):
      if char == "O":
        boxes.append((i, j))
  return boxes


def move(grid, pos, order):
  new_pos = get_new_pos(pos, order)
  char = get_char(grid, new_pos)
  if char == ".":
    update(grid, pos, new_pos)
    return new_pos  # Moved into empty position.

  if char == "O" and move(grid, new_pos, order) != new_pos:
    update(grid, pos, new_pos)
    return new_pos

  return pos  # Could not move.


def update(grid, old, new):
    set_char(grid, new, get_char(grid, old))
    set_char(grid, old, ".")



def get_char(grid, pos):
  i, j = pos
  return grid[i][j]


def set_char(grid, pos, char):
  i, j = pos
  grid[i][j] = char


def get_new_pos(pos, order):
  i, j = pos
  if order == UP:
    return (i-1, j)
  if order == RIGHT:
    return (i, j+1)
  if order == DOWN:
    return (i+1, j)
  if order == LEFT:
    return (i, j-1)


def print_grid(grid):
  for row in grid:
    row_str = ""
    for char in row:
      if char == ".":
        row_str += " "
      else:
        row_str += char
    print(row_str)


def solution():
  """Solve the problem."""
  grid, orders = read_grid_and_orders()
  pos = find_robot(grid)
  for order in orders:
    pos = move(grid, pos, order)

  boxes = find_boxes(grid)
  coord_sum = 0
  for i, j in boxes:
    coord_sum += 100 * i + j
  return coord_sum
