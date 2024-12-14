from collections import defaultdict
class Solution:
    def __init__(self, file_path):
        self.robots = []
        self.M = 103
        self.N = 101
        with open(file_path, 'r') as f:
            for line in f:
                p = ""
                v = ""
                first = True
                for ch in line:
                    if ch not in ['p', ' ', 'v', '=']:
                        p += ch if first else ''
                        v += ch if not first else ''
                    elif ch == 'v':
                        first = False
                self.robots.append(
                    [[int(x) for x in p.split(',')], [int(x) for x in v.split(',')]])

    def part_one(self, time= 100):
        self.quadrants = {'a':0,'b':0,'c':0,'d':0, 'f': 0,'center':0}
        # test
        # self.M = 7
        # self.N = 11
        self.locs = []
        self.rows = defaultdict(int)
        self.max_rows = 0
        for robot in self.robots:
            j,i = robot[0]
            h_speed, v_speed = robot[1]
            j_after = (j + h_speed * time) % self.N
            i_after = (i + v_speed * time) % self.M
            self.quadrants[self.get_quadrant((i_after,j_after))] += 1
            self.locs.append((i_after,j_after))
            self.rows[j_after] += 1
            self.max_rows = max(self.max_rows, self.rows[i_after])
        ans = 1    
        for x in 'abcd':
            ans *= self.quadrants[x]
        # print('Part One:',ans)
        
    def get_quadrant(self, pos):
        if 45 < pos[0] < 65 and 45 < pos[1] < 65:
            return 'center'
        if pos[0] < self.M // 2:
            if pos[1] < self.N // 2: 
                return 'a'
            if pos[1] > self.N // 2:
                return 'b'
        if pos[0] > self.M //2:
            if pos[1] < self.N // 2:
                return 'c'
            if pos[1] > self.N // 2:
                return 'd'
        return 'f'
    def part_two(self):
        
        i = 0
        while i < 10000:
            self.part_one(i)
            i+=1
            #if all([self.rows[x] >= 15 for x in range(40,60)]):
            if self.max_rows > 30:
                grid = [['.' for _ in range(self.N)] for _ in range(self.M)]
                for pos in self.locs:
                    grid[pos[0]][pos[1]] = 'x'
                j = 0
                for layer in grid:
                    j+= 1
                    if j > 40:
                        file_name = './trees/' + str(i) +'_tree.txt'
                        with open(file_name, 'a') as f:
                            f.write(''.join(layer) +'\n')
        
s = Solution('./14.txt')
s.part_one()
s.part_two()
