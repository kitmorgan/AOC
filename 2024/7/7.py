import time
from functools import lru_cache
import random
import sys
class Solution:

    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            for l in f:
                line = l.strip().split(':')
                target = int(line[0])
                vals = [int(x) for x in line[1].split()]
                l1.append((target,vals))
        return l1

    def part_one(self, l1):
        ans = 0
        for t, v in l1:
            if self.valid(t,v,0,0):
                ans += t
        return ans
    
    def valid(self, target, vals, curr, i):
        if curr == target and i == len(vals):
            return True
        if i == len(vals):
            return False
        n = vals[i]
        x = curr + n
        y = curr * n
        return self.valid(target, vals,x,i+1) or self.valid(target, vals, y, i+1)
    
    def part_two(self, l1):
        ans = 0
        for  t,v in l1:
            id = str(random.randint(1, 20000000))
            if self.valid_two(t,v,0,0, id):
                ans += t
            self.valid()
        return ans 
    
    def valid_two(self, target, vals, curr, i, id):
        if i == len(vals) or curr > target:
            if curr == target:
                print(id)
            return curr == target
        n = vals[i]
        x = curr + n
        y = curr * n
        z = int(str(curr) + str(n))
        a = self.valid_two(target, vals,x,i+1, id + "a") 
        b = False
        if i != 0:
            b = self.valid_two(target, vals, y, i+1, id + "b")
        c = self.valid_two(target,vals,z,i+1, id + "c")
        return a or b or c
        
sol = Solution()

l1 = sol.get_input('./2024/7/input.txt')
stime = time.time_ns()
print('Part One: ', sol.part_one(l1))
etime = time.time_ns()
print("1 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()
ans = sol.part_two(l1)
print('Part Two: ', ans)

print(492383931650959 - ans)
etime = time.time_ns()
print("2 -- took {} ms".format((etime - stime) // 1000000))
