
def part1(lines: 'list[str]'):
  position = 50
  zeroes = 0

  for line in lines:
    direction = line[0]
    quantity = int(line[1:]) % 100

    if direction == 'L':
      if position - quantity < 0:
        diff = quantity - position
        position = 100 - diff
      else:
        position -= quantity
    else:
      if position + quantity > 99:
        diff = abs(100 - (position + quantity))
        position = 0 + diff
      else:
        position += quantity
    
    zeroes += 1 if position == 0 else 0

  return zeroes


def part2(lines: 'list[str]'):
  position = 50
  zeroes = 0
  for line in lines:
    direction = line[0]
    move = int(f"{'-' if direction == 'L' else ''}{line[1:]}")
    destination = (position + move) % 100
    through_zero = 0

    for i in range(position, position + move + (-1 if direction == 'L' else 1), -1 if direction == 'L' else 1):
      if i % 100 == 0 and not (position == 0 and i == 0):
        through_zero += 1

    position = destination

    zeroes += through_zero

  return zeroes
      