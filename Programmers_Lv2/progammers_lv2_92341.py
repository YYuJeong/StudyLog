from collections import defaultdict
import math


def solution(fees, records):
    answer = []

    dic = defaultdict(list)
    for record in records:
        time, car, state = record.split(' ')
        if not car in dic:
            dic[car] = [time, 0, state]
        else:
            if state == "OUT":
                h, m = map(int, dic[car][0].split(':'))
                new_h, new_m = map(int, time.split(':'))
                parking_time = dic[car][1] + (new_h*60 + new_m) - (h*60 + m)
                dic[car] = [time, parking_time, state]
            elif state == "IN":
                dic[car][0] = time
                dic[car][2] = state

    for car, val in dic.items():
        if val[2] == "IN":
            h, m = map(int, val[0].split(":"))
            val[1] = val[1] + (23*60 + 59) - (h*60 + m)

    for car, val in dic.items():
        if val[1] <= fees[0]:
            dic[car][0] = fees[1]
        else:
            dic[car][0] = fees[1] + math.ceil((val[1]-fees[0])/fees[2])*fees[3]

    return [dic[key][0] for key in sorted(dic)]
