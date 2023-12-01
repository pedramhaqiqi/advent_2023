# A list of number mappings in words from 1 - 9
numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six' : 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_string_in_line(line, reverse=False):
    for key in numbers.keys():
        if reverse:
            index = line.rfind(key)
            if index != -1:
                return (index, key)
        else:
            index = line.find(key)
            if index != -1:
                return (index, key)
    return (-1, -1)

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
    return (-1, -1)



def main():
    code_numbers = []
    for line in read_file('q1.txt'):
        result_forwards = find_number_in_line(line, reverse=False)
        result_backwards = find_number_in_line(line, reverse=True)

        result_string_forwards = find_string_in_line(line, reverse=False)
        result_string_backwards = find_string_in_line(line, reverse=True)

        forwards_string_index = result_string_forwards[0]
        backwards_string_index = result_string_backwards[0]

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
