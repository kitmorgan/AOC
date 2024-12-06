import time
from collections import defaultdict, deque
import sys
from functools import cmp_to_key


class Solution:

    def get_input(self, file_path):
        l1 = []
        start = [0,0]
        i = 0
        with open(file_path, 'r') as f:
            for l in f:
                l = l.strip()
                l1.append(list(l))
                if '^' in l:
                    start[0] = i
                    start[1] = l.index('^')
                i += 1
            self.M = len(l1)
            self.N = len(l1[0])
        return l1, start

    def part_one(self, l1,start):
        ans = 1
        d = 0
        dir = [(-1,0), (0,1),(1,0),(0,-1)]
        i = start[0]
        j = start[1]
        l1[i][j] = 'x'
        while self.v(i,j):
            if self.v(i+dir[d][0],j+dir[d][1]):
                if l1[i+dir[d][0]][j+ dir[d][1]] == '#':
                    # turn
                    d = (d+1) % 4
                else:
                    # move
                    i += dir[d][0]
                    j += dir[d][1]
                    if l1[i][j] == '.':
                        ans += 1
                        l1[i][j] = 'x'
            else:
                return ans
        return ans
    def v(self,i,j):
        return i >= 0 and j >= 0 and i < self.N and j < self.M
    
    def part_two(self, l1,start):
        # i guess i just brute force
        ans = 0 
        for i in range(self.M):
            for j in range(self.N):
                if [i,j] != start and l1[i][j] != "#":
                    l1[i][j] = "#"
                    ans += 1 if self.is_loop(l1,start) else 0
                    l1[i][j] = '.'
        return ans

    def is_loop(self, l1, start):
        dir = [(-1,0), (0,1),(1,0),(0,-1)]
        d = 0
        i = start[0]
        j = start[1]
        seen = defaultdict(int)
        hit = []
        while self.v(i,j):
            if self.v(i+dir[d][0],j+dir[d][1]):
                if l1[i+dir[d][0]][j+ dir[d][1]] == '#':
                    # turn
                    d = (d+1) % 4
                    seen[(i,j)] += 1
                    if seen[(i,j)] >= 4:
                        return True
                else:
                    # move
                    i += dir[d][0]
                    j += dir[d][1]
                
            else:
                return False
        return False

sol = Solution()

l1, start = sol.get_input('./2024/6/input.txt')
stime = time.time_ns()
print('Part One: ', sol.part_one(l1,start))
etime = time.time_ns()
print("1 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()
print('Part Two: ', sol.part_two(l1,start))
etime = time.time_ns()
print("2 -- took {} ms".format((etime - stime) // 1000000))
