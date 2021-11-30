from random import randrange


def generate(file_name, lines=10, max_variables=10, max_in_line=3):
    with open(file_name+".cnf", "w") as f:
        print("Creating new data file")

        used = []
        for i in range(lines):
            # na razie suma trzech w każdej linii
            j = 0
            # minimalnie dwa polaczenia
            while j < randrange(max_in_line-1)+2:
                r = randrange(max_variables*2) - max_variables
                if r != 0 and not used.__contains__(r):
                    used.append(r)
                    f.write(str(r) + ' ')
                    j += 1

            f.write(str(0) + '\n')
            used = []


def load(file_name):
    with open(file_name, "r") as f:
        # next(f) # pominięcie pierwszej linii
        array = []
        for line in f:  # odczytanie pozostałych linii
            array += ([int(x) for x in line.split()])
    return array