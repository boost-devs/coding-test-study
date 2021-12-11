import math


def solution(progresses, speeds):
    remained = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]   # 개발 완료까지 남은 날
    deploy = [] # 배포 개수 목록
    count = 1   # 배포 기능 카운트
    max_remained = remained[0]  # 배포 그룹에서 최대 남은 날
    for i in range(1, len(remained)):
        if max_remained >= remained[i]:
            count += 1
        else:
            deploy.append(count)
            max_remained = remained[i]
            count = 1
    return deploy + [count]
