# 문제: [BOJ 6416] 트리인가?
# 유형: 트리
# 메모리/시간: 32048kb / 88ms
# 참고: https://chanqun.tistory.com/213

import sys
from collections import defaultdict, deque
from itertools import chain


def check_tree(graph: dict):
    # 트리가 없는 경우
    if not graph:
        # 트리라고 반환
        return True

    from_nodes = set(graph.keys())  # 나가는 간선이 있는 노드
    graph_values = list(chain(*graph.values()))
    to_nodes = set(graph_values)  # 들어가는 간선이 있는 노드
    all_nodes = from_nodes | to_nodes  # 모든 노드

    # 조건 1. 루트 노드 검사
    root = from_nodes - to_nodes
    if not root:
        return False

    # 조건 2. 하나의 들어오는 간선이 존재하는지 검사
    if (root not in to_nodes) and (len(graph_values) != len(to_nodes)):
        return False

    # 조건 3. 루트에서 다른 노드로 갈 수 있는지
    if len(all_nodes) != len(graph_values) + 1:
        return False

    return True


count = 1  # 테스트 케이스 카운트
end_flag = False  # 입력 종료 플래그
check_flag = False  # 테스트 케이스 종료 플래그
graph = defaultdict(list)  # 인접 리스트

for line in sys.stdin:
    nodes = line.rstrip().split("  ")
    # 입력이 빈 줄인 경우
    if not nodes[0]:
        continue

    # 입력이 있는 경우
    for node in nodes:
        u, v = map(int, node.split())
        # 테스트 케이스 종료
        if (u, v) == (0, 0):
            check_flag = True
            break
        # 입력 종료
        elif (u, v) == (-1, -1):
            end_flag = True
            break
        else:
            graph[u].append(v)  # 인접 리스트 갱신

    if check_flag:
        # 트리인지 체크
        is_tree = check_tree(graph)

        # 출력
        print(f"Case {count} {'is' if is_tree else 'is not'} a tree.")

        # 변수 초기화
        count += 1
        graph = defaultdict(list)
        check_flag = False

    if end_flag:
        break
