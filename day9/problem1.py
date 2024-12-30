"""Solution for https://adventofcode.com/2024/day/9."""
from util import read


def read_data(content=None):
  if content is None:
    content = read.read_file("day9/input1.txt")
  files = []
  spaces = []
  is_file = True
  for char in content:
    size = int(char)
    if is_file:
      files.append(size)
    else:
      spaces.append(size)
    is_file = not is_file
  if len(spaces) < len(files):
    spaces.append(0)
  return (files, spaces)


def get_checksum(files, spaces):
  checksum = 0
  index = 0
  front_f = 0
  back_f = len(files) - 1
  rem_back_f = files[back_f]
  while front_f < back_f:
    file_size = files[front_f]
    for _ in range(file_size):
      checksum += (index * front_f)
      index += 1
    space_size = spaces[front_f]
    for _ in range(space_size):
      if rem_back_f < 1:
        back_f -= 1
        rem_back_f = files[back_f]
      checksum += (index * back_f)
      index += 1
      rem_back_f -= 1
    front_f += 1
  if front_f == back_f:
    while rem_back_f > 0:
      checksum += (index * back_f)
      index += 1
      rem_back_f -= 1
  return checksum


def solution():
  """Solve the problem."""
  files, spaces = read_data()
  return get_checksum(files, spaces)
