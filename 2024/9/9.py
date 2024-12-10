import time
from collections import defaultdict, deque
import re
from math import floor
from itertools import repeat
import sys


class Solution:
    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            input_data = f.read()
        return list(map(int, input_data.strip()))

    def get_list(self, s):
        l = []
        inc = 0
        for i, ch in enumerate(s):
            for j in range(int(ch)):
                l.append(inc if i % 2 == 0 else None)
            inc += 1 if i % 2 == 0 else 0
        if inc % 2 == 1:
            while l[-1] == None:
                l.pop()
        return l

    def reorder_list(self, l):
        i = 0
        while i < len(l):
            while l[i] == None:
                l[i] = l.pop()
            i += 1

    def reorder_list2(self, l):
        i = 0
        while i < len(l):
            j = i  # j = 0
            while l[j] == None:  # find out how much empty space
                j += 1
            empty = j - i  # empty = 0-0
            while l[-1] == None:
                l.pop()
            if empty:
                v = len(l) - 1
                curr = l[v]
                cnt = 0
                while v > j and empty:
                    if l[v] != curr:  # check if last chunk fits
                        if cnt <= empty and cnt != 0:  # cnt - 2, empty - 3
                            v_tmp = v + 1  # [9 *, 9]
                            for _ in range(cnt):  # 0, 1
                                l[i] = curr  # l[2] = 9
                                i += 1  # 3
                                l[v_tmp] = None  # l[9*]
                                v_tmp += 1
                            empty -= cnt
                        while l[v] == None:
                            v -= 1
                        cnt = 1
                        curr = l[v]
                        v -= 1
                    elif l[v] == None:
                        v -= 1
                    else:
                        cnt += 1
                        v -= 1
                i = j + 1
            else:
                i += 1

    def re(self, l, start):
        if start < 2:
            return
        j = start
        while l[j] == None:
            j -= 1
        curr = l[j]
        cnt = 0
        while curr == l[j]:
            cnt += 1
            j -= 1
        spaces = 0
        i = 0
        while i < j:
            if l[i] == None:
                spaces += 1
            else:
                spaces = 0
            i += 1
            if spaces == cnt:
                tmp_j = j+1
                for x in range(i - spaces, i):  # 11 - 3, 11 -> 8,9,10
                    l[x], l[tmp_j] = l[tmp_j], l[x]
                    tmp_j += 1
                break

        return self.re(l, j)

    def get_checksum(self, l):
        ans = 0
        for i, n in enumerate(l):
            ans += i * n if n is not None else 0
        return ans

    def part_one(self, l1):
        l = self.get_list(l1)
        # print(l)
        # self.reorder_list(l)
        print(self.ans(l))
        return self.get_checksum(l)

    def part_two(self, l1):
        sys.setrecursionlimit(10000)
        l = self.get_list(l1)
        j = self.re(l, len(l) - 1)
        return self.get_checksum(l)

    def get_data(self, d):
        ids = {}
        ind = 0
        spaces = []
        id = 0
        for i, ch in enumerate(d):
            # print("i", i, "ch", ch, "id", id, "mod", i % 2, "ind", ind)
            if i % 2 == 0:
                ids[id] = (ind, int(ch))  # start, len
                id += 1
            else:
                if int(ch) != 0:
                    spaces.append((ind, int(ch)))  # start, len
            ind += int(ch)
        return ids, spaces, id - 1  # dict, list, max_id

    def part_two_v2(self, ids: dict, spaces, max_id):
        #print(ids,spaces)               # 00...111...2...333.44.5555.6666.777.888899
        for i in range(max_id, -1, -1): # 00992111777.44.333....5555.6666.....8888
            start_id, len_id = ids[i]
            for j, space in enumerate(spaces):
                start_space, len_space = space
                if start_space < start_id and len_space >= len_id: # found a space to fill
                    start_id = start_space # id moves to space
                    # len stays same
                    len_space -= len_id # space shrinks
                    start_space += len_id # space start shifts over 1...22 (1,3) -> (3,1) 122. 
                    if len_space == 0:
                        spaces.pop(j) # remove
                    else:
                        spaces[j] = (start_space, len_space)
                    ids[i] = (start_id, len_id)
                    break # found the space so exit this loop
        ans = 0
        for id, val in ids.items(): 
            start, length = val
            for x in range(start, start+length): # 2 : (1,3) 
                ans += x * id
        return ans
                
                    


sol = Solution()

l1 = sol.get_input('./9.txt')
ids, spaces, max_id = sol.get_data(l1)
ans = sol.part_two_v2(ids, spaces, max_id)
print(ans)
# stime = time.time_ns()

# print('Part One: ', sol.part_one(l1))
# etime = time.time_ns()
# print("1 -- took {} ms".format((etime - stime) // 1000000))

# stime = time.time_ns()
print('Part Two: ', sol.part_two(l1))
# etime = time.time_ns()
# print("2 -- took {} ms".format((etime - stime) // 1000000))
