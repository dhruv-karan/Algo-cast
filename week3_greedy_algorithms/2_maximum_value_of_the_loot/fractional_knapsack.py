# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0
    weights = [weights.sort()]
    type(weights)
    values = [values.sort()]
    ratio =  [x/y for x,y in zip(values,weights)]
    inx ,max_val = ratio.index(max(ratio)) , max(ratio)
    if (capacity > weights[inx]):
        value += values[inx]
        capacity -= weights[inx]
        del weights[inx]
        del ratio[inx]
        del capacity[inx]
    elif(capacity ==0):
        return value
    elif(capacity < weights[inx]):
        value += max_val*capacity
        return value
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


print(get_optimal_value(20,[5,7,3,8,1,4],[300,200,176,98,65,500]))


weights=[5,7,3,8,1,4]

weights = [weights.sort()]
print(type(weights))