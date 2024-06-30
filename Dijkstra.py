from heapq import heapify, heappush, heappop

def adjacencyList(v, list):
    dict = {}

    for x in range(v + 1):
        dict[x] = []

    for z in list:
        dict[z[0]].append((z[1], z[2]))

    return dict

def find_least(list):
    new_list = []

    for x in range(len(list)):
         if list[x][1] != 1:
             new_list.append(list[x])

    heapify(new_list)
    vertex = heappop(new_list)

    for y in range(len(list)):
        if list[y] == vertex:
            return y


def dijkstra(graph, source, dijkstra_distance):
    flag = False
    for y in dijkstra_distance:
        if y[1] == 0:
            flag = True

    if flag == False:
        return

    for x in graph[source]:
        if dijkstra_distance[x[0]][1] != 1 and dijkstra_distance[x[0]][0] > x[1]:
            dijkstra_distance[x[0]][0] = x[1] + dijkstra_distance[source][0]

    least = find_least(dijkstra_distance)
    dijkstra_distance[least][1] = 1

    dijkstra(graph, least, dijkstra_distance)

read_list = [["input1a.txt", "output1a.txt"], ["input1b.txt", "output1b.txt"]]

for num in read_list:
    r = open(num[0], 'r')
    w = open(num[1], 'w')

    first = r.readline().split()
    list = []

    for x in range(int(first[1])):
        second = r.readline().split()
        second = [int(x) for x in second]
        list.append(second)

    source = int(r.readline())

    dijkstra_distance = [[float("inf"), 1]]

    for y in range(int(first[0])):
        dijkstra_distance.append([float("inf"), 0])

    dijkstra_distance[source] = [0, 1]

    store = adjacencyList(int(first[0]), list)
    dijkstra(store, source, dijkstra_distance)

    output = ""
    for x in range(len(dijkstra_distance)):
        if x == 0:
            continue
        if dijkstra_distance[x][0] == float("inf"):
            output += f"-1 "
        else:
            output += f"{dijkstra_distance[x][0]} "

    w.write(output)
    w.close()
