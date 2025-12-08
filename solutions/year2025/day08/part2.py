"""Solution for https://adventofcode.com/2025/day/8#part2."""

import math

from util import read


_TEST = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


class Pair(object):

  def __init__(self, point_a, point_b):
    self.points = [point_a, point_b]
    self.distance = get_distance(point_a, point_b)


def get_distance(point_a, point_b):
  x_a, y_a, z_a = point_a
  x_b, y_b, z_b = point_b
  return math.sqrt(pow(x_a - x_b, 2) +
                   pow(y_a - y_b, 2) +
                   pow(z_a - z_b, 2))


def solution():
  """Solve the problem."""
  data = read.read_input()
  # data = _TEST
  rows = data.split("\n")
  points = []
  for row in rows:
    x, y, z = row.split(",")
    points.append((int(x), int(y), int(z)))

  pairs = []
  for i, point_a in enumerate(points):
    for j, point_b in enumerate(points[i+1:]):
      pairs.append(Pair(point_a, point_b))

  pairs.sort(key=lambda p: p.distance, reverse=True)
  circuits = []

  while True:
    if not pairs:
      break
    pair = pairs.pop()
    point_a, point_b = pair.points
    c_a = None
    c_b = None
    for c, circuit in enumerate(circuits):
      if point_a in circuit:
        c_a = c
      if point_b in circuit:
        c_b = c
      if c_a is not None and c_b is not None:
        break

    if c_a is None and c_b is None:
      circuits.append([point_a, point_b])
    elif c_a is None:
      circuits[c_b].append(point_a)
    elif c_b is None:
      circuits[c_a].append(point_b)
    elif c_a != c_b:
      circuits[c_a].extend(circuits[c_b])
      del circuits[c_b]

    if len(circuits) == 1 and len(circuits[0]) == len(points):
      return point_a[0] * point_b[0]

  return None
