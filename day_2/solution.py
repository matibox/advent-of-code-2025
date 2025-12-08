def part1(lines: 'list[str]'):
  line = lines[0]

  sum = 0

  for id_group in line.split(','):
    [start, end] = [int(id) for id in id_group.split('-')]
      
    for _id in range(start, end + 1):
      id = str(_id)
         
      if len(id) % 2 == 1:
        continue
         
      if id[0:int(len(id)/2)] == id[int(len(id)/2):]:
        sum += _id

  return sum


def is_repeated_subsequence(s: 'str') -> 'bool':
  return s in (s + s)[1:-1]

def part2(lines: 'list[str]'):
  line = lines[0]

  sum = 0

  for id_group in line.split(','):
    [start, end] = [int(id) for id in id_group.split('-')]
      
    for _id in range(start, end + 1):
      id = str(_id)
         
      if is_repeated_subsequence(id):
        sum += _id

  return sum
