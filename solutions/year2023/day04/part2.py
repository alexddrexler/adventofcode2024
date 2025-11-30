"""Solution for https://adventofcode.com/2023/day/4#part2."""

from util import read


def solution():
  """Solve the problem."""
  data = read.read_input()
  cards = data.split("\n")
  scratchers = []
  for card in cards:
    card = card[9:].strip()
    winner_str, have_str = card.split("|")
    parsed_nums = []
    for num_str in [winner_str, have_str]:
      num_str = num_str.strip()
      nums = []
      cur_num = ""
      for c in num_str:
        if c.isnumeric():
          cur_num += c
        else:
          if cur_num:
            nums.append(int(cur_num))
          cur_num = ""
      if cur_num:
        nums.append(int(cur_num))

      parsed_nums.append(nums)
    winners, haves = parsed_nums
    count = 0
    for have in haves:
      if have in winners:
        count += 1
    scratchers.append((count, 1))
  tot = 0
  for pos, (win_count, times) in enumerate(scratchers):
    print(pos)
    i = 0
    while i < times:
      tot += 1
      j = 0
      while j < win_count:
        c, t = scratchers[pos + j + 1]
        scratchers[pos + j + 1] = (c, t+1)
        j += 1
      i += 1

  return tot
