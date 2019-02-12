# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    fibs = [0, 1]
    su = 0
    for i in range(2, n+1):
         num = fibs[-1] + fibs[-2]
         su = num + su
         fibs.append(num)
    return su%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m=10))
