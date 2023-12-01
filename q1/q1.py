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
    for line in read_file('q1.txt'):
        result = find_number_in_line(line)
        print(result)
        return

if __name__ == "__main__":
    main()
