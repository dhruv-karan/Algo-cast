#Uses python3

import sys

def max_dot_product(a, b):
    a = sorted(a)
    b= sorted(b)
    c= [i*j for i,j in zip(a,b)]
    res =sum(c)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
