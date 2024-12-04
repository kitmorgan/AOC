class Solution:
    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            for line in f:
                l1.append([int(x) for x in line.split()])
        return l1

    def use_ans(self, l):
        ans = 0
        for li in l:
            if self.ans([li]):
                ans += 1
            else:
                perm = self.create_lists(li)
                ans += 1 if self.ans(perm) else 0
        print(ans)

    def create_lists(self, list1):
        return [list1[:i] + list1[i+1:] for i in range(len(list1))]

    def ans(self, x):
        ans = 0
        for line in x:
            prev = line[0]
            inc = None
            valid = True
            for el in line[1:]:
                if prev == el:

                    valid = False
                    break
                if inc is None:

                    inc = 1 if prev < el else -1
                if inc == 1 and (el - prev < 0 or el - prev > 3):

                    valid = False
                    break
                if inc == -1 and (prev - el < 0 or prev - el > 3):

                    valid = False
                    break
                prev = el
            if valid:
                ans += 1
            if ans == 1:
                return True
            valid = True



sol = Solution()

out = sol.get_input('./2024/2/input.txt')
sol.use_ans(out)
