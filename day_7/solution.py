from functools import reduce

def part1(lines: 'list[str]'):
  splits = 0
  state = []

  for ch in lines[0]:
    if ch == 'S':
      state.append(1)
    else:
      state.append(0)

  for line in lines[1:]:
    for x, ch in enumerate(line):
      if ch == '^' and state[x] == 1:
        splits += 1
        state[x] = 0
        state[x - 1] = 1
        state[x + 1] = 1

  return splits


def part2(lines: 'list[str]'):
  state = []

  for ch in lines[0]:
    if ch == 'S':
      state.append(1)
    else:
      state.append(0)

  for line in lines[1:]:
    for x, ch in enumerate(line):
      if ch == '^' and state[x] > 0:
        state[x - 1] += state[x]
        state[x + 1] += state[x]
        state[x] = 0

    # print(' '.join(str(c) for c in state))

  return reduce(lambda a, b: a + b, state)
