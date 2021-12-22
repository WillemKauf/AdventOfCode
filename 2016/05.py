import hashlib

def read_input():
    with open("input/input5.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str):
    num = 0
    password = []
    for i in range(0, 8):
        while True:
           num += 1
           combined_str = input_str+str(num)
           result = hashlib.md5(combined_str.encode())
           hex_str = result.hexdigest()
           hexZeros = hex_str[:5]
           if hexZeros == "00000":
               hexChar = hex_str[5]
               break
        password.append(hexChar)
    password = "".join(password)
    return password

def part_2(input_str):
    num = 0
    password = [None for i in range(8)]
    while True:
        combined_str = input_str+str(num)
        result = hashlib.md5(combined_str.encode())
        hex_str = result.hexdigest()
        hex_zeros = hex_str[:5]
        hex_location = None
        if hex_zeros == "00000":
            if hex_str[5] in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                hex_location = int(hex_str[5])
                hex_char = hex_str[6]
        if hex_location != None:
            if password[hex_location] == None:
                password[hex_location] = hex_char
        if None not in password:
            return "".join(password)
        num += 1
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
