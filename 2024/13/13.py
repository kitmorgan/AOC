class Solution:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.min_guess = float('inf')
            self.range = [x for x in range(101)]
            a = None
            b = None
            prize = None
            ind = 0
            self.puzzles = []
            for line in f:
                if line.startswith("Button A: "):
                    ax = ""
                    ay = ""
                    first = True
                    for ch in line:
                        if ch.isdigit():
                            ax += ch if first else ""
                            ay += ch if not first else ""
                        if ch == ",":
                            first = False
                    ax = int(ax)
                    ay = int(ay)
                elif line.startswith("Button B: "):
                    bx = ""
                    by = ""
                    first = True
                    for ch in line:
                        if ch.isdigit():
                            bx += ch if first else ""
                            by += ch if not first else ""
                        if ch == ",":
                            first = False
                    bx = int(bx)
                    by = int(by)
                elif line.startswith("Prize:"):
                    x = ""
                    y = ""
                    first = True
                    for ch in line:
                        if ch.isdigit():
                            x += ch if first else ""
                            y += ch if not first else ""
                        if ch == ",":
                            first = False
                    prize = (int(x), int(y))
                    self.puzzles.append((prize, (ax, ay), (bx, by)))
            ''' Button A: X+94, Y+34
                Button B: X+22, Y+67
                Prize: X=8400, Y=5400 '''

            # (prize, (ax,ay) (bx,by))
    def search(self, prize, a, b):
        l = 0
        r = 100
        while l <= r:
            # if Ax < Bx and x_off > y_off -> press A more
            # if Ay < By and x_off > y_off -> press B more
            a_times = (l + r) // 2
            off_by = (prize[0] - a[0] * a_times, prize[1] - a[1] * a_times)
            b_times = off_by[0]//b[0]
            x_off = off_by[0] - (b_times * b[0])
            y_off = off_by[1] - (b_times * b[1])
            # print('atimes',a_times,'btimes',b_times,'off',x_off,y_off, l, r)
            if x_off == 0 and y_off == 0 and b_times >= 0 and b_times <= 100:
                print('ans', a_times, b_times)
                if a == b:
                    return a_times + b_times
                return a_times * 3 + b_times
            if x_off > y_off:
                print('XXXatimes', a_times, 'btimes',
                      b_times, 'off', x_off, y_off, l, r)
                if a[0] > b[0]:
                    l = a_times + 1
                else:
                    r = a_times - 1

            else: # y_off 
                print('atimes', a_times, 'btimes',
                      b_times, 'off', x_off, y_off, l, r, a, b)
                if a[1] > b[1]:
                    l = a_times + 1
                else:
                    r = a_times - 1

    def part_one(self):
        # binary search? 0 -> max(prize/push)
        self.guess = []
        for i, puzzle in enumerate(self.puzzles):
            prize, a, b = puzzle
            ans = self.search(prize, a, b)
            print(prize)
            if ans:
                self.guess.append(ans)
                print(ans)
        # guess - 23832, 24136, 23832 -- too low 
        # when both buttons are the same?
        # when a button changes by 0?
        
        print(sum(self.guess))


# find min A, B such that ax * A  + bx * B = target_x and ay * A + by * B = target_y
#
s = Solution('./13.txt')
print(s.puzzles)
print("Part one: ", s.part_one())
