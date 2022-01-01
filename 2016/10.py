from collections import defaultdict
import heapq

def read_input():
    input_lst = []
    input_dct = defaultdict(list)
    with open("input/input10.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            if line[0] == "bot":
                bot      = int(line[1])
                bot_or_output_low = line[5] == "bot"
                low_bot  = int(line[6])
                bot_or_output_high = line[-2] == "bot"
                high_bot = int(line[-1])
                input_lst.append((bot, low_bot, high_bot, bot_or_output_low, bot_or_output_high))
            elif line[0] == "value":
                val = int(line[1])
                bot = int(line[-1])
                heapq.heappush(input_dct[bot], val)
    return input_dct, input_lst

def part_1(bots, cmds):
    low, high = 17, 61
    output = defaultdict(list)
    while True:
        for cmd in cmds:
            bot, low_bot, high_bot, bot_or_output_low, bot_or_output_high = cmd
            if len(bots[bot]) != 2:
                continue
            low_v, high_v = heapq.heappop(bots[bot]), heapq.heappop(bots[bot])
            if (low_v, high_v) == (low, high):
                return bot
            if bot_or_output_low:
                heapq.heappush(bots[low_bot], low_v)
            else:
                heapq.heappush(output[low_bot], low_v)
            if bot_or_output_high:
                heapq.heappush(bots[high_bot], high_v)
            else:
                heapq.heappush(output[high_bot], high_v)

def part_2(bots, cmds):
    output = defaultdict(list)
    while True:
        for cmd in cmds:
            bot, low_bot, high_bot, bot_or_output_low, bot_or_output_high = cmd
            if len(bots[bot]) != 2:
                continue
            low_v, high_v = heapq.heappop(bots[bot]), heapq.heappop(bots[bot])
            if bot_or_output_low:
                heapq.heappush(bots[low_bot], low_v)
            else:
                heapq.heappush(output[low_bot], low_v)
            if bot_or_output_high:
                heapq.heappush(bots[high_bot], high_v)
            else:
                heapq.heappush(output[high_bot], high_v)
        if all([len(output[0]), len(output[1]), len(output[2])]):
            return output[0][0]*output[1][0]*output[2][0]

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
