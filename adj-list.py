from collections import defaultdict
def create_adj_list():
    n = int(input("Enter the number of vertices: "))
    adj_list = defaultdict(list)

    for _ in range(n):
       node = int(input(f"Enter the node : "))
       adj_list[node]

    edges = int(input("Enter the number of edges: "))

    IsADirected = int(input("Enter 1 for directed otherswise 0 : "))

    for _ in range(edges):
        u = int(input("Enter the source node: "))
        v = int(input("Enter the destination node: "))

        adj_list[u].append(v)

        if IsADirected == 0:
            adj_list[v].append(u)

    return adj_list
my_adj_list = create_adj_list()
print(my_adj_list, "Adjacency List:")