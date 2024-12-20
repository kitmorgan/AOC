from collections import defaultdict
class Solution:
    def __init__(self, file_path):
        self.grid = []
        with open(file_path,'r') as f:
            self.start = None
            self.directions = []

            section = 1
            
            for i,l in enumerate(f):
                if l == "\n":
                    section = 2
                    continue
                if section == 1:
                    self.grid.append(list(l.strip())[1:len(l)-2])
                    if not self.start:
                        try:
                            self.start = (i-1, l.index('@') - 1)
                        except:
                            continue
                else:
                    self.directions += list(l.strip())
                
        self.grid = self.grid[1:len(self.grid)-1]
        self.M = len(self.grid)
        self.N = len(self.grid[0])
        self.dirs = { '^' : (-1,0), '>' : (0,1), 'v' : (1,0), '<' : (0,-1) }

    def get_gps(self, pos:tuple[int,int]) -> int:
        return 100 * pos[0] + pos[1]
    
    def inbounds(self, pos):
        if pos == (0,6):
            pass
        return 0 <= pos[0] < self.M and 0 <= pos[1] < self.N
            
    def can_move(self, pos, dir):
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if self.inbounds(next):
            ch = self.grid[next[0]][next[1]]
            if ch == '.':
                return next
            if ch == '#':
                return False
            if ch == 'O':
                return self.can_move(next, dir) # @ o o .
        return False

    def print_grid(self):
        for x in self.grid:
            print(x)

    def move(self, start, end, prev = '.'):
        inc = 0
        if end[0] > start[0]:
            inc = 1
        if end[0] < start[0]:
            inc = -1
        
        jnc = 0
        if end[1] > start[1]:
            jnc = 1
        if end[1] < start[1]:
            jnc = -1
        
    
        # self.print_grid()
        # print('-----')
        for i in range(start[0], end[0] + inc, -1 if end[0] < start[0] else 1): #0 - 0 # 3-0
            tmp = self.grid[i][start[1]]
            self.grid[i][start[1]] = prev
            prev = tmp
            # self.print_grid()
            # print('-----')
        for j in range(start[1], end[1] + jnc, -1 if end[1] < start[1] else 1): # 1-3
            tmp = self.grid[start[0]][j]
            self.grid[start[0]][j] = prev 
            prev = tmp
            # self.print_grid()

            print('-----')
    
    def part_one(self):
        robot = self.start
        for inst in self.directions:
            dir = self.dirs[inst]
            di, dj = dir
            moving = True
            curr = robot # 1,1 > 1,2
            end = self.can_move(curr,dir)
            if end != False:
                self.move(curr,end)
                robot = (robot[0] + di, robot[1] + dj)
        ans = 0
        for i in range(self.M):
            for j in range(self.N):
                if self.grid[i][j] == 'O':
                    ans += self.get_gps((i+1,j+1))
        self.print_grid()
        print('one_ans', ans)
                    
s = Solution('./15.txt')
s.part_one()