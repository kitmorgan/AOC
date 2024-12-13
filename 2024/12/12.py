from collections import deque


class Solution:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.grid = [list(line.strip()) for line in f]
            self.M = len(self.grid)
            self.N = len(self.grid[0])
            self.visited_one = set()
            self.visited_two = set()
            self.units = []
            self.d = {}

    def dfs(self, pos: tuple, unit_ind: int = None):
        if pos not in self.visited_one:
            char = self.grid[pos[0]][pos[1]]
            self.visited_one.add(pos)
            if unit_ind is None:
                self.units.append([0, 0])
                unit_ind = len(self.units) - 1
            self.units[unit_ind][1] += 1
            dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            per = 4
            for dir in dirs:
                di = pos[0] + dir[0]
                dj = pos[1] + dir[1]
                if di >= 0 and dj >= 0 and di < self.M and dj < self.N and (di, dj) and self.grid[di][dj] == char:
                    per -= 1
                    self.dfs((di, dj), unit_ind)
            self.units[unit_ind][0] += per

    def dfs_2(self, pos: tuple, unit_ind: int = None, edges: set = set()):
        if pos not in self.visited_one:
            char = self.grid[pos[0]][pos[1]]

            self.visited_one.add(pos)

            if unit_ind is None:
                self.units.append([0, 0])
                unit_ind = len(self.units) - 1

            self.units[unit_ind][1] += 1
            dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            per = 0

            for dir in dirs:
                di = pos[0] + dir[0]
                dj = pos[1] + dir[1]

            for dir in dirs:
                di = pos[0] + dir[0]
                dj = pos[1] + dir[1]
                if di >= 0 and dj >= 0 and di < self.M and dj < self.N and (di, dj) and self.grid[di][dj] == char:
                    self.dfs_2((di, dj), unit_ind, edges)
                else:
                    edges.add((di, dj, dir)) # all squares that count in part one 

            return unit_ind, edges

    def part_one(self):
        for i in range(self.M):
            for j in range(self.N):
                if (i, j) not in self.visited_one:
                    self.dfs((i, j))
        ans = 0
        for block in self.units:
            ans += block[0] * block[1]
        return ans

    def get_perim(self, edges: set) -> int:
        ans = 0
        dirs = [(1, 0), (0, 1)]
        counted = set()
        l = sorted(edges)
        for edge in sorted(edges):
            if edge not in counted:
                ans += 1
            for dir in dirs:
                curr = (edge[0] + dir[0], edge[1] + dir[1],edge[2])
                counted.add(curr)
            
            counted.add(edge)
        return ans

    def part_two(self):
        for i in range(self.M):
            for j in range(self.N):
                if (i, j) not in self.visited_one:
                    id, edges = self.dfs_2((i, j), None, set())
                    self.units[id][0] = self.get_perim(edges)
                    print(id, edges)
        ans = 0
        for block in self.units:
            ans += block[0] * block[1]
            print(block[0], block[1])
        return ans


# walk through grid,a single unit has per 4 area 1
# for each unit it touches it loses 1 per
s = Solution('./12.txt')
# print('Part One:',s.part_one())
print('Part Two:', s.part_two())
