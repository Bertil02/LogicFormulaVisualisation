import data
import graph1


if __name__ == '__main__':
    file_name = 'sample'

    data.generate(file_name)
    graph1.draw(file_name)
