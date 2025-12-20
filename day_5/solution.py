def parseRange(range: 'str'):
  [start, end] = range.split('-')
  return (int(start), int(end))

def part1(lines: 'list[str]'):
  input = '\n'.join(lines)
  total = 0

  [ranges, ids] = [e.split('\n') for e in input.split('\n\n')]

  ranges = list(map(parseRange, ranges))
  ids = [int(id) for id in ids]

  for id in ids:
    for (start, end) in ranges:
      if id >= start and id <= end:
        total += 1
        break

  return total


def part2(lines: 'list[str]'):
  input = '\n'.join(lines)
  total = 0

  ranges = list(map(parseRange, input.split('\n\n')[0].split('\n')))
  ranges = sorted(ranges, key = lambda x: x[0])

  occupied_ranges = []

  for start, end in ranges:
    for o_start, o_end in occupied_ranges:
      if start >= o_start and start <= o_end:
        start = o_end + 1 

      if end >= o_start and end <= o_end:
        end = o_start - 1
    
    if end >= start:
      diff = end - start + 1
      total += diff
      occupied_ranges.append((start, end))

  return total