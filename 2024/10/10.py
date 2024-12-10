import copy


class Solution:
    def get_input(self, file_path):
        with open(file_path, 'r') as f:
            return [list(map(int, line.strip())) for line in f]

    def part_one(self, grid, pos, flag):
        # recursive loop with curr_pos
        M = len(grid)
        N = len(grid[0])
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        curr = grid[pos[0]][pos[1]]
        if curr == 9:
            if flag == 1:
                grid[pos[0]][pos[1]] = -2
            return 1
        trails = 0
        for dir in dirs:
            di = pos[0] + dir[0]
            dj = pos[1] + dir[1]
            if di >= 0 and dj >= 0 and di < M and dj < N and grid[di][dj] == curr + 1:
                trails += self.part_one(grid, (di, dj), flag)
        return trails


sol = Solution()

grid = sol.get_input('./10.txt')
ans1 = 0
ans2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            ans1 += sol.part_one(copy.deepcopy(grid), (i, j), 1)
            ans2 += sol.part_one(copy.deepcopy(grid), (i,j), 2)
print("PART ONE:", ans1)
print("PART TWO:", ans2)