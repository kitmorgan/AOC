from collections import defaultdict
from itertools import combinations


class Solution:
    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            for l in f:
                line = l.strip()
                l1.append(list(line))
        return l1

    def part_one(self, l1):
        node_map = self.find_antennas(l1)
        set_coords = set()
        for unique, locs in node_map.items():
            if len(locs) > 1:
                for loc_a, loc_b in combinations(locs, 2):
                    locs = self.find_antinodes(l1, loc_a, loc_b)
                    for loc in locs:
                        set_coords.add(loc)
        for i, j in set_coords:
            l1[i][j] = "#"
        for l in l1:
            print(''.join(l))
        return len(set_coords)

    def find_antinodes(self, l1, loc1, loc2):
        M = len(l1)
        N = len(l1[0])
        i, j = loc1
        y, x = loc2
        anti_nodes = []
        anti_a = (i + i - y, j + j - x)
        anti_b = (y + y - i, x + x - j)
        for anti in [anti_a, anti_b]:
            if anti[0] >= 0 and anti[0] < M and anti[1] >= 0 and anti[1] < N:
                anti_nodes.append(anti)
        return anti_nodes

    def find_antennas(self, l1):
        node_map = defaultdict(list)
        for i in range(len(l1)):
            for j in range(len(l1[0])):
                ch = l1[i][j]
                if ch != '.':
                    node_map[ch].append((i, j))
        return node_map

    def part_two(self,l1):
        node_map = self.find_antennas(l1)
        set_coords = set()
        for unique, locs in node_map.items():
            for loc_a, loc_b in combinations(locs, 2):
                locs = self.find_antinodes_2(l1, loc_a, loc_b)
                for loc in locs:
                    set_coords.add(loc)
                set_coords.add(loc_a)
                set_coords.add(loc_b)

        for i, j in set_coords:
            l1[i][j] = "#"
        for l in l1:
            print(''.join(l))
        return len(set_coords)

    def find_antinodes_2(self, l1, loc1, loc2):
        M = len(l1)
        N = len(l1[0])
        i, j = loc1
        y, x = loc2
        anti_nodes = set()
        q = [([i,j], i-y,j-x) ,([y,x],y-i, x-j)]
        while q:
            anti, di,dj = q.pop()
            anti[0] += di
            anti[1] += dj
            if anti[0] >= 0 and anti[0] < M and anti[1] >= 0 and anti[1] < N:
                anti_nodes.add(tuple(anti))
                q.append((anti,di,dj))
        return anti_nodes
    
sol = Solution()
l1 = sol.get_input('./8.txt')
# ans1 = sol.part_one(l1)

# print('Part one', ans1)

ans2 = sol.part_two(l1)
print('Part two', ans2)