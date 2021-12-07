import re

def read_input():
    input_file = open("input/input16.txt", "r")
    things_arr = []
    dict_arr = []
    #This sure is old code
    for line in input_file:
        input_dict = {}
        currentLine = line.split()
        thing_one = str(currentLine[2].split(":")[0])
        num_thing_one = int(currentLine[3].split(",")[0])
        thing_two = str(currentLine[4].split(":")[0])
        num_thing_two = int(currentLine[5].split(",")[0])
        thing_three = str(currentLine[6].split(":")[0])
        num_thing_three = int(currentLine[7])
        sue_num = int(currentLine[1].split(":")[0])
        input_dict[thing_one]  = num_thing_one
        input_dict[thing_two]  = num_thing_two
        input_dict[thing_three] = num_thing_three
        if thing_one not in things_arr:
            things_arr.append(thing_one)
        dict_arr.append(input_dict)

    for thing in things_arr:
        for stuff in dict_arr:
            if thing not in stuff.keys():
                stuff[thing] = 999

    match_dict = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}
    return dict_arr, things_arr, match_dict

def part_1(dict_arr, things_arr, match_dict):
    matches_flag = False
    match_arr = []
    for term in dict_arr:
            for thing_name in things_arr:
                if term[thing_name] == match_dict[thing_name] or term[thing_name] == 999:
                    matches_flag = True
                else:
                    matches_flag = False
                    break
            if matches_flag == True:
                return dict_arr.index(term)+1

    return None

def part_2(dict_arr, things_arr, match_dict):
    matches_flag = False
    match_arr = []
    for term in dict_arr:
            for thing_name in things_arr:
                if thing_name == "cats" or thing_name == "trees":
                    if term[thing_name] > match_dict[thing_name] or term[thing_name] == 999:
                        matches_flag = True
                    else:
                        matches_flag = False
                        break
                elif thing_name == "pomeranians" or thing_name == "goldfish":
                    if term[thing_name] < match_dict[thing_name] or term[thing_name] == 999:
                        matches_flag = True
                    else:
                        matches_flag = False
                        break
                else:
                    if term[thing_name] == match_dict[thing_name] or term[thing_name] == 999:
                        matches_flag = True
                    else:
                        matches_flag = False
                        break

            if matches_flag == True:
                return dict_arr.index(term)+1

    return None

def main():
    dict_arr, things_arr, match_dict = readInput()
    print(part_1(dict_arr, things_arr, match_dict))
    print(part_2(dict_arr, things_arr, match_dict))

if __name__ == "__main__":
    main()
