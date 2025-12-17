def part1(lines: 'list[str]'):
  total = 0

  for y, line in enumerate(lines):
    for x, ch in enumerate(line):
      if ch != "@" :
        continue
      
      adjacent_rolls = 0

      for adj_y in range(-1, 2):
        for adj_x in range(-1, 2):
          if adj_y == 0 and adj_x == 0:
            continue

          dest_y = y + adj_y
          dest_x = x + adj_x 

          if dest_x < 0 or dest_x >= len(lines[0]) or dest_y < 0 or dest_y >= len(lines):
            continue

          if lines[dest_y][dest_x] == "@":
            adjacent_rolls += 1
      

      if adjacent_rolls < 4:
        total += 1

  return total


def part2(lines: 'list[str]'):
  lines = [*lines]

  total = 0


  while True:
    to_remove = []

    for y, line in enumerate(lines):
      for x, ch in enumerate(line):
        if ch != "@" :
          continue
        
        adjacent_rolls = 0

        for adj_y in range(-1, 2):
          for adj_x in range(-1, 2):
            if adj_y == 0 and adj_x == 0:
              continue

            dest_y = y + adj_y
            dest_x = x + adj_x 

            if dest_x < 0 or dest_x >= len(lines[0]) or dest_y < 0 or dest_y >= len(lines):
              continue

            if lines[dest_y][dest_x] == "@":
              adjacent_rolls += 1
        

        if adjacent_rolls < 4:
          total += 1
          to_remove.append((y, x))

    if len(to_remove) == 0:
      break

    for y, x in to_remove:
      str = lines[y]
      str = list(str)
      str[x] = "."
      lines[y] = "".join(str)


  return total
