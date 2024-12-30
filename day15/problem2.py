"""Solution for https://adventofcode.com/2024/day/15#part2."""
from day15 import problem1
from util import read


TEST = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def read_grid_and_orders(content=None):
  if content is None:
    content = read.read_file("day15/input1.txt")
  grid_content, order_content = content.split("\n\n")
  grid = []
  for row in grid_content.split("\n"):
    grid_row = []
    for char in row:
      if char == "#":
        grid_row.extend(["#", "#"])
      elif char == "O":
        grid_row.extend(["[", "]"])
      elif char == ".":
        grid_row.extend([".", "."])
      elif char == "@":
        grid_row.extend(["@", "."])
    grid.append(grid_row)

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
      if char == "[":
        boxes.append((i, j))
  return boxes


def can_move(grid, pos, order):
  new_pos = get_new_pos(pos, order)
  char = get_char(grid, new_pos)
  if char == ".":
    return True
  if char == "[":
    return can_move_box(grid, new_pos, order)
  if char == "]":
    return can_move_box(grid, get_new_pos(new_pos, LEFT), order)

  return False  # Invalid space.


def can_move_box(grid, pos, order):
  # We know that pos is a "[" char.
  lchar_pos = pos
  rchar_pos = get_new_pos(pos, RIGHT)
  if order == LEFT:
    return can_move(grid, lchar_pos, LEFT)
  elif order == RIGHT:
    return can_move(grid, rchar_pos, RIGHT)
  else:  # UP and DOWN.
    return can_move(grid, lchar_pos, order) and can_move(grid, rchar_pos, order)


def move(grid, pos, order):
  if not can_move(grid, pos, order):
    return pos
  new_pos = get_new_pos(pos, order)
  char = get_char(grid, new_pos)
  if char == ".":
    update(grid, pos, new_pos)
  elif char == "[":
    move_box(grid, new_pos, order)
    update(grid, pos, new_pos)
  elif char == "]":
    move_box(grid, get_new_pos(new_pos, LEFT), order)
    update(grid, pos, new_pos)
  return new_pos


def move_box(grid, pos, order):
  lchar_pos = pos
  rchar_pos = get_new_pos(pos, RIGHT)
  if order == LEFT:
    move(grid, lchar_pos, LEFT)
    update(grid, rchar_pos, lchar_pos)
  elif order == RIGHT:
    move(grid, rchar_pos, RIGHT)
    update(grid, lchar_pos, rchar_pos)
  else:  # UP and DOWN.
    move(grid, lchar_pos, order)
    move(grid, rchar_pos, order)


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
