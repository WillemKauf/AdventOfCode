import re
import heapq
from collections import defaultdict

def read_input():
    flowrate_mp = {}
    graph       = defaultdict(set)
    regex = re.compile(r"Valve (\w+) has flow rate=(\d+);")
    with open("input/input16.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            matches = regex.findall(line)
            valve, flowrate = matches[0]
            flowrate_mp[valve] = int(flowrate)
            line = line.split("valve")
            c_valves = line[1][1:]
            if c_valves[0] == " ":
                c_valves = c_valves[1:]
            for c_valve in c_valves.split(", "):
                graph[valve].add(c_valve)
    for k in graph.keys():
        graph[k] = sorted(graph[k], key = lambda v : flowrate_mp[v], reverse=True)
    return flowrate_mp, graph

def part1(flowrate_mp, graph):
    max_flowrate = sum(flowrate_mp.values())
    t = 30
    queue = [(0, t, 0, "AA", set())]
    max_res = -1
    seen_states = {}
    def encode_state(time, node, released):
        released_encode = 0
        for v in released:
            released_encode += 1 << ord(v[0])-ord("A")
            released_encode += 1 << (ord(v[1])-ord("A")+26)
        return (time, node, released_encode)
    while len(queue):
        pressure, time, _, node, released = heapq.heappop(queue)
        pressure *= -1
        state = encode_state(time, node, released)
        max_pressure = pressure + time*max_flowrate
        if max_pressure <= max_res:
            continue
        if time == 0:
            max_res = max(max_res, pressure)
            continue
        for n in released:
            pressure += flowrate_mp[n]
        if state in seen_states:
            if seen_states[state] >= pressure:
                continue
        seen_states[state] = pressure
        if node not in released:
            #Released, stay version
            if flowrate_mp[node] != 0: #Why bother?
                heapq.heappush(queue, (-1*pressure, time-1, -(len(released)+1), node, released | set([node])))
        for neighbour in graph[node]:
            #Non-released, move to neighbour version
            heapq.heappush(queue, (-1*pressure, time-1, -len(released), neighbour, released))
    return max_res

def part2(flowrate_mp, graph):
    max_flowrate = sum(flowrate_mp.values())
    t = 26
    queue = [(0, t, 0, "AA", "AA", set())]
    max_res = -1
    seen_states = {}
    def encode_state(time, node, e_node, released):
        released_encode = 0
        for v in released:
            released_encode += 1 << ord(v[0])-ord("A")
            released_encode += 1 << (ord(v[1])-ord("A")+26)
        return (time, node, e_node, released_encode)

    while len(queue):
        pressure, time, _, node, e_node, released = heapq.heappop(queue)
        pressure *= -1
        state = encode_state(time, node, e_node, released)
        max_pressure = pressure + time*max_flowrate
        if max_pressure <= max_res:
            continue
        if time == 0:
            max_res = max(max_res, pressure)
            continue
        for n in released:
            pressure += flowrate_mp[n]
        if state in seen_states:
            if seen_states[state] >= pressure:
                continue
        seen_states[state] = pressure
        #release node, e travel
        #release e-node, n travel
        #release node, e-node
        if node not in released:
            if flowrate_mp[node] != 0: #Why bother?
                for e_neighbour in graph[e_node]:
                    heapq.heappush(queue, (-1*pressure, time-1, -(len(released)+1), node, e_neighbour, released | set([node])))
        if e_node not in released:
            if flowrate_mp[e_node] != 0: #Why bother?
                for neighbour in graph[node]:
                    heapq.heappush(queue, (-1*pressure, time-1, -(len(released)+1), neighbour, e_node, released | set([e_node])))
        if node not in released and e_node not in released and node != e_node:
            if flowrate_mp[node] != 0 and flowrate_mp[e_node] != 0: #Why bother?
                heapq.heappush(queue, (-1*pressure, time-1, -(len(released)+2), node, e_node, released | set([node, e_node])))
        for neighbour in graph[node]:
            for e_neighbour in graph[e_node]:
                #Non-released, move to neighbour version
                heapq.heappush(queue, (-1*pressure, time-1, -len(released), neighbour, e_neighbour, released)) #Both travel

    return max_res

def main():
    print(part1(*read_input()))
    print(part2(*read_input()))

if __name__ == "__main__":
    main()
