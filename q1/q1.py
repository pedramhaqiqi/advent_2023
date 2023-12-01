def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def find_number_in_line(line ,reverse=False):
    if reverse:
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                return (i, line[i])
    else:
        for i in range(len(line)):
            if line[i].isdigit():
                return (i, line[i])
    


def main():
    code_numbers = []
    for line in read_file('q1.txt'):
        result_forwards = find_number_in_line(line, reverse=False)
        result_backwards = find_number_in_line(line, reverse=True)

        forwards_index = result_forwards[0]
        backwaeds_indx = result_backwards[0]

        if forwards_index == backwaeds_indx:
            code_numbers.append(result_forwards[1])
        else: 
            code_numbers.append(f"{result_forwards[1]}{result_backwards[1]}")
    sum = 0
    [sum := sum + int(i) for i in code_numbers]  
    print(code_numbers)
   

if __name__ == "__main__":
    main()
