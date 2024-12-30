"""Main file for handling Advent of Code actions.

When run, this program takes two inputs, either directly from the command line
or via interactive prompt if not provided.
"""
import argparse
import importlib
import os


PROBLEM_BOILERPLATE_TEMPLATE = """\"\"\"Solution for {link}.\"\"\"


def solution():
  \"\"\"Solve the problem.\"\"\"
  return None
"""


def parse_day_and_problem() -> tuple[int, int]:
  parser = argparse.ArgumentParser(prog="AdventOfCodeRunner")
  parser.add_argument("day")
  parser.add_argument("problem")
  args = parser.parse_args()
  return(int(args.day), int(args.problem))


def _get_or_create_day_pkg(day: int) -> str:
  pkg_name = f"day{day}"
  pkg_path = os.path.join(os.path.dirname(__file__), pkg_name)
  if not os.path.exists(pkg_path):
    # Create directory.
    os.makedirs(pkg_path)
    # Add init file.
    open(os.path.join(pkg_path, "__init__.py"), "x")
  return pkg_path


def _get_or_create_problem_file(day: int, problem: int) -> str:
  day_pkg_path = _get_or_create_day_pkg(day)
  file_name = f"problem{problem}.py"
  file_path = os.path.join(day_pkg_path, file_name)
  if not os.path.exists(file_path):
    print(f"Creating {file_path}.")
    link = f"https://adventofcode.com/2024/day/{day}"
    if problem > 1:
      link += f"#part{problem}"
    with open(file_path, "a") as problem_file:
      problem_file.write(PROBLEM_BOILERPLATE_TEMPLATE.format(link=link))
  return file_path


def run(day: int, problem: int):
  problem_file = _get_or_create_problem_file(day, problem)
  absdir, filename = os.path.split(problem_file)
  module_name = os.path.basename(absdir)
  module_name += "." + filename[:-3]  # Drop "".py"
  module = importlib.import_module(module_name)
  print(module.solution())
  

day, problem = parse_day_and_problem()
print(f"Requested day{day}.problem{problem}")
run(day, problem)