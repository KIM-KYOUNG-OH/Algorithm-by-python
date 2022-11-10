import math


def parseMinute(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour * 60 + minute


class Cost:
    def __init__(self, ids, cost):
        self.id = ids
        self.cost = cost


def calc_fee(fees, elapsed_time):
    default_parking_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    if elapsed_time <= default_parking_time:
        return default_fee
    else:
        fee = default_fee
        diff = elapsed_time - default_parking_time
        fee += math.ceil(diff / unit_time) * unit_fee
        return fee


def solution(fees, records):
    garage = dict()
    elapsed_times = dict()

    for record in records:
        arr = record.split(' ')
        time = parseMinute(arr[0])
        ids = arr[1]
        order = arr[2]
        if order == 'IN':
            garage[ids] = time
        else:
            in_time = garage.pop(ids)
            elapsed_time = time - in_time
            if ids not in elapsed_times.keys():
                elapsed_times[ids] = elapsed_time
            else:
                elapsed_times[ids] += elapsed_time

    end_time = parseMinute('23:59')
    for key, value in garage.items():
        elapsed_time = end_time - value
        if key not in elapsed_times.keys():
            elapsed_times[key] = elapsed_time
        else:
            elapsed_times[key] += elapsed_time

    costs = list()
    for key, value in elapsed_times.items():
        costs.append(Cost(key, calc_fee(fees, value)))

    costs.sort(key=lambda e: e.id)
    answer = list()
    for cost in costs:
        answer.append(cost.cost)
    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])