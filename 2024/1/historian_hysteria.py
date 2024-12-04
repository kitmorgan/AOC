import heapq
from collections import Counter

class Solution:
    def get_input(self, file):
        list1 = []
        list2 = []
        with open(file, 'r') as f:
            for line in f: 
                nums = line.split()
                heapq.heappush(list1, int(nums[0]))
                heapq.heappush(list2, int(nums[1]))
        return (list1, list2)

    def print_ans_one(self, list1, list2):
        diff = 0
        while list1:
            a = heapq.heappop(list1)
            b = heapq.heappop(list2)
            diff += max(a, b) - min(a, b)
            print(a,b)

        print(diff)
    
    def print_ans_two(self, list1, list2):
        l1 = Counter(list1)
        l2 = Counter(list2)
        sim = 0
        for el in list1:
            sim += el * l2[el]
        
        print(sim)
        
sol = Solution()
one, two = sol.get_input('./2024/1/input.txt')
sol.print_ans_two(one, two)
