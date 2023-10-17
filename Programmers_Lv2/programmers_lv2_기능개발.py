import math


def solution(progresses, speeds):
    answer = []
    days = []

    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100-progress)/speed))

    max_day = 0

    for day in days:
        if max_day < day:
            answer.append(1)
            max_day = day
        else:
            answer[-1] += 1

    return answer
