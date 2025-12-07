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
  beams = set()
  splits = 0
  for row in grid:
    if not beams:
      for i, c in enumerate(row):
        if c == "S":
          beams.add(i)
          break

    new_beams = set()
    for i in beams:
      if row[i] == "^":
        new_beams.add(i-1)
        new_beams.add(i+1)
        splits += 1
      else:
        new_beams.add(i)
    beams = new_beams

  return splits
