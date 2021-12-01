class Passport():
    def __init__(self, dct):
        for k, v in dct.items():
            setattr(self, k, v)

def read_input():
    input_arr = []
    with open("input/input4.txt") as i_f:
        curr_str = ""
        for line in i_f:
            line = line.rstrip()
            if line != "":
                curr_str += line.rstrip() + " "
            else:
                input_arr.append(curr_str[:-1])
                curr_str = ""
    if curr_str != "":
        input_arr.append(curr_str[:-1])
    passports = []
    for passport in input_arr:
        dct = {}
        for pair in passport.split(" "):
            k, v = pair.split(":")
            dct[k] = v
        curr_passport = Passport(dct)
        passports.append(curr_passport)
    return passports

def part_1(passports):
    num_valid = 0
    for passport in passports:
        attrs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        if all(map(lambda attr : getattr(passport, attr, None) != None, attrs)):
            num_valid += 1
    return num_valid

def part_2(passports):
    byr_lambda = lambda byr : False if byr == None else 1920 <= int(byr) <= 2002
    iyr_lambda = lambda iyr : False if iyr == None else 2010 <= int(iyr) <= 2020
    eyr_lambda = lambda eyr : False if eyr == None else 2020 <= int(eyr) <= 2030
    hgt_lambda = lambda hgt : False if hgt == None else (hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193) or (hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76)
    hcl_lambda = lambda hcl : False if hcl == None else all([hcl[0] == "#", *[char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                                  "a", "b", "c", "d", "e", "f"] for char in hcl[1:]]])
    ecl_lambda = lambda ecl : False if ecl == None else ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid_lambda = lambda pid : False if pid == None else len(pid) == 9
    num_valid = 0
    for passport in passports:
        attrs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        attr_lambdas = [byr_lambda, iyr_lambda, eyr_lambda, hgt_lambda, hcl_lambda, ecl_lambda, pid_lambda]
        get_attrs = list(map(lambda attr : getattr(passport, attr, None), attrs))
        lst = [attr_lambdas[i](get_attrs[i]) for i in range(0, len(get_attrs))]
        num_valid += int(all([attr_lambdas[i](get_attrs[i]) for i in range(0, len(get_attrs))]))
    return num_valid

def main():
    passports = read_input()
    print(part_1(passports))
    print(part_2(passports))

if __name__ == "__main__":
   main()
