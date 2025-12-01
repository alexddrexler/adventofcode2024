"""Global variables, set in run.py."""

VARS = {}


def set_vars(year, day, part):
  VARS["YEAR"] = year
  VARS["DAY"] = day
  VARS["PART"] = part
  VARS["MODULE_COMPONENTS"] = [
      "solutions",
      f"year{year}",
      f"day{day:02}",
      f"part{part}",
  ]
