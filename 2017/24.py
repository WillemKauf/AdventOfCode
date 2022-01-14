def read_input():
    input_lst = []
    with open("input/input24.txt") as input_file:
        for line in input_file:
            input_lst.append([int(i) for i in line.rstrip().split("/")])
    return input_lst

def part_1(input_lst):
    def recursive_solve(bridge, ports):
        max_strength = sum([sum(p) for p in bridge])
        for port in ports:
            prev_port = bridge[-1][1]
            if port[0] == prev_port:
                new_ports = list(ports)
                new_ports.remove(port)
                max_strength = max(max_strength, recursive_solve(bridge+[port], new_ports))
            elif port[1] == prev_port:
                new_ports = list(ports)
                new_ports.remove(port)
                max_strength = max(max_strength, recursive_solve(bridge+[port[::-1]], new_ports))
        return max_strength

    max_strength = -1
    for port in input_lst:
        if port[0] == 0:
            new_ports = list(input_lst)
            new_ports.remove(port)
            max_strength = max(max_strength, recursive_solve([port], new_ports))
        elif port[1] == 0:
            new_ports = list(input_lst)
            new_ports.remove(port)
            max_strength = max(max_strength, recursive_solve([port[::-1]], new_ports))
    return max_strength

def part_2(input_lst):
    def recursive_solve(bridge, ports):
        max_length   = len(bridge)
        max_strength = sum([sum(p) for p in bridge])
        for port in ports:
            prev_port = bridge[-1][1]
            if port[0] == prev_port:
                new_ports = list(ports)
                new_ports.remove(port)
                new_length, new_strength = recursive_solve(bridge+[port], new_ports)
                if new_length >= max_length:
                    max_length   = new_length
                    max_strength = new_strength
            elif port[1] == prev_port:
                new_ports = list(ports)
                new_ports.remove(port)
                new_length, new_strength = recursive_solve(bridge+[port[::-1]], new_ports)
                if new_length >= max_length:
                    max_length   = new_length
                    max_strength = new_strength
        return max_length, max_strength

    max_length = -1
    max_strength = -1
    for port in input_lst:
        if port[0] == 0:
            new_ports = list(input_lst)
            new_ports.remove(port)
            new_length, new_strength = recursive_solve([port], new_ports)
            if new_length >= max_length:
                max_length   = new_length
                max_strength = new_strength
        elif port[1] == 0:
            new_ports = list(input_lst)
            new_ports.remove(port)
            new_length, new_strength = recursive_solve([port[::-1]], new_ports)
            if new_length >= max_length:
                max_length   = new_length
                max_strength = new_strength
    return max_strength

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
