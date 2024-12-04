class Solution:
    def get_input(self, file_path):
        l1 = []
        with open(file_path, 'r') as f:
            for line in f:
                l1 += line
        return l1
    
    def find_muls(self,l):
        # whenever we see mul( add everything to curr until a )
        # if that splits evenly into two nums then multiply and add prods to list
        curr = ""
        nums = ""
        products = []
        i = 0
        while i < len(l):
            curr += l[i]
            i += 1
            if curr.endswith("mul("):
                n = ""
                while i < len(l) and (l[i].isdigit() or l[i] == ","):
                    n += l[i]
                    i += 1
                if i < len(l) and l[i] ==')':
                    x = n.split(",")
                    if len(x) == 2:
                        products.append(int(x[0]) * int(x[1]))
        return sum(products)
    
    def part_two(self,l):
    # whenever we see mul( add everything to curr until a )
        # if that splits evenly into two nums then multiply and add prods to list
        #part two add boolean DO
        curr = ""
        nums = ""
        products = []
        i = 0
        do = True
        while i < len(l):
            curr += l[i]
            i += 1
            if curr.endswith("do()"):
                do = True
            if curr.endswith("don't()"):
                do = False
            if curr.endswith("mul("):
                n = ""
                while i < len(l) and (l[i].isdigit() or l[i] == ","):
                    n += l[i]
                    i += 1
                if i < len(l) and l[i] ==')' and do == True:
                    x = n.split(",")
                    if len(x) == 2:
                        products.append(int(x[0]) * int(x[1]))
        return sum(products)
sol = Solution()

l1 = sol.get_input('./2024/3/input.txt')
print(sol.part_two(l1))