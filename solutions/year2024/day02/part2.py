"""Solution for https://adventofcode.com/2024/day/2#part2."""
from solutions.year2024.day02 import part1


def is_report_safe(report: list[int], inc: bool, cropped: bool = False) -> bool:
  if len(report) < 2:
    return True
  for i in range(1, len(report)):
    if is_level_safe(report, i, inc):
      continue
    print(report)
    if cropped:
      return False
    cropped_reports = [
        report[:i-1] + report[i:],  # Drop i-1.
        report[:i] + report[i+1:]   # Drop i.
    ]
    return any([is_report_safe(r, inc, cropped=True) for r in cropped_reports])
  return True


def is_level_safe(report, l, inc):
  if inc:
    higher = l
    lower = l - 1
  else:
    higher = l - 1
    lower = l
  diff = report[higher] - report[lower]
  print(diff)
  return diff <= 3 and diff >= 1


def solution():
  """Solve the problem."""
  reports = part1.read_reports()
  safe_count = 0
  for report in reports:
    is_safe = any([
        is_report_safe(report, inc=True),
        is_report_safe(report, inc=False),
    ])
    if is_safe:
      safe_count += 1
  return safe_count