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
                if r != 0 and not used.__contains__(abs(r)):
                    used.append(abs(r))
                    f.write(str(r) + ' ')
                    j += 1

            f.write(str(0) + '\n')
            used = []


def load(file_name):
    data = [4]
    with open(file_name, "r") as f:
        array = [] #Utworzenie tablicy z danymi o pliku [p cnf X Y]
        for line in f:  
            if line.startswith('c') or line.startswith('C') or line in ['', ' ']:
                continue # Pominiecie linii z komentarzami
            if line.startswith('p'):
                data[0] = line.replace('\n','').split(' ') #obsługa lini zaczynającej się od p
            else:
                array += ([int(x) for x in line.split()])

    print(data)
    return array,data
