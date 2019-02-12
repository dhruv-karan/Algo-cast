# Uses python3
import sys

def fibonacci_sum_naive(n):
    fibs = [0, 1]
    su = 1
    if n ==0:
        su =0
        return su
    for i in range(2, n+1):
         num = fibs[-1] + fibs[-2]
         su = num + su
         fibs.append(num)
    return su%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
