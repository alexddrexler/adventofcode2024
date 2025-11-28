"""Main file for handling Advent of Code actions.

When run, this program takes two inputs, either directly from the command line
or via interactive prompt if not provided.
"""
import argparse
import importlib
import os

from util import global_vars


SOLUTION_BOILERPLATE_TEMPLATE = """\"\"\"Solution for {link}.\"\"\"


def solution():
  \"\"\"Solve the problem.\"\"\"
  return None
"""


def parse_args() -> tuple[int, int, int]:
  parser = argparse.ArgumentParser(prog="AdventOfCodeRunner")
  parser.add_argument("year", type=int)
  parser.add_argument("day", type=int)
  parser.add_argument("part", type=int, nargs="?", default=1)
  args = parser.parse_args()
  return(int(args.year), int(args.day), int(args.part))


def _get_or_create_module() -> str:
  pkg_path = os.path.dirname(__file__)
  module_components = global_vars.VARS["MODULE_COMPONENTS"]

  subdirs = module_components[:-1]
  for subdir in subdirs:
    pkg_path = os.path.join(pkg_path, subdir)
    if not os.path.exists(pkg_path):
      print(f"Creating {pkg_path}")
      # Create directory.
      os.makedirs(pkg_path)
      # Add init file.
      open(os.path.join(pkg_path, "__init__.py"), "x")

  file_basename = module_components[-1]
  file_path = os.path.join(pkg_path, f"{file_basename}.py")
  if not os.path.exists(file_path):
    print(f"Creating {file_path}")
    year = global_vars.VARS["YEAR"]
    day = global_vars.VARS["DAY"]
    part = global_vars.VARS["PART"]
    link = f"https://adventofcode.com/{year}/day/{day}"
    if part > 1:
      link += f"#part{part}"
    with open(file_path, "a") as solution_file:
      solution_file.write(SOLUTION_BOILERPLATE_TEMPLATE.format(link=link))

  return ".".join(module_components)


def run(year: int, day: int, part: int):
  global_vars.set_vars(year, day, part)
  module_name = _get_or_create_module()
  module = importlib.import_module(module_name)

  print(module.solution())
  

def main():
  year, day, part = parse_args()
  print(f"Requested solution {year}.{day}.{part}")
  run(year, day, part)


main()
