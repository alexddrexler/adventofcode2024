"""Common util functions for printing to terminal."""


def print_char_grid(grid: list[list[str]], char_mapping: dict[str, str] = dict()) -> None:
  """Prints a rectangular grid of characters."""
  print("+" + "-" * len(grid[0]) + "+")
  for row in grid:
    row_str = "|"
    for char in row:
      out = char_mapping.get(char)
      if out is None:
        out = char
      row_str += out
    print(row_str + "|")
  print("+" + "-" * len(grid[0]) + "+")
