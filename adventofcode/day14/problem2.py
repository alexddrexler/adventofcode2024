"""Solution for https://adventofcode.com/2024/day/14#part2.

Ran this manually and observed output until the tree was visible.
Grid view at second 6888:
+-----------------------------------------------------------------------------------------------------+
|                                       1                                                             |
|                    1                                                                                |
|              1                                       1                                              |
|                               1                                                                     |
|                                                                                1                    |
|        1                                           1                                1               |
|                         1                                     1                                1    |
|                                                                           1                         |
|                                                                                                     |
|   1                    1                                       1                              1   1 |
|                                                                                1                    |
|   1                 1  1                                                                            |
|         1      1                          1                                             1           |
|                                                                                                     |
|                    1                                                                                |
|               1                        1                                                     1      |
|            1                   1                                                            1       |
|             1                    1                                                                  |
|                                                                                                    1|
|                                 1111111111111111111111111111111                                     |
|              1                  1                             1                                     |
|                                 1                             1                                     |
|                          1      1                             1                                     |
|                      1     1    1                             1                                1    |
|                   1             1              1              1                                     |
|               1      1          1             111             1                                     |
|           1                     1            11111            1     1                               |
|                                 1           1111111           1                         1      1    |
|                                 1          111111111          1                    1                |
|                                 1            11111            1                        1            |
|                          1      1           1111111           1      1                      1       |
|                                 1          111111111          1                                     |
|                                 1         11111111111         1                            1        |
|            1                    1        1111111111111        1                                     |
|          1                      1          111111111          1    1                                |
|                                 1         11111111111         1                                     |
|                                 1        1111111111111        1                                     |
|                                 1       111111111111111       1                                     |
|                                 1      11111111111111111      1                          1          |
|  1                1             1        1111111111111        1                                 1   |
|                           1     1       111111111111111       1                                     |
|     1                           1      11111111111111111      1                                     |
|                                 1     1111111111111111111     1                                     |
|       1             1           1    111111111111111111111    1                  1                  |
|                                 1             111             1                                     |
|                               1 1             111             1                                     |
|                             1   1             111             1                                     |
|                                 1                             1                           1         |
|                                 1                             1                                     |
|                                 1                             1                 1                   |
|                                 1                             1        1                          1 |
|                                 1111111111111111111111111111111                                     |
|                                                                              1                      |
|                    1                                                                                |
|     1                                                                                              1|
|                          1    1          1              1      1        1                      1    |
|                                                                                                     |
|                                               1                     1                               |
|                                                                                                     |
|                                                                                                     |
|       1                                                                                             |
|                                                                                                     |
|               1                                                                             1       |
|                                                                                                     |
|                                   1                                                                 |
|                                                                                        1            |
|                                                    1                                                |
|                            11                                                                       |
|                         1                                                                           |
|                                                                                                     |
|                     1                                                     1                      1  |
|             1                                        1                                              |
|       1                                                                                             |
|                                                                                                  1  |
|                                                                                                     |
|         1                                                       1                         1         |
|                                                                                                     |
|                                                                               1                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|         1                                                                                           |
|                            1            1           1                        1                      |
|       1                  1     1                         1                       1                  |
|                                                                                          1     1    |
|                             1                                              1                        |
|                                                                                                     |
|      1               1                                                 1                            |
|                                                                                                     |
|                 1          11                                                                       |
|                                                                                                     |
|                                                 1                                                   |
|                                                                                          1        1 |
|                                                                             1                       |
|                                                              1                                      |
|                       1                       1                                                     |
|             1                                               1                                       |
| 1                             1                                                                     |
|             1             1         1                                                               |
|                           1     1              1                               1                    |
|               1                                                                                     |
|                               1                                                                     |
|                            1                                            1                           |
+-----------------------------------------------------------------------------------------------------+
"""
from day14 import problem1


def print_grid(grid):
  print("+" + "-" * 101 + "+")
  for row in grid:
    row_str = "|"
    for val in row:
      if val == 0:
        row_str += " "
      else:
        row_str += str(val)
    row_str += "|"
    print(row_str)
  print("+" + "-" * 101 + "+")


def solution():
  """Solve the problem."""
  robots = problem1.read_robots()
  seconds = 0
  while True:
    grid = []
    for _ in range(103):
      grid.append([0] * 101)
    printable = False
    for robot in robots:
      x, y = problem1.get_pos(robot, seconds)
      grid[y][x] += 1
    for row in grid:
      if sum(row) > 20:
        printable = True
    print(f"SECONDS: {seconds}")
    if printable:
      print_grid(grid)
      input()
    seconds += 1
  return None
