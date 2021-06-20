# https://www.acmicpc.net/problem/6416
# 트리인가?


def dfs(node, graph, visited):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, graph, visited)
        else: # 방문했던 노드를 방문하는 경우 트리가 아님
            return False
    return True


end_of_game = False
case_idx = 1

while not end_of_game:
    edges = []
    nodes = set()
    end_of_case = False
    
    while not end_of_case:
        line = input().split('  ')
        if not line[0]:
            continue

        if int(line[0].split()[0]) < 0: # 입력이 하나라도 음수가 되는 경우는 마지막밖에 없다.
            end_of_game = True
            break

        for pair in line:
            u, v = map(int, pair.split())
            if u > 0: # 모든 노드의 번호는 0보다 크다.
                edges.append((u, v))
                nodes.update({u, v})
            else:
                end_of_case = True
            
    if not end_of_game:
        is_tree = True
        if edges: # 빈 그래프도 트리
            graph_in = {node: [] for node in nodes}
            graph_out = {node: [] for node in nodes}
            for u, v in edges:
                graph_in[v].append(u)
                graph_out[u].append(v)

            roots = [node for node in nodes if not graph_in[node]]
            if len(roots) != 1: # 조건 1
                is_tree = False
            else:
                root = roots[0]
                if not all([
                    len(graph_in[node]) == 1 
                    for node in nodes 
                    if node != root
                ]): # 조건 2
                    is_tree = False
                else: # 조건 3; DFS
                    visited = {node: False for node in nodes}
                    is_tree = dfs(root, graph_out, visited)
                    if not all(visited.values()):
                        is_tree = False

        print(f"Case {case_idx} is{' ' if is_tree else ' not '}a tree.")
        case_idx += 1
