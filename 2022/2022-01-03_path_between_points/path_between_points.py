"""
Given a list of Point objects (where a Point object has a name, and a list of
names it is connected to), a starting Point object, and an ending Point object,
return a possible path between the two Points. If there are multiple paths,
return the shortest one. If there is no path, return “no path”.

Example:

listOfPoints = [
  { name: "A", connections: ["B", "C"] },
  { name: "B", connections: ["A", "E"] },
  { name: "C", connections: ["A", "D"] },
  { name: "D", connections: ["C"] },
  { name: "E", connections: ["B", "F"] },
  { name: "F", connections: ["E"] },
]

$ pathBetweenPoints(listOfPoints, "A", "F")
$ A -> B -> E -> F

$ pathBetweenPoints(listOfPoints, "D", "B")
$ D -> C -> A -> B
"""

def get_route(backlinks, start, end):
    pt = end
    points = [pt]
    while pt != start:
        pt = backlinks[pt]
        points.insert(0, pt)
    return " -> ".join(points)


def pathBetweenPoints(points, start, end):
    connections = { pt['name']: pt['connections'] for pt in points }
    backlinks = {}
    queue = [start]
    current_pos = None
    while queue:
        current_pos = queue.pop(0)
        if current_pos == end:
            return get_route(backlinks, start, end)
        for pt in connections[current_pos]:
            if pt not in backlinks:
                backlinks[pt] = current_pos
                queue.append(pt)
    return "no path"
    


def test_examples():
    listOfPoints = [
      { "name": "A", "connections": ["B", "C"] },
      { "name": "B", "connections": ["A", "E"] },
      { "name": "C", "connections": ["A", "D"] },
      { "name": "D", "connections": ["C"] },
      { "name": "E", "connections": ["B", "F"] },
      { "name": "F", "connections": ["E"] },
    ]
    assert pathBetweenPoints(listOfPoints, "A", "F") == "A -> B -> E -> F"
    assert pathBetweenPoints(listOfPoints, "D", "B") == "D -> C -> A -> B"


def test_no_path():
    points = [
        { "name": "A", "connections": [] },
        { "name": "B", "connections": [] }
    ]
    assert pathBetweenPoints(points, "A", "B") == "no path"


def test_start_is_end():
    points = [
        { "name": "A", "connections": [] },
        { "name": "B", "connections": [] }
    ]
    assert pathBetweenPoints(points, "A", "A") == "A"
