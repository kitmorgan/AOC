'''
0,1,2,3 -> 0(1), 2(3) 

Combo operands 0 through 3 represent literal values 0 through 3.
Combo operand 4 represents the value of register A.
Combo operand 5 represents the value of register B.
Combo operand 6 represents the value of register C.
Combo operand 7 is reserved and will not appear in valid programs.

Op codes
ADV 0 -- div A/2^ComboOp -> int A
BXL 1 -- xor B ^ literal op -> B
bst 2 -- comboOp % 8 -> B
jnz 3 -- does some crazy stuff
bxc 4 -- B ^ C -> B (ignores an operand)
out 5 -- comboOp % 8 -> 
bdv 6 -- div A/2^ComboOp -> B
cdv 7 -- div A/2^ComboOp --> C

'''

class Solution:
    def __init__(self, file_path):
        self.registers = {'A':0,'B':0,'C':0}
        self.program = None
        self.out = []
        with open(file_path,'r') as f:
            for l in f:
                if l == "\n":
                    continue
                line = l.strip().split(':')
                if   line[0][-1] == 'A':
                    self.registers['A'] = int(line[1])
                elif line[0][-1] == 'B':
                    self.registers['B'] == int(line[1])
                elif line[0][-1] == 'C':
                    self.registers['C'] == int(line[1])
                else:
                    self.program = line[1].strip().split(',')
                    
    def com_0(self,comboOp):
        self.registers['A'] = self.registers['A'] >> comboOp
    
    def com_1(self, litOp):
        self.registers['B'] ^= litOp
        
    def com_2(self, comboOp):
        self.registers['B'] = comboOp % 8
        
    def com_3(self, litOp): # jump
        if self.registers['A'] == 0:
            return -1
        return litOp  
    
    def com_4(self, comboOp):
        self.registers['B'] ^= self.registers['C']
    
    def com_5(self, comboOp):
        self.out.append(comboOp % 8)

    def com_6(self, comboOp):
        self.registers['B'] = self.registers['A'] >> comboOp
        
    def com_7(self, comboOp):
        self.registers['C'] = self.registers['A'] >> comboOp
    
    def operator(self, combo, func_num):
        if func_num == '1' or combo in ('0123'):
            return int(combo)
        else:
            if combo == '4':
                return self.registers['A']
            elif combo == '5':
                return self.registers['B']
            elif combo == '6':
                return self.registers['C']
        print('somethings wrong', combo, func_num)
        
    def part_one(self):
        functions = {'0' : self.com_0, '1': self.com_1, '2':self.com_2, '3':self.com_3, '4': self.com_4, '5':self.com_5, '6': self.com_6, '7':self.com_7}
        pointer = 0
        try:
            while pointer < len(self.program):
                command = self.program[pointer]
                if command != '3' or self.registers['A'] == 0:
                    pointer += 1
                    functions[command](self.operator(self.program[pointer],command))
                    pointer += 1
                else:
                    pointer = int(self.program[pointer + 1])
                    
        except IndexError:
            print('Out',self.out)
        print(self.registers)

s = Solution('./17.txt')
s.part_one()
print('Part One:', ','.join([str(x) for x in s.out]))