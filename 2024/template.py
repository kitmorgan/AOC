import time
class Solution:
    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            for l in f:
                pass
        return l1
    
    def part_one(x):
        return
    def part_two(x):
        return
sol = Solution()

l1 = sol.get_input('./2024/5/input.txt')

stime = time.time_ns()
print('Part One: ', sol.part_one(l1))
etime = time.time_ns()
print("1 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()        
print('Part Two: ', sol.part_two(l1))
etime = time.time_ns()
print("2 -- took {} ms".format((etime - stime) // 1000000))