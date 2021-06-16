# https://www.acmicpc.net/problem/1068
# 트리


def find_children(num_nodes, parents):
    graph = [[] for _ in range(num_nodes)]
    for child, parent in enumerate(parents):
        if parent != -1:
            graph[parent].append(child)
    return graph


def count_leaves(start, to_remove, graph):
    if not graph[start]:
        return 1

    count = 0
    for child in graph[start]:
        if child != to_remove:
            count += count_leaves(child, to_remove, graph)
        elif len(graph[start]) == 1:
            count += 1
    return count


if __name__ == '__main__':
    num_nodes = int(input())
    parents = [int(p) for p in input().split()]
    children = find_children(num_nodes, parents)
    root = parents.index(-1)
    node_to_remove = int(input())

    if node_to_remove == root:
        num_leaves = 0
    else:
        num_leaves = count_leaves(root, node_to_remove, children)
    
    print(num_leaves)
