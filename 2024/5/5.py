import time
from collections import defaultdict
import sys
from functools import cmp_to_key

class Solution:
    def __init__(self):
        self.i = 0
        self.d_order = {}
        sys.setrecursionlimit(10000)
        
    def get_input(self, file_path):
        l1 = []
        l2 = []
        two = False
        with open(file_path, 'r') as f:
            for l in f:
                if l == "\n":
                    two = True
                    continue
                if not two:
                    l1.append(tuple(int(ch) for ch in l.split('|')))
                else:
                    l2.append([int(ch) for ch in l.split(',')])
        return (l1,l2)
    
    def part_one(self, l1,l2):
        # create map {page : set(pages_after)}
        # loop through e in l2
            # if x in map[e] in seen: return false
            # seen.add(e)
        d_before = defaultdict(set)
        ans = 0 
        for u, v in l1:
            d_before[v].add(u)
            # 53: {97, 75, 61, 47}
        
        for pages in l2:
            flag = True
            before = set()
            for page in pages:
                if page in before:
                    flag = False
                    break
                before |= d_before[page]
                
            ans += pages[len(pages)//2] if flag else 0
         
        return ans
        
    def part_two(self, l1, l2):
        self.d_before = defaultdict(set)
        ans = 0 
        for u, v in l1:
            self.d_before[u].add(v)
            
        for pages in l2:
            sorted_pages = sorted(pages, key=cmp_to_key(lambda x, y: -1 if y in self.d_before[x] else 1))
            if pages != sorted_pages:
                ans += sorted_pages[len(sorted_pages)//2]
        return ans
    
            # worked for sample not for real input
    # def get_order(self, x):
    #     # dfs, first look at each of x's "afters"
    #     # if any x is either not in order or all of it's "afters" have an assigned value give it the next value
    #     if x not in self.d_order:
    #         for n in self.d_before[x]:
    #             self.get_order(n)
    #         self.i += 1
    #         self.d_order[x] = self.i
            
    def is_ordered(self, l):
        flag = True
        before = set()
        for page in l:
            if page in before:
                flag = False
            before |= self.d_before[page]
        return flag
        
sol = Solution()

l1, l2 = sol.get_input('./2024/5/input.txt')
stime = time.time_ns()
print('Part One: ', sol.part_one(l1,l2))
etime = time.time_ns()
print("1 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()        
print('Part Two: ', sol.part_two(l1, l2))
etime = time.time_ns()
print("2 -- took {} ms".format((etime - stime) // 1000000))