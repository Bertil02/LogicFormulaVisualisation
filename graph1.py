from igraph import *
import data
import os


def draw(file_name):
    draw_raw(file_name)
    line_number = 0
    variables = []
    exp = []
    edges = []
    edges_colors = []
    g = Graph()
    input_string,dataHeader = data.load(file_name)

    for variable in input_string:
        if variable != 0:
            if abs(variable) not in variables:
                variables.append(abs(variable))

            edges.append([variables.index(abs(variable)), line_number])
            if variable < 0:
                edges_colors.append('red')
            else:
                edges_colors.append('black')
        else:
            line_number += 1
            exp.append('C_' + str(line_number))

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

    try:
        os.mkdir('result')
    except WindowsError:
        print('Directory already exists')

    g.vs["edge_color"] = edges_colors

    plot(g, 'result/random.png', bbox=(950, 690), layout=g.layout("random"), vertex_label=g.vs["name"],
         color=g.vs["color"], edge_color=g.vs["edge_color"])
    plot(g, 'result/tree.png', bbox=(950, 690), layout=g.layout("tree"), vertex_label=g.vs["name"],
         color=g.vs["color"], edge_color=g.vs["edge_color"])
    plot(g, 'result/reingold.png', bbox=(950, 690), layout=g.layout("fr"), vertex_label=g.vs["name"],
         color=g.vs["color"], edge_color=g.vs["edge_color"])
    plot(g, 'result/kamada_kawai.png', bbox=(950, 690), layout=g.layout("kk"), vertex_label=g.vs["name"],
         color=g.vs["color"], edge_color=g.vs["edge_color"])


def draw_raw(file_name):
    line_number = 0
    variables = []
    exp = []
    edges = []
    edges_colors = []
    g = Graph()
    input_string, data_header = data.load(file_name)

    for variable in input_string:
        if variable != 0:
            if variable not in variables:
                variables.append(variable)

            edges.append([variables.index(variable), line_number])
        else:
            line_number += 1
            exp.append('C_' + str(line_number))

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

    try:
        os.mkdir('result')
    except WindowsError:
        print('Directory already exists')

    plot(g, 'result/random_rough.png', bbox=(950, 690), layout=g.layout("random"), vertex_label=g.vs["name"],
         color=g.vs["color"])
