def read_input():
    input_arr = []
    with open("input/input7.txt") as input_file:
        for line in input_file.readlines():
            line = line.rstrip().split()
            input_arr.append(line)
    return input_arr

def solvePuzzle(instructArr, hash_dict):
    """
    &: AND
    |: OR
    ^ 65535: NOT
    <<: LSHIFT
    >>: RSHIFT
    """
    operations = ['RSHIFT', 'OR', 'LSHIFT', 'AND']
    while len(instructArr):
        used_instructs = []
        for instruct in instructArr:
            if len(instruct) == 3:
                try:
                    if instruct[2] not in hash_dict.keys():
                        hash_dict[instruct[2]] = int(instruct[0])
                    used_instructs.append(instruct)
                except:
                    if instruct[0] in hash_dict.keys():
                        hash_dict[instruct[2]] = int(hash_dict[instruct[0]])
                        used_instructs.append(instruct)
            elif instruct[0] == "NOT":
                if instruct[1] in hash_dict.keys():
                    hash_dict[instruct[3]] = hash_dict[instruct[1]] ^ 65535
                    used_instructs.append(instruct)
            elif instruct[1] in operations:
                arg1 = instruct[0]
                oper = instruct[1]
                arg2 = instruct[2]
                tar  = instruct[4]
                if oper == "RSHIFT":
                    if arg1 in hash_dict.keys():
                        hash_dict[tar] = hash_dict[arg1] >> int(arg2)
                        used_instructs.append(instruct)
                elif oper == "LSHIFT":
                    if arg1 in hash_dict.keys():
                        hash_dict[tar] = hash_dict[arg1] << int(arg2)
                        used_instructs.append(instruct)
                elif oper == "OR":
                    if arg1 in hash_dict.keys() and arg2 in hash_dict.keys():
                        hash_dict[tar] = hash_dict[arg1] | hash_dict[arg2]
                        used_instructs.append(instruct)
                elif oper == "AND":
                    if arg1 in hash_dict.keys() and arg2 in hash_dict.keys():
                        hash_dict[tar] = hash_dict[arg1] & hash_dict[arg2]
                        used_instructs.append(instruct)
                    elif arg2 in hash_dict.keys() and arg1 in list("123456789"):
                        hash_dict[tar] = int(arg1) & hash_dict[arg2]
                        used_instructs.append(instruct)
                    elif arg1 in hash_dict.keys() and arg2 in list("123456789"):
                        hash_dict[tar] = hash_dict[arg1] & int(arg2)
                        used_instructs.append(instruct)
        for used_instruct in used_instructs:
            instructArr.remove(used_instruct)
    return hash_dict["a"]

def main():
    new_b = solvePuzzle(read_input(), {})
    print(new_b)
    print(solvePuzzle(read_input(), {"b":new_b}))

main()

