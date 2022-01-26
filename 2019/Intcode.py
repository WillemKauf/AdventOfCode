from collections import defaultdict

class IntCode:
    def __init__(self, tape):
        self.tape          = defaultdict(int, {i:tape[i] for i in range(0, len(tape))})
        self.length        = len(tape)
        self.index         = 0
        self.input         = []
        self.output        = []
        self.status        = "Running"
        self.rank          = None
        self.relative_base = 0

    def set_rank(self, n, rank_as_input):
        self.rank = n
        if rank_as_input:
            self.input = [n]

    def add_input(self, input_lst):
        for i in input_lst:
            self.input.append(i)

    def set_input(self, input_lst):
        self.input = input_lst

    def parse_tape(self):
        if self.status == "Waiting" and len(self.input):
            self.status = "Running"
        while self.index < self.length:
            if self.status != "Running":
                break
            _ = self.parse_code()
        return self.output

    def parse_tape_with_output(self):
        if self.status == "Waiting" and len(self.input):
            self.status = "Running"
        while self.index < self.length:
            if self.status != "Running":
                break
            output = self.parse_code()
            if output != None:
                yield self.output[-1]

    def parse_tape_with_n_output(self, n):
        if self.status == "Waiting" and len(self.input):
            self.status = "Running"
        output_lst = []
        while self.index < self.length:
            if self.status != "Running":
                break
            output = self.parse_code()
            if output != None:
                output_lst.append(output)
            if len(output_lst) == n:
                return output_lst
        return [None]*n

    def read_tape(self, tape_value, mode):
        if mode == 0: #Position mode
            return self.tape[tape_value] #Use tape value as pointer
        elif mode == 1: #Immediate Mode
            return tape_value #Use tape value as value
        elif mode == 2: #Relative Mode
            return self.tape[self.relative_base + tape_value] #Use tape value and relative base as pointer
        else:
            raise ValueError

    def add(self, mode):
        read_p1, read_p2, res_p = [self.tape[self.index+i] for i in range(1,4)]
        val_1, val_2            = self.read_tape(read_p1, mode[0]), self.read_tape(read_p2, mode[1])
        if mode[2] == 2:
            res_p += self.relative_base
        self.tape[res_p] = val_1 + val_2
        self.index += 4

    def multiply(self, mode):
        read_p1, read_p2, res_p = [self.tape[self.index+i] for i in range(1,4)]
        val_1, val_2            = self.read_tape(read_p1, mode[0]), self.read_tape(read_p2, mode[1])
        if mode[2] == 2:
            res_p += self.relative_base
        self.tape[res_p] = val_1 * val_2
        self.index += 4

    def get_input(self, mode):
        if not len(self.input):
            self.status = "Waiting"
            return None
        if mode[0] == 0:
            self.tape[self.tape[self.index+1]] = self.input.pop(0)
        elif mode[0] == 2:
            self.tape[self.relative_base+self.tape[self.index+1]] = self.input.pop(0)
        else:
            raise ValueError
        self.index += 2

    def get_output(self, mode):
        output_val = self.read_tape(self.tape[self.index+1], mode[0])
        self.output.append(output_val)
        self.index += 2

    def jump_if_true(self, mode):
        read_p1, read_p2 = [self.tape[self.index+i] for i in range(1,3)]
        val_1, val_2     = self.read_tape(read_p1, mode[0]), self.read_tape(read_p2, mode[1])
        if val_1 != 0:
            self.index = val_2
        else:
            self.index += 3

    def jump_if_false(self, mode):
        read_p1, read_p2 = [self.tape[self.index+i] for i in range(1,3)]
        val_1, val_2     = self.read_tape(read_p1, mode[0]), self.read_tape(read_p2, mode[1])
        if val_1 == 0:
            self.index = val_2
        else:
            self.index += 3

    def less_than(self, mode):
        read_p1, read_p2, res_p = [self.tape[self.index+i] for i in range(1,4)]
        val_1, val_2       = self.read_tape(read_p1, mode[0]), self.read_tape(read_p2, mode[1])
        res = 1 if val_1 < val_2 else 0
        if mode[2] == 2:
            res_p += self.relative_base
        self.tape[res_p] = res
        self.index += 4

    def equals(self, mode):
        read_p1, read_p2, res_p = [self.tape[self.index+i] for i in range(1,4)]
        val_1, val_2            = self.read_tape(read_p1, mode[0]), self.read_tape(read_p2, mode[1])
        res = 1 if val_1 == val_2 else 0
        if mode[2] == 2:
            res_p += self.relative_base
        self.tape[res_p] = res
        self.index += 4

    def set_relative_base(self, mode):
        self.relative_base += self.read_tape(self.tape[self.index+1], mode[0])
        self.index += 2

    def parse_code(self):
        opcode    = self.tape[self.index]
        A,B,C,D,E = list(str(opcode).zfill(5))
        cmd       = int(D+E)
        mode      = [int(C), int(B), int(A)]
        if cmd == 1:
            self.add(mode)
        elif cmd == 2:
            self.multiply(mode)
        elif cmd == 3:
            self.get_input(mode)
        elif cmd == 4:
            self.get_output(mode)
            return self.output[-1]
        elif cmd == 5:
            self.jump_if_true(mode)
        elif cmd == 6:
            self.jump_if_false(mode)
        elif cmd == 7:
            self.less_than(mode)
        elif cmd == 8:
            self.equals(mode)
        elif cmd == 9:
            self.set_relative_base(mode)
        elif cmd == 99:
            self.status = "Halted"
        else:
            raise ValueError(cmd, self.index, self.tape[self.index])
        return None

class IntCodes():
    def __init__(self, intcode_lst, rank_as_input=False):
        self.ics           = intcode_lst
        self.input_buffer  = defaultdict(list)
        self.output_buffer = defaultdict(list)
        self.length        = len(self.ics)
        for rank, ic in enumerate(self.ics):
            ic.set_rank(rank, rank_as_input)

    def set_input(self, input_dct):
        for n, lst in input_dct.items():
            for input_val in lst:
                self.input_buffer[n].append(input_val)

    def set_n_input(self, rank):
        self.ics[rank].add_input(self.input_buffer[rank])
        self.input_buffer[rank]  = []
        self.output_buffer[rank] = []

    def set_n_output(self, rank):
        for output in self.output_buffer[rank]:
            self.input_buffer[(rank+1)%self.length].append(output)

    def sync_run(self):
        while any([ic.status != "Halted" for ic in self.ics]):
            for ic in self.ics:
                self.set_n_input(ic.rank)
                for output in ic.parse_tape_with_output():
                    self.output_buffer[ic.rank].append(output)
                self.set_n_output(ic.rank)
        return [ic.output for ic in self.ics]

class NICs():
    def __init__(self, intcode_lst, rank_as_input=False):
        self.ics           = intcode_lst
        self.input_buffer  = defaultdict(list)
        self.output_buffer = defaultdict(list)
        self.NAT_buffer    = []
        self.NAT_seen      = set()
        self.length        = len(self.ics)
        for rank, ic in enumerate(self.ics):
            ic.set_rank(rank, rank_as_input)

    def set_input(self, input_dct):
        for n, lst in input_dct.items():
            for input_val in lst:
                self.input_buffer[n].append(input_val)

    def set_n_input(self, rank):
        if not self.input_buffer[rank]:
            self.input_buffer[rank] = [[-1]]
        for i in self.input_buffer[rank]:
            self.ics[rank].add_input(i)
        self.input_buffer[rank]  = []
        self.output_buffer[rank] = []

    def sync_run(self,p2=False):
        while any([ic.status != "Halted" for ic in self.ics]):
            for ic in self.ics:
                self.set_n_input(ic.rank)
                output    = ic.parse_tape_with_n_output(3)
                addr, x,y = output
                if (x,y) != (None, None):
                    if addr == 255:
                        if not p2:
                            return y
                        self.NAT_buffer = [x,y]
                    self.input_buffer[addr].append([x,y])
            if p2:
                if all([ic.status == "Waiting" for ic in self.ics]):
                    self.input_buffer[0].append(self.NAT_buffer)
                    tup_rep = tuple(self.NAT_buffer)
                    if tup_rep in self.NAT_seen:
                        return tup_rep[1]
                    self.NAT_seen.add(tup_rep)
