from dataclasses import dataclass

favorite_number = 1350

class Graph:
    def bfs(self, start: "Node", end: "Node") -> int:
        queue = [start]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node.x == end.x and node.y == end.y:
                return node.dist
            if node not in visited:
                visited.add(node)
                queue.extend(node.neighbors)
        return None

    def distinct(self, start: "Node", max_dist: int) -> int:
        queue = [start]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node.dist > max_dist:
                continue
            if (node.x, node.y) not in visited:
                visited.add((node.x, node.y))
                queue.extend(node.neighbors)
        return len(visited)


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    dist: int

    def is_open(self):
        return bin((self.x*self.x + 3*self.x + 2*self.x*self.y + self.y + self.y*self.y) + favorite_number).count('1') % 2 == 0

    @property
    def neighbors(self):
        n = list()
        for n_x, n_y in ((self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)):
            if n_x >= 100 or n_y >= 100 or n_x < 0 or n_y < 0:
                continue
            new_neighbor = Node(n_x, n_y, self.dist + 1)
            if new_neighbor.is_open():
                n.append(new_neighbor)
        return n



def q1():
    g = Graph()
    start = Node(1, 1, 0)
    end = Node(31, 39, 0)
    return g.bfs(start, end)

def q2():
    g = Graph()
    start = Node(1, 1, 0)
    return g.distinct(start, 50)

if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
