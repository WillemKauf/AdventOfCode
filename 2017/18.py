from collections import defaultdict, deque

class Program:
    def __init__(self, input_lst, p_ID):
        self.tape      = input_lst
        self.regs      = defaultdict(int)
        self.p_ID      = p_ID
        self.regs["p"] = p_ID
        self.status    = "Running"
        self.input     = deque([])
        self.index     = 0
        self.n         = len(self.tape)
        self.sent      = 0

    def parse_tape(self):
        if self.status == "Waiting":
            yield False
        while self.index < self.n:
            cmd = self.tape[self.index]
            op = cmd[0]
            if op == "snd":
                a = cmd[1]
                if a.islower():
                    snd = self.regs[a]
                else:
                    snd = a
                self.sent  += 1
                self.index += 1
                yield snd
            elif op == "set":
                a, b = cmd[1:]
                if b.islower():
                    self.regs[a] = self.regs[b]
                else:
                    self.regs[a] = int(b)
            elif op == "add":
                a, b = cmd[1:]
                if b.islower():
                    self.regs[a] += self.regs[b]
                else:
                    self.regs[a] += int(b)
            elif op == "mul":
                a, b = cmd[1:]
                if b.islower():
                    self.regs[a] *= self.regs[b]
                else:
                    self.regs[a] *= int(b)
            elif op == "mod":
                a, b = cmd[1:]
                if b.islower():
                    self.regs[a] = self.regs[a] % self.regs[b]
                else:
                    self.regs[a] = self.regs[a] % int(b)
            elif op == "rcv":
                a = cmd[1]
                if not len(self.input):
                    self.status = "Waiting"
                    yield False
                else:
                    self.regs[a] = self.input.popleft()
            elif op == "jgz":
                a, b = cmd[1:]
                if a.islower():
                    if self.regs[a] > 0:
                        if b.islower():
                            self.index += self.regs[b]-1
                        else:
                            self.index += int(b)-1
                else:
                    if int(a) > 0:
                        if b.islower():
                            self.index += self.regs[b]-1
                        else:
                            self.index += int(b)-1
            self.index += 1
        self.status = "Terminated"

    def get_input(self, inp):
        self.input.append(inp)
        if self.status == "Waiting":
            self.status = "Running"

def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip().split())
    return input_lst

def part_1(input_lst):
    regs = defaultdict(int)
    i = 0
    n = len(input_lst)
    while i < n:
        cmd = input_lst[i]
        op = cmd[0]
        if op == "snd":
            a = cmd[1]
            if a.islower():
                snd = regs[a]
            else:
                snd = a
        elif op == "set":
            a, b = cmd[1:]
            if b.islower():
                regs[a] = regs[b]
            else:
                regs[a] = int(b)
        elif op == "add":
            a, b = cmd[1:]
            if b.islower():
                regs[a] += regs[b]
            else:
                regs[a] += int(b)
        elif op == "mul":
            a, b = cmd[1:]
            if b.islower():
                regs[a] *= regs[b]
            else:
                regs[a] *= int(b)
        elif op == "mod":
            a, b = cmd[1:]
            if b.islower():
                regs[a] = regs[a] % regs[b]
            else:
                regs[a] = regs[a] % int(b)
        elif op == "rcv":
            a = cmd[1]
            if regs[a] != 0:
                return snd
        elif op == "jgz":
            a, b = cmd[1:]
            if a.islower():
                if regs[a] > 0:
                    if b.islower():
                        i += regs[b]-1
                    else:
                        i += int(b)-1
            else:
                if int(a) > 0:
                    if b.islower():
                        i += regs[b]-1
                    else:
                        i += int(b)-1
        i += 1

def part_2(input_lst):
    p1 = Program(input_lst, 0)
    p2 = Program(input_lst, 1)
    output_dct = {1:deque([]), 2:deque([])}
    bad_states = ["Waiting", "Terminated"]
    while p1.status not in bad_states and p2.status not in bad_states:
        output1 = next(p1.parse_tape())
        output2 = next(p2.parse_tape())
        if output1 != False:
            output_dct[1].append(output1)
        else:
            if len(output_dct[2]):
                p1.get_input(output_dct[2].popleft())
        if output2 != False:
            output_dct[2].append(output2)
        else:
            if len(output_dct[1]):
                p2.get_input(output_dct[1].popleft())
    return p2.sent

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
