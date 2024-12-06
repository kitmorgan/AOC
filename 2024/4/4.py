import time


class Solution:
    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            for l in f:
                l1 += [[ch for ch in l if ch.isalpha()]]
        return l1
    
    def part_one(self,l):
        # loop through each elem of list
            # when elem == x
                # check every dir
                # if target isnt m use same dir
            # increment counter if xmas is found
        self.dirs = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
        ans = 0
        self.l = l 
        self.M = len(self.l)
        self.N = len(self.l[0])
        
        self.xmas = 'XMAS'
        for i in range(self.M):
            for j in range(self.N):
                if self.l[i][j] == 'X':
                    for dx, dy in self.dirs:
                        ans += self.validate(dx + i, dy + j, 1,(dx, dy))                
        return ans
    
    def part_two(self,l):
        # find 'A', check corners
        valid = set(['MAS','SAM'])
        ans = 0
        for i in range(self.M):
            for j in range(self.N):
                if (i - 1 >= 0 and j - 1 >= 0 and i + 1 < self.M and j + 1 < self.N) and self.l[i][j] == 'A':
                    tmp1 = ''.join([self.l[i-1][j-1],'A', self.l[i+1][j+1]])
                    tmp2 = ''.join([self.l[i-1][j+1],'A', self.l[i+1][j-1]])
                    if tmp1 in valid and tmp2 in valid:
                        ans += 1             
        return ans
    
    def validate(self, i, j, target, dir) -> int:
        if target == 4:
            return 0
        if (i >= 0 and j >= 0 and i < self.M and j < self.N) and self.l[i][j] == self.xmas[target]:
            if target == 3:
                return 1
            return self.validate(i+dir[0], j+dir[1], target + 1, dir)
        return 0
    
sol = Solution()

l1 = sol.get_input('./2024/4/input.txt')
stime = time.time_ns()
print('Part One: ', sol.part_one(l1))
etime = time.time_ns()
print("1 -- took {} ms".format((etime - stime) // 1000000))

stime = time.time_ns()        
print('Part Two: ', sol.part_two(l1))
etime = time.time_ns()
print("2 -- took {} ms".format((etime - stime) // 1000000))