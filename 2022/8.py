def read_input():
    input_arr = []
    with open("input/input8.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            curr_arr = [int(i) for i in line]
            input_arr.append(curr_arr)
    return input_arr

def get_left_max_array(arr):
    max_arr = []
    running_max = -1
    for i,n in enumerate(arr):
        if running_max == -1:
            running_max = n
        elif n > running_max:
            running_max = max(running_max, n)
        else:
            if running_max in arr[:i]:
                running_max += 1
        max_arr.append(running_max)
    return max_arr

def get_right_max_array(arr):
    max_arr = []
    running_max = -1
    for i,n in enumerate(arr[::-1]):
        if running_max == -1:
            running_max = n
        elif n > running_max:
            running_max = max(running_max, n)
        else:
            if running_max in arr[::-1][:i]:
                running_max += 1
        max_arr.append(running_max)
    return max_arr[::-1]

def get_column(input_arr, i):
    col = []
    for j in range(0, len(input_arr)):
        col.append(input_arr[j][i])
    return col

def part1(input_arr):
    m = len(input_arr)
    n = len(input_arr[0])
    res = 2*m+2*n-4
    for j in range(1, m-1):
        for i in range(1, n-1):
            c = input_arr[j][i]
            col = get_column(input_arr, i)
            row = input_arr[j]
            left_max_col = get_left_max_array(col)
            left_max_row = get_left_max_array(row)
            right_max_col = get_right_max_array(col)
            right_max_row = get_right_max_array(row)
            if c >= left_max_col[j]:
                res += 1
                continue
            if c >= left_max_row[i]:
                res += 1
                continue
            if c >= right_max_col[j]:
                res += 1
                continue
            if c >= right_max_row[i]:
                res += 1
    return res

def valid(i,j,n,m):
    return 0 <= i < n and 0 <= j < m

def part2(input_arr):
    m = len(input_arr)
    n = len(input_arr[0])
    ddir = [[0,-1],[-1,0],[1,0],[0,1]]
    max_res = -1
    for j in range(0, m):
        for i in range(0, n):
            c = input_arr[j][i]
            res = [0]*len(ddir)
            for k, dd in enumerate(ddir):
                ii = i + dd[0]
                jj = j + dd[1]
                while valid(ii,jj,n,m):
                    if input_arr[jj][ii] < c:
                        res[k] += 1
                    else:
                        res[k] += 1
                        break
                    ii += dd[0]
                    jj += dd[1]
            if(i,j)==(2,2):
                print(i,j,c, res,res[0]*res[1]*res[2]*res[3])
            max_res = max(max_res, res[0]*res[1]*res[2]*res[3])
    return max_res


def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()
