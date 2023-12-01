def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()



def main():
    for line in read_file('q1.txt'):
        pass

if __name__ == "__main__":
    main()
