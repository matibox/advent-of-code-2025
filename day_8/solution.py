def part1(lines: 'list[str]'):
  boxes = list(map(lambda l: [int(el) for el in l.split(',')], lines))
  iterations = 1000
  distances = []

  for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
      x1, y1, z1 = boxes[i]
      x2, y2, z2 = boxes[j]

      dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

      distances.append((boxes[i], boxes[j], dist))

  distances = list(sorted(distances, key=lambda d: d[2]))

  circuits: list[list[tuple]] = [] # [[(x1, y1, z1), (x2, y2, z2), ...]]
  box_to_circuit: dict[tuple, int] = {} # '(x,y,z) -> circuit id'

  attempts = 0
  for box_1, box_2, _ in distances:
    if attempts == iterations:
      break

    attempts += 1

    box_1 = tuple(box_1)
    box_2 = tuple(box_2)

    c1 = box_to_circuit.get(box_1)
    c2 = box_to_circuit.get(box_2)

    # case 1 -> both boxes don't belong to any circuit
    # create new circuit and assign them
    if c1 is None and c2 is None:
      circuits.append([box_1, box_2])
      i = len(circuits) - 1
      box_to_circuit[box_1] = i
      box_to_circuit[box_2] = i
    # case 2 -> box 1 is in a circuit
    # add box 2 to the circuit
    elif c1 is not None and c2 is None:
      circuits[c1].append(box_2)
      box_to_circuit[box_2] = c1
    # case 3 -> box 2 is in a circuit
    # add box 1 to the circuit
    elif c1 is None and c2 is not None:
      circuits[c2].append(box_1)
      box_to_circuit[box_1] = c2
    # case 4 -> both boxes are in DIFFERENT circuits
    # merge
    elif c1 is not None and c2 is not None and c1 != c2:
      if len(circuits[c1]) < len(circuits[c2]):
        c1, c2 = c2, c1

      for box in circuits[c2]:
        circuits[c1].append(box)
        box_to_circuit[box] = c1
      
      circuits[c2] = []
    # case 5 -> both boxes are in SAME circuits

  circuits = list(sorted([c for c in circuits if c], key=len, reverse=True))[:3]

  total = 1

  for c in circuits:
    total *= len(c)

  return total


def part2(lines: 'list[str]'):
  boxes = list(map(lambda l: [int(el) for el in l.split(',')], lines))
  distances = []

  for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
      x1, y1, z1 = boxes[i]
      x2, y2, z2 = boxes[j]

      dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

      distances.append((boxes[i], boxes[j], dist))

  distances = list(sorted(distances, key=lambda d: d[2]))

  circuits: list[list[tuple]] = [] # [[(x1, y1, z1), (x2, y2, z2), ...]]
  box_to_circuit: dict[tuple, int] = {} # '(x,y,z) -> circuit id'

  last_box_x1 = 0
  last_box_x2 = 0

  for box_1, box_2, _ in distances:
    if len(box_to_circuit) == len(boxes) and len([c for c in circuits if c]) == 1:
      break

    box_1 = tuple(box_1)
    box_2 = tuple(box_2)

    last_box_x1 = box_1[0]
    last_box_x2 = box_2[0]

    c1 = box_to_circuit.get(box_1)
    c2 = box_to_circuit.get(box_2)

    # case 1 -> both boxes don't belong to any circuit
    # create new circuit and assign them
    if c1 is None and c2 is None:
      circuits.append([box_1, box_2])
      i = len(circuits) - 1
      box_to_circuit[box_1] = i
      box_to_circuit[box_2] = i
    # case 2 -> box 1 is in a circuit
    # add box 2 to the circuit
    elif c1 is not None and c2 is None:
      circuits[c1].append(box_2)
      box_to_circuit[box_2] = c1
    # case 3 -> box 2 is in a circuit
    # add box 1 to the circuit
    elif c1 is None and c2 is not None:
      circuits[c2].append(box_1)
      box_to_circuit[box_1] = c2
    # case 4 -> both boxes are in DIFFERENT circuits
    # merge
    elif c1 is not None and c2 is not None and c1 != c2:
      if len(circuits[c1]) < len(circuits[c2]):
        c1, c2 = c2, c1

      for box in circuits[c2]:
        circuits[c1].append(box)
        box_to_circuit[box] = c1
      
      circuits[c2] = []
    # case 5 -> both boxes are in SAME circuits

  return last_box_x1 * last_box_x2