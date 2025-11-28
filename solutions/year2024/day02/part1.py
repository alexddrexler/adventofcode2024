"""Solution for https://adventofcode.com/2024/day/2."""
from util import read


def read_reports() -> list[list[int]]:
  input_content = read.read_input()
  reports = []
  for row in input_content.split("\n"):
    reports.append([int(i) for i in row.split(" ")])
  return reports


def solution():
  """Solve the problem."""
  reports = read_reports()
  safe_count = 0
  for report in reports:
    if len(report) < 2:
      safe_count += 1
      continue
    inc = report[0] < report[1]
    prev_level = None
    is_safe = True
    for level in report:
      if prev_level is None:
        prev_level = level
        continue
      diff = level - prev_level
      if abs(diff) > 3 or abs(diff) < 1:
        is_safe = False
        break
      if inc and diff < 0:
        is_safe = False
        break
      if not inc and diff > 0:
        is_safe = False
        break
      prev_level = level
    if is_safe:
      safe_count += 1
  return safe_count