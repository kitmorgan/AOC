import time
from functools import cache


@cache
def convert_stone(val):
    if val == '0':
        return ('1', False)
    elif len(val) % 2 == 0:
        first_half = val[:len(val)//2]
        second_half = val[len(val)//2:]

        if second_half[0] == '0':
            second_half = str(int(second_half))

        return (first_half, second_half)
    else:
        return (str(int(val) * 2024), False)


class LinkedList:
    def __init__(self, val='x', next=None):
        self.val = val
        self.next = next


class Solution:
    def get_input(self, file_path):
        with open(file_path, 'r') as f:
            return f.read().strip().split()

    def process_stones(self, rem: int, stones: list[str]) -> int:

        if not rem:
            return len(stones)
        inserts = []  # (ind, val)
        for i, stone in enumerate(stones):  # do i need to check every stone, yes

            if stone == '0':
                stones[i] = '1'
            elif len(stone) % 2 == 0:
                first_half = stones[i][:len(stones[i])//2]
                second_half = stones[i][len(stones[i])//2:]

                while second_half[0] == '0' and len(second_half) > 1:  # slow
                    second_half = second_half[1:]

                stones[i] = first_half
                inserts.append((second_half, i+1))

            else:
                stones[i] = str(int(stones[i]) * 2024)

        # very slow, faster ways to insert (linked list) 1,20,3,4 -> 1, 2, 0, 3, 4 but i really just need the len (len only changes on even len stones)
        for val, ind in inserts:
            # ll, but how do you track length
            stones.insert(ind, val)
        return self.process_stones(rem - 1, stones)

    def process_linked_stones(self, rem, stone: LinkedList, length):
        print(rem)
        if not rem:
            return length
        head = stone
        while stone:
            val = stone.val
            out = convert_stone(val)
            if out[1] == False:
                stone.val = out[0]
            else:
                stone.val = out[0]
                n = stone.next
                stone.next = LinkedList(out[1], n)
                length += 1
                stone = stone.next
            # if val == '0':
            #     stone.val = '1'
            # elif len(val) % 2 == 0:
            #     first_half = val[:len(val)//2]
            #     second_half = val[len(val)//2:]

            #     while second_half[0] == '0' and len(second_half) > 1: # slow
            #         second_half = second_half[1:]

            #     stone.val = first_half
            #     next_next = stone.next
            #     stone.next = LinkedList(second_half, next_next)
            #     length += 1
            #     stone = stone.next

            # else:
            #     stone.val = str(int(stone.val) * 2024)
            stone = stone.next
        return self.process_linked_stones(rem-1, head, length)
    @cache
    def process_single_stone(self, rem, stone):
        if rem == 0:
            return 0
        cnt_stones = 0
        if stone == '0':
            cnt_stones = self.process_single_stone(rem-1, '1')
        elif len(stone) % 2 == 0:
            cnt_stones = 1 + \
                          self.process_single_stone(rem-1, str(int(stone[:len(stone)//2]))) + \
                          self.process_single_stone(rem-1, str(int(stone[len(stone)//2:])))
        else:
            cnt_stones = self.process_single_stone(
                rem-1, str(int(stone) * 2024))

        return cnt_stones


sol = Solution()

stones = sol.get_input('./11.txt')
# stime = time.time_ns()
# print(sol.process_stones(25, stones))
# etime = time.time_ns()
# print("1 -- took {} ms".format((etime - stime) // 1000000))

stones_2 = sol.get_input('./11.txt')

stime = time.time_ns()
ans = len(stones_2)
for stone in stones_2:
    ans += sol.process_single_stone(75, stone)
etime = time.time_ns()                                    
print("2 -- ans: {} took {} ms".format(ans, (etime - stime) // 1000000))
