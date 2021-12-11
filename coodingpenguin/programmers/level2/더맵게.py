import heapq


def solution(scoville, K):
    heapq.heapify(scoville)  # 최소힙으로 변환
    count = 0  # 섞는 횟수
    while len(scoville) > 1:
        min_first = heapq.heappop(scoville)  # 가장 낮은 스코빌
        if min_first >= K:
            break
        min_second = heapq.heappop(scoville)  # 두 번째로 가장 낮은 스코빌
        mixed = min_first + (min_second * 2)  # 섞은 스코빌
        count += 1
        heapq.heappush(scoville, mixed)
    # 다 섞었을 때도 K를 넘지 못한 경우
    if scoville[0] < K:
        return -1
    return count
