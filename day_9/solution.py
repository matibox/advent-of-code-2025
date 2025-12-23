from collections import defaultdict

def part1(lines: 'list[str]'):
  nodes: list[tuple[int, int]] = []

  for line in lines:
    x, y = line.split(',')
    nodes.append((int(x), int(y)))

  # |------|
  # |      |  b
  # |------|
  #    a

  largest_area = 0

  for i, n1 in enumerate(nodes):
    for n2 in nodes[i + 1:]:
      a = abs(n2[0] - n1[0]) + 1
      b = abs(n2[1] - n1[1]) + 1

      area = a * b

      if area > largest_area:
        largest_area = area

  return largest_area

def calc_area(x_diff: 'int', y_diff: 'int'):
  x = abs(x_diff) + 1
  y = abs(y_diff) + 1

  return x * y

def part2(lines: 'list[str]'):
  red_nodes = []


  for line in lines:
    x, y = line.split(',')
    red_nodes.append((int(x), int(y)))

  shape_by_rows = defaultdict(list)

  # create horizontal lines
  start = red_nodes[0]
  pos = None # [x, y]
  vertical = None

  while pos is None or not (pos[0] == start[0] and pos[1] == start[1]):
    if pos is None:
      pos = start

      # check horizontal nodes
      inline_nodes = [n for n in red_nodes if n[0] != pos[0] and n[1] == pos[1]]
      
      if len(inline_nodes) > 0:
        vertical = True
        next = inline_nodes[0]

        # left
        if next[0] < pos[0]:
          shape_by_rows[pos[1]].append((next[0], pos[0]))
        # right
        else:
          shape_by_rows[pos[1]].append((pos[0], next[0]))
        
        pos = next
        continue
      
      # check vertical nodes
      inline_nodes = [n for n in red_nodes if n[0] == pos[0] and n[1] != pos[1]]
      next = inline_nodes[0]
      vertical = False

      pos = next
      continue
    else:
      if vertical:
        inline_nodes = [n for n in red_nodes if n[0] == pos[0] and n[1] != pos[1]]
        next = inline_nodes[0]
      else:
        inline_nodes = [n for n in red_nodes if n[0] != pos[0] and n[1] == pos[1]]
        next = inline_nodes[0]
        
        # left
        if next[0] < pos[0]:
          shape_by_rows[pos[1]].append((next[0], pos[0]))

        # right
        else:
          shape_by_rows[pos[1]].append((pos[0], next[0]))

      vertical = not vertical
      pos = next

  ys = [y for _, y in red_nodes]
  y_min = min(ys)
  y_max = max(ys)

  for y in range(y_min, y_max + 1):
    intersections = []

    # todo: loop through EDGES
    for i in range(len(red_nodes)):
      x1, y1 = red_nodes[i]
      x2, y2 = red_nodes[(i + 1) % len(red_nodes)] # this ensures last point connects with the first

      if y1 == y2:
        # print(y, (x1, y1), (x2, y2), False)
        # edge is horizontal -> ignore
        continue

      if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1

      if y1 <= y < y2:
        # print(y, (x1, y1), (x2, y2), True)
        # edge is vertical -> SWITCH = intersection
        intersections.append(x1)
    
    intersections = sorted(intersections)
  
    for i in range(0, len(intersections), 2):
      x1 = intersections[i]
      x2 = intersections[i + 1]

      inside = (x1, x2) # from x1 to x2 inclusive -> inside of the shape

      shape_by_rows[y].append(inside)

  shape_by_rows = dict(sorted(shape_by_rows.items()))

  for y, ranges in shape_by_rows.items():
    for i, r1 in enumerate(ranges):
      for r2 in ranges[i + 1:]:
        if r1[0] > r2[0]:
          r1, r2 = r2, r1

        if r1[1] == r2[0]:
          ranges[i] = (r1[0], r2[1])
          del ranges[i + 1]

  max_area = 0

  for i, c1 in enumerate(red_nodes):
    for c2 in red_nodes[i+1:]:
      x1, y1 = c1
      x2, y2 = c2

      x_diff = x2 - x1
      y_diff = y2 - y1

      # horizontal or vertical edge
      if y_diff == 0 or x_diff == 0:
        area = calc_area(x_diff, y_diff)
        if area > max_area:
          max_area = area
      else:
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        rows_in_shape = 0

        for y in range(y_min, y_max + 1):
          inside = False
          shape_ranges = shape_by_rows[y]

          for r in shape_ranges:
            if x_min >= r[0] and x_max <= r[1]:
              inside = True
              break

          if not inside:
            break

          rows_in_shape += 1
        
        if rows_in_shape == y_max - y_min + 1:
          area = calc_area(x_diff, y_diff)
          if area > max_area:
            max_area = area

  return max_area # around 100s runtime, but works