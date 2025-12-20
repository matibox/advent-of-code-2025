from functools import reduce

def part1(input: 'list[str]'):
  lines = [line.split() for line in input]
  transposed = list(map(list, zip(*lines)))

  total = 0

  for set in transposed:
    numbers = list(map(int, set[:-1]))

    if set[-1] == "*":
      total += reduce(lambda a, b: a * b, numbers)
    else:
      total += reduce(lambda a, b: a + b, numbers)

  return total


def part2(lines: 'list[str]'):
  columns: 'list[list[str]]' = list(reversed(list(map(list, zip(*lines)))))
  total = 0

  sets: 'list[list[list[str]]]' = []
  curr = []

  for i, col in enumerate(columns):
    if i == len(columns) - 1:
      curr.append(col)
      sets.append(curr)
      break

    if len(''.join(col).split()) == 0:
      sets.append(curr)
      curr = []
      continue
    
    curr.append(col)

  for set in sets:
    sign = None
    nums = []

    for cols in set:
      col_num = ''

      for col in cols:
        for ch in col:
          if ch.isnumeric():
            col_num += ch
          elif ch == '*' or ch == '+':
            sign = ch
          else:
            continue
      
      nums.append(int(col_num))

    if sign == "*":
      total += reduce(lambda a, b: a * b, nums)
    else:
      total += reduce(lambda a, b: a + b, nums)

  return total
