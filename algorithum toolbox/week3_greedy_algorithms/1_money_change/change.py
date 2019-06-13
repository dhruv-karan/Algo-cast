# Uses python3
import sys
import math
def get_change(m):
    change = 0
    remainder = m
    if m >=10:
        ques = math.floor(m/10)
        remainder = m%10
        change += ques
    if remainder>=5:
        change +=1
        change = change + remainder-5
    else:
        change = remainder + change
    return change

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))