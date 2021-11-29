from igraph import *
import data


# podstawowy graf, wyswietla wszystkie polaczenia
def draw(file_name):
    lines = 0
    variables = []
    exp = []
    edges = []
    g = Graph()
    input_string = data.load(file_name)

    for char in input_string:
        if char != 0:
            if char not in variables:
                variables.append(char)

            edges.append([variables.index(char), lines])
        else:
            lines += 1
            exp.append('C_' + str(lines))

    for i in range(len(edges)):
        edges[i] = (edges[i][0], edges[i][1] + len(variables))

    print("expressions:", exp)
    print("variables:", variables)
    print("edges:", edges)

    g.add_vertices(len(exp) + len(variables))
    g.vs["name"] = variables + exp

    colors = []

    for i in range(len(variables)):
        colors.append('yellow')

    for i in range(len(exp)):
        colors.append('green')

    g.vs["color"] = colors
    g.add_edges(edges)
    plot(g, bbox=(800, 800), layout=g.layout("kk"), vertex_label=g.vs["name"], color=g.vs["color"])
    plot(g, bbox=(800, 800), layout=g.layout("tree"), vertex_label=g.vs["name"], color=g.vs["color"])
