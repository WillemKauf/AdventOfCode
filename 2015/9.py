import collections
import numpy as np

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, node_name):
        for node in self.nodes:
            if node.name == node_name:
                return node

class Node:
    def __init__(self, name, rho=0.5):
        self.name       = name
        self.rho        = rho
        self.neighbours = {}
        self.cost       = {}
        self.pheromone  = {}
        self.dpheromone = {}

    def add_neighbour(self, neighbour, dist):
        dist = int(dist)
        self.neighbours[neighbour]  = dist
        self.cost[neighbour]        = 1/dist
        self.pheromone[neighbour]   = 1
        self.dpheromone[neighbour]  = 0

    def update_node(self):
        for neighbour in self.neighbours.keys():
            self.pheromone[neighbour]  = (1 - self.rho)*self.pheromone[neighbour] + self.dpheromone[neighbour]
            self.dpheromone[neighbour] = 0

def read_input():
    graph = Graph()
    with open("input/input9.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            city_A, _, city_B, _, dist = line
            if city_A in [node.name for node in graph.nodes]:
                for index, node in enumerate(graph.nodes):
                    if city_A == node.name:
                        node.add_neighbour(city_B, dist)
            else:
                curr_node = Node(city_A)
                curr_node.add_neighbour(city_B, dist)
                graph.add_node(curr_node)
            if city_B in [node.name for node in graph.nodes]:
                for index, node in enumerate(graph.nodes):
                    if city_B == node.name:
                        node.add_neighbour(city_A, dist)
            else:
                curr_node = Node(city_B)
                curr_node.add_neighbour(city_A, dist)
                graph.add_node(curr_node)
    return graph

def part_1(graph):
    lowest_dist = int(1e6)
    prev_dist   = -1
    num_ants    = 1000
    max_iter    = int(1e3)
    for _ in range(0, max_iter):
        for _ in range(0, num_ants):
            total_cost   = 0
            total_dist   = 0
            initial_city = np.random.choice(graph.nodes)
            seen_cities  = []
            queue        = collections.deque([initial_city])
            while(queue):
                curr_city = queue.pop()
                seen_cities.append(curr_city.name)
                if len(seen_cities) == len(graph.nodes):
                    lowest_dist = min(lowest_dist, total_dist)
                    for i in range(0, len(seen_cities)-1):
                        first_city  = seen_cities[i]
                        second_city = seen_cities[i+1]
                        graph.get_node(first_city).dpheromone[second_city] += total_cost
                        graph.get_node(second_city).dpheromone[first_city] += total_cost
                    break
                prob_map  = {}
                denom     = 0
                possible_cities = [city for city in curr_city.neighbours.keys() if city not in seen_cities]

                for neighbour in possible_cities:
                    prob_map[neighbour] = curr_city.cost[neighbour]*curr_city.pheromone[neighbour]
                    denom += prob_map[neighbour]

                for neighbour in prob_map:
                    prob_map[neighbour] /= denom
                weights   = [prob_map[neighbour] for neighbour in possible_cities]
                next_city = np.random.choice(possible_cities, p=weights)
                total_cost += curr_city.cost[next_city]
                total_dist += curr_city.neighbours[next_city]
                queue.append(graph.get_node(next_city))

        for node in graph.nodes:
            node.update_node()

        if lowest_dist == prev_dist:
            break
        prev_dist = lowest_dist
    return lowest_dist

def part_2(graph):
    highest_dist = -500
    prev_dist   = -1
    num_ants    = 1000
    max_iter    = int(1e3)
    for _ in range(0, max_iter):
        for _ in range(0, num_ants):
            total_cost   = 0
            total_dist   = 0
            initial_city = np.random.choice(graph.nodes)
            seen_cities  = []
            queue        = collections.deque([initial_city])
            while(queue):
                curr_city = queue.pop()
                seen_cities.append(curr_city.name)
                if len(seen_cities) == len(graph.nodes):
                    highest_dist = max(highest_dist, total_dist)
                    for i in range(0, len(seen_cities)-1):
                        first_city  = seen_cities[i]
                        second_city = seen_cities[i+1]
                        graph.get_node(first_city).dpheromone[second_city] += total_cost
                        graph.get_node(second_city).dpheromone[first_city] += total_cost
                    break
                prob_map  = {}
                denom     = 0
                possible_cities = [city for city in curr_city.neighbours.keys() if city not in seen_cities]

                for neighbour in possible_cities:
                    prob_map[neighbour] = curr_city.cost[neighbour]*curr_city.pheromone[neighbour]
                    denom += prob_map[neighbour]

                for neighbour in prob_map:
                    prob_map[neighbour] /= denom
                weights = [prob_map[neighbour] for neighbour in possible_cities]
                weights = np.reciprocal(weights)
                weights /= np.sum(weights)
                next_city = np.random.choice(possible_cities, p=weights)
                total_cost += curr_city.cost[next_city]
                total_dist += curr_city.neighbours[next_city]
                queue.append(graph.get_node(next_city))

        for node in graph.nodes:
            node.update_node()

        if highest_dist == prev_dist:
            break
        prev_dist = highest_dist
    return highest_dist

def main():
    graph = read_input()
    print(part_1(graph))
    print(part_2(graph))

main()

