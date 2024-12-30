"""Solution for [insert link]."""
from day5 import problem1


def reorder(update, rules):
  valid = False
  while not valid:
    if single_pass(update, rules):
      valid = True

def single_pass(update, rules):
  rev_update = update[::-1]
  for i, num in enumerate(rev_update):
    bombs = rules[num]
    ind = len(update) - 1 - i
    for j, other_num in enumerate(update[:ind]):
      if other_num in bombs:
        update.pop(ind)
        update.insert(j, num)
        return False
  return True


def solution():
  """Solve the problem."""
  rules, updates = problem1.read_input()
  invalid_updates = [
      update for update in updates if not problem1.is_valid(update, rules)
  ]
  middle_sum = 0
  for update in invalid_updates:
    reorder(update, rules)
    middle_sum += update[int(len(update) / 2)]

  return middle_sum
