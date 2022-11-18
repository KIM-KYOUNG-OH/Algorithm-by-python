from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:
        menus = []
        for order in orders:
            lst = sorted(list(order))
            candidates = combinations(lst, k)
            for candidate in candidates:
                menus.append(''.join(list(candidate)))

        menu_count = Counter(menus).most_common()
        answer += [menu for menu, count in menu_count if count >= 2 and count == menu_count[0][1]]
    return sorted(answer)