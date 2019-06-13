# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0
    ratio =  [x/y for x,y in zip(values,weights)]
    while len(ratio)>0:
        inx ,max_val = ratio.index(max(ratio)) , max(ratio)
        if (capacity > weights[inx]):
            value += values[inx]
            capacity -= weights[inx]
            del weights[inx]
            del ratio[inx]
            del values[inx]
        elif(capacity ==0):
            return value
        elif(capacity <= weights[inx]):
            value += max_val*capacity
            return value
        else:
            return value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))