import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    num_mix = 0
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        num_mix += 1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2 * second)
        
    if scoville[0] < K:
        return -1
    return num_mix
    