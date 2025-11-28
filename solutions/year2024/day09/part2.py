"""Solution for https://adventofcode.com/2024/day/9#part2."""
from solutions.year2024.day09 import part1


# TESTCASES.
# 2333133121414131402, 2858.
# 2833133121414131402, 2184.


def solution():
  """Solve the problem."""
  files, spaces = part1.read_data()
  indexed_files = [(i, size) for i, size in enumerate(files)]
  back_file_index = len(files) - 1
  while back_file_index > 0:
    _, f_size = indexed_files[back_file_index]
    relocated = False
    for i, s_size in enumerate(spaces[:back_file_index]):
      if f_size <= s_size:
        f = indexed_files.pop(back_file_index)
        s = spaces.pop(back_file_index)
        spaces[back_file_index - 1] += s + f_size
        indexed_files.insert(i+1, f)
        spaces[i] = spaces[i] - f_size
        spaces.insert(i, 0)
        relocated = True
        break
    if not relocated:
      back_file_index -= 1

  index = 0
  checksum = 0
  for i, (original_i, size) in enumerate(indexed_files):
    while size > 0:
      checksum += original_i * index
      index += 1
      size -= 1
    space = spaces[i]
    index += space
  return checksum