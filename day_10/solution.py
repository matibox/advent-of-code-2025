from collections import defaultdict
from itertools import product

def part1(lines: 'list[str]'):
  result = 0

  for line in lines:
    line = line.split(" ")[:-1]
    lights = line[0][1:-1]
    buttons = line[1:]

    lights_target = [1 if l == "#" else 0 for l in lights]
    lights_to_buttons: dict[int, set] = defaultdict(set)

    for i, b in enumerate(buttons):
      button_lights = b[1:-1].split(",")
      
      for l1 in button_lights:
        lights_to_buttons[int(l1)].add(i)

    equations_order = [] # (pivot_btn, buttons, target_val)
    # one equation depends on another, as in
    # 1. x + y + z = 10
    # 2. y + z = 5

    # go from reverse, subtract 2. from 1.
    # giving
    # 1. x = 5

    for l1 in range(len(lights)):
      btns_1 = lights_to_buttons[l1]
      target_1 = lights_target[l1]

      if not btns_1:
        continue

      pivot = min(btns_1)

      equations_order.append((pivot, btns_1, target_1))
      
      for l2 in range(l1 + 1, len(lights)):
        btns_2 = lights_to_buttons[l2]
        target_2 = lights_target[l2]
        
        if pivot not in btns_2:
          continue
        
        new_btns = btns_2 ^ btns_1
        new_target = target_2 ^ target_1

        lights_to_buttons[l2] = new_btns
        lights_target[l2] = new_target

    all_button_indices = set(range(len(buttons)))
    pivot_buttons = set(eq[0] for eq in equations_order)

    # free buttons - they don't depend on anything
    free_buttons = list(all_button_indices - pivot_buttons)

    min_clicks = 999999

    for combination in product([0, 1], repeat=len(free_buttons)):
      trial_clicks = {}

      for i, val in enumerate(combination):
        trial_clicks[free_buttons[i]] = bool(val)
      
      for pivot, btns_in_eq, target in reversed(equations_order):
        current_state = 0
        for b in btns_in_eq:
          if b != pivot and trial_clicks.get(b, False):
            current_state ^= 1
        
        trial_clicks[pivot] = current_state != target

      total = sum(trial_clicks.values())
      min_clicks = min(min_clicks, total)

    result += min_clicks

  return result


def part2(lines: 'list[str]'):

  return None