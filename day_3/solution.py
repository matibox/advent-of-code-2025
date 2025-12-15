def part1(banks: 'list[str]'):
  total = 0
  for bank in banks:
    reverse = False
    batteries = [int(b) for b in bank]
    b1 = max(batteries)
    b1idx = batteries.index(b1)

    if b1idx == len(batteries) - 1:
      batteries = batteries[0:-1]
      reverse = True
    else:
      batteries = batteries[b1idx + 1:]

    b2 = max(batteries)
    
    if not reverse:
      s = int(f'{b1}{b2}')
    else:
      s = int(f'{b2}{b1}')

    total += s

  return total

def max_subsequence_number(bank: str, max_length: int = 12) -> int:
  stack = []
  to_discard = len(bank) - max_length

  for battery in bank:
    while len(stack) != 0 and to_discard > 0 and int(stack[-1]) < int(battery):
      stack.pop()
      to_discard -= 1

    stack.append(battery)
        
  return int(''.join(stack[:max_length]))

def part2(banks: 'list[str]') -> int:
  total = 0
  max_length = 12

  for bank in banks:
    total += max_subsequence_number(bank, max_length)

  return total
