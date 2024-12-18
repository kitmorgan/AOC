from heapq import heappop, heappush
from collections import defaultdict
import time

class Solution:
    def __init__(self, file_path):
        self.first_corrupted = set()
        self.all_corrupted = []
        self.start = (0,0)
        self.end = (70,70)
        self.M = 71
        self.N = 71
        with open(file_path,'r') as f:
            i = 1
            for line in f:
                if i <= 1024:
                    self.first_corrupted.add(tuple(map(int,line.strip().split(','))))
                i += 1
                self.all_corrupted.append(tuple(map(int,line.strip().split(','))))
    def part_one(self):
        print('part one: ', self.dijkstras())
    
    def dijkstras(self) -> tuple[int,int]:
        q = [(0,(0,0))]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        distances = defaultdict(lambda: float('inf'))
        distances[(0,0)] = 0
        while q:
            dist, loc = heappop(q)
            if loc == (70,70):
                return dist
            for di, dj in dirs:
                i = di + loc[0]
                j = dj + loc[1]
                new_dist = dist + 1
                if 0 <= i < self.M and 0 <= j < self.N and (i,j) not in self.first_corrupted and distances[(i,j)] > new_dist:
                    heappush(q,(new_dist, (i,j)))
                    distances[(i,j)] = new_dist

    def part_two(self):
        l, r = 1024, len(self.all_corrupted) -1 # find first instance of 
        ans = float('inf')
        while l < r:
            m = (l + r) // 2
            self.first_corrupted = set(self.all_corrupted[:m+1])
            res = self.dijkstras()
            if not res:
                r = m - 1
                ans = min(ans, m)
            else:
                l = m + 1
        print('part two', ans, self.all_corrupted[ans])
        
    def brute(self):
        for m in range(1024,len(self.all_corrupted)):
            self.first_corrupted = set(self.all_corrupted[:m+1])
            res = self.dijkstras()
            if not res:
                print('brute - ', self.all_corrupted[m])
                return
            
s = Solution('./18.txt')
stime = time.time_ns()
s.part_one()
etime = time.time_ns()
print("1 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()
s.part_two()
etime = time.time_ns()
print("2 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()
s.brute()
etime = time.time_ns()
print("3 -- took {} ms".format((etime - stime) // 1000000))