from math import ceil


def count_diggers(distance, days, one_digger_per_day):
    return ceil(distance / one_digger_per_day / days)


print(count_diggers(1400, 2, 3))
