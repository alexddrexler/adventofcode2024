"""Solution for https://adventofcode.com/2025/day/7#part2."""
"""Solution for https://adventofcode.com/2025/day/7."""

from util import read


_TEST = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def solution():
  """Solve the problem."""
  grid = read.read_input_grid()
  tls = {}
  for row in grid:
    if not tls:
      for i, c in enumerate(row):
        if c == "S":
          tls[i] = 1
          break

    new_tls = {}
    for i, count in tls.items():
      new_paths = [i]
      if row[i] == "^":
        new_paths = [i-1, i+1]
      for j in new_paths:
        val = new_tls.get(j) or 0
        new_tls[j] = val + count
    tls = new_tls

  return sum(tls.values())
