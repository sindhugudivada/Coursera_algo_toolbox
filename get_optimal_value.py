# python3
import sys


def get_optimal_value(capacity, weights, values):

    value = 0
    weight_so_far = 0
    unit_value = []

    for i in range(len(weights)):
         unit = float(values[i]) / weights[i]
         unit_value.append(unit)
    while (weight_so_far < capacity) and len(unit_value) > 0:
        max_unit = max(unit_value)
        max_index = unit_value.index(max_unit)
        max_value = values[max_index]
        max_weight = weights[max_index]

        if max_weight <= capacity - weight_so_far :
            weight_so_far = weight_so_far + max_weight
            value = value + max_value
        else:
            value = value + (float(max_value * (capacity - weight_so_far)) / max_weight)
            weight_so_far = capacity
        unit_value.pop(max_index)
        weights.pop(max_index)
        values.pop(max_index)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
