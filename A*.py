import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while pq:
        current = heapq.heappop(pq)[1]
        
        if current == goal:
            break

        for neighbor in graph[current]:

            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(pq, (priority, neighbor))
                came_from[neighbor] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    path = [goal]
    node = goal
    while node != start:
        node = came_from[node]
        path.append(node)
    path.reverse()
    return path

# Example usage:
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(1, 1): 1, (0, 0): 1},
    (1, 1): {(1, 0): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(1, 1): 1, (0, 2): 1},
    (2, 1): {(2, 2): 1, (1, 1): 1},
    (2, 2): {(1, 2): 1, (2, 1): 1}
}

start = (0, 0)
goal = (2, 2)

came_from, cost_so_far = a_star(graph, start, goal)
path = reconstruct_path(came_from, start, goal)

print(f"Path: {path}")
print(f"Cost: {cost_so_far[goal]}")