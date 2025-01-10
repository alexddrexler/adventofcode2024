"""Solution for https://adventofcode.com/2024/day/17."""
import re

from util import read


CONTENT_REGEX = r"Register A: (\d*)\nRegister B: (\d*)\nRegister C: (\d*)\n\nProgram: ([\d,]*)"


def read_state():
  content = read.read_file("day17/input1.txt")
  match = re.match(CONTENT_REGEX, content)
  a, b, c, instruction_str = match.group(1, 2, 3, 4)
  instructions = [int(s) for s in instruction_str.split(",")]
  return int(a), int(b), int(c), instructions


class Comp():
  def __init__(self, a, b, c, instructions):
    self._a = a
    self._b = b
    self._c = c

    self._instructions = instructions
    self._i = 0
    
    self.out = []
  
  def halt(self):
    return self._i >= len(self._instructions)
  
  def read_instruction(self):
    opcode = self._instructions[self._i]
    self._i += 1
    operand = self._instructions[self._i]
    self._i += 1
    return opcode, operand

  
  def run(self):
    while not self.halt():
      opcode, operand = self.read_instruction()
      self.do(opcode, operand)
    return self.out
  
  def do(self, opcode, operand):
    if opcode == 0:  # adv/division.
      self._a = int(self._a / pow(2, self.get_combo(operand)))
    elif opcode == 1:  # bxl/bitwise XOR.
      self._b = self._b ^ operand
    elif opcode == 2:  # bst/mod8.
      self._b = self.get_combo(operand) % 8
    elif opcode == 3:  # jnz/nothing/jump.
      if self._a != 0:
        self._i = operand
    elif opcode == 4:  # bxc/bitwise XOR.
      self._b = self._b ^ self._c
    elif opcode == 5:  # out.
      self.out.append(self.get_combo(operand) % 8)
    elif opcode == 6:  # bdv/division.
      self._b = int(self._a / pow(2, self.get_combo(operand)))
    elif opcode == 7:  # cdv/division.
      self._c = int(self._a / pow(2, self.get_combo(operand)))
    else:
      raise ValueError(f"Invalid opcode: {opcode}")

  
  def get_combo(self, operand):
    if operand > 0 and operand < 4:
      return operand
    if operand == 4:
      return self._a
    if operand == 5:
      return self._b
    if operand == 6:
      return self._c
    raise ValueError(f"Invalid operand: {operand}")


def solution():
  """Solve the problem."""
  a, b, c, instructions = read_state()
  comp = Comp(a, b, c, instructions)
  out = comp.run()
  return ",".join(map(str, out))
