def read_input():
    input_lst = []
    with open("input/input13.txt") as input_file:
        timestamp = int(input_file.readline().rstrip())
        for line in input_file.readlines():
            for x in line.rstrip().split(","):
                input_lst.append(x)
    return timestamp, input_lst

def part_1(timestamp, input_lst):
    min_wait_time = 9999999
    min_bus_id    = None
    for bus_id in input_lst:
        if bus_id != "x":
            bus_id = int(bus_id)
            curr_wait_time = -(timestamp % bus_id)+bus_id
            if curr_wait_time < min_wait_time:
                min_wait_time = curr_wait_time
                min_bus_id = bus_id
    return min_wait_time*min_bus_id

def part_2(input_lst):
    #I could do Chinese Remainder Theorem. But that's boring.
    highest_num_matched = 0
    highest_dt          = -999
    unique_busses       = [int(i) for i in input_lst if i != "x"]
    num_busses          = len(unique_busses)
    min_bus_id          = min(unique_busses)
    curr_timestamp      = min_bus_id
    dt                  = min_bus_id
    while True:
        matched = []
        for offset, bus_id in enumerate(input_lst):
            if bus_id == "x":
                continue
            bus_id = int(bus_id)
            if (curr_timestamp+offset) % bus_id == 0:
                matched.append(bus_id)
        num_matched = len(matched)
        if num_matched == num_busses:
            return curr_timestamp
        if num_matched >= highest_num_matched:
            highest_num_matched = num_matched
            highest_dt          = 1
            for bus_id in matched:
                highest_dt *= bus_id
        dt = max(highest_dt, dt)
        curr_timestamp += dt

def main():
    timestamp, input_lst = read_input()
    print(part_1(timestamp, input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()
