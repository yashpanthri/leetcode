import heapq
import math

def run_dijkstra(start, goal, grid, diagonal):
    grid_height = len(grid)
    grid_width = len(grid[0])
    start_x, start_y = start
    goal_x, goal_y = goal
    if grid[start_y][start_x] == 1 or grid[goal_y][goal_x] == 1:
        return None, math.inf
    
    if diagonal:
        moves = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    else:
        moves = [(-1,0),(1,0),(0,-1),(0,1)]

    distance = [[math.inf]*grid_width for _ in range(grid_height)]
    parent = [[None]*grid_width for _ in range(grid_height)]
    distance[start_y][start_x] = 0.0
    priority_queue = []
    heapq.heappush(priority_queue, (0.0, start_x, start_y))

    while priority_queue:
        d, x, y = heapq.heappop(priority_queue)
        if d != distance[y][x]:
            continue
        if (x, y) == (goal_x, goal_y):
            break
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < grid_width and 0 <= new_y < grid_height and grid[new_y][new_x] == 0:
                weight = math.sqrt(2 if (dx != 0 and dy != 0) else 1.0)
                new_distance = d+weight
                if new_distance < distance[new_y][new_x]:
                    distance[new_y][new_x] = new_distance
                    parent[new_y][new_x] = (x, y)
                    heapq.heappush(priority_queue, (new_distance, new_x, new_y))

    if distance[goal_y][goal_x] == math.inf:
        return None, math.inf
    path = []
    current = (goal_x, goal_y)
    while current is not None:
        path.append(current)
        cx, cy = current
        current = parent[cy][cx]
    path.reverse()
    return path, distance[goal_y][goal_x]

def draw(grid, path, start,goal):
    grid_height = len(grid)
    grid_width = len(grid[0])
    path_set = set(path or [])
    start_x, start_y = start
    goal_x, goal_y = goal
    for y in range(grid_height):
        row = []
        for x in range(grid_width):
            if (x, y) == (start_x, start_y):
                row.append("S")
            elif (x, y) == (goal_x, goal_y):
                row.append("G")
            elif (x, y) in path_set:
                row.append("*")
            elif grid[y][x] == 1:
                row.append("#")
            else:
                row.append(".")
        print("".join(row))

if __name__ == "__main__":
    grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,1,1,1,1,0],
        [0,0,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,1,1,0,1,0],
        [0,1,0,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    start = [0,0]
    goal = [9, 5]
    consider_diagonal = input("Want to consider diagonal movements? (Y/N): ") == "Y"
    path, cost = run_dijkstra(start, goal, grid, consider_diagonal)
    print("cost:", cost)
    draw(grid, path, start, goal)