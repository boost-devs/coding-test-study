from math import ceil


def solution(progresses, speeds):
    schedule = [] # [배포일, 개수]
    for progress, speed in zip(progresses, speeds):
        complete = ceil((100 - progress) / speed)
        if schedule and schedule[-1][0] >= complete:
            schedule[-1][1] += 1
        else:
            schedule.append([complete, 1])
    return [t[1] for t in schedule]
    