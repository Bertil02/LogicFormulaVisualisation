from igraph import *


def draw(file_name):
    MAX_WEIGHT = 2

    # grubość połączenia (więcej wyrazów wspólnych -> grubsza linia; brak wyrazów wspólnych -> brak linii)
    weight = 0
    weights = []

    # kolor połączenia (zgodość=100% -> zielony; zgodność>50% -> żółty; zgodność<=50% -> czarny)
    edge_colors = []

    g = Graph()
    names = []

    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append([int(x) for x in line.split()][:-1])

    g.add_vertices(len(lines))
    for current_line in range(len(lines)):
        names.append('C_' + str(current_line+1))
        for previous_line in range(current_line):
            for var in lines[current_line]:
                if var in lines[previous_line]:
                    weight += MAX_WEIGHT/len(lines[current_line])

            if len(lines[current_line]) != len(lines[previous_line]) or weight <= MAX_WEIGHT/2:
                edge_colors.append('black')
            elif weight == MAX_WEIGHT:
                edge_colors.append('green')
            elif weight > MAX_WEIGHT/2:
                edge_colors.append('yellow')

            print('current_line:', current_line+1, 'previous line:', previous_line+1, 'weight:', weight,
                  'edge color:', edge_colors[-1])
            g.add_edge(current_line, previous_line)

            weights.append(weight)
            weight = 0
        print('-' * 60)

    g.vs["color"] = ['green']
    plot(g, bbox=(950, 690), layout=g.layout("fr"), vertex_label=names, edge_width=weights,
         edge_color=edge_colors, color=g.vs["color"])


# przykład działania
# import data
# data.generate('sample', 30)
# draw('sample.cnf')
