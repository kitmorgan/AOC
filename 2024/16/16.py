from collections import defaultdict, deque
from copy import deepcopy
import heapq

class Solution:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.grid = []
            self.start = None
            self.end = None
            self.ans = float('inf')
            self.dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            
            for i, line in enumerate(f):
                self.grid.append(list(line.strip()))
                if not self.start and  line.__contains__('S'):
                    self.start = (i,line.index('S'),0)
                if not self.end and line.__contains__('E'):
                    self.end = (i, line.index('E'))
            self.M = len(self.grid)
            self.N = len(self.grid[0])
            

        
    def bfs(self):
        q = []
        heapq.heappush(q, (0,self.start, (0,1))) # dist, loc, dir
        visited = defaultdict(lambda: float('inf'))
        while q:
            dist, loc, facing = heapq.heappop(q)
            if dist > visited[loc]:
                continue
            for dir in self.dirs:
                di, dj = dir
                i = loc[0] + di
                j = loc[1] + dj
                if not (0 <= i < self.M and 0 <= j < self.N and self.grid[i][j] != '#'):
                    continue
                if dir == facing:
                    next_dist = dist + 1
                else:
                    next_dist = dist + 1001
                
                if next_dist < visited[(i,j)]:
                    visited[(i,j)] = next_dist
                    self.grid[i][j] = next_dist
                    heapq.heappush(q, (next_dist, (i,j), dir))
                    
                if (i,j) == self.end:
                    return next_dist  
        return visited
            
        
    def part_one(self):
        print('PART ONE: ', self.bfs())

s = Solution('./16.txt')
s.part_one()