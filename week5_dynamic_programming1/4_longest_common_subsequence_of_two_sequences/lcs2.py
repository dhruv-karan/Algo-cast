#Uses python3

import sys

def lcs2(a, b):
    a = 'huv'
    b= 'huvw'
    lena = len(a)
    lenb = len(b)
    matrix = [[0]*(lena+1) for i in range(lenb+1)]
    
    for k in range(1,lena+1):
        for l in range(1,lenb+1):
            if a[k-1] == b[l-1]:
                matrix[k][l] = matrix[k-1][l-1] + 1
            else:
                matrix[k][l] = max(matrix[k][l-1],matrix[k-1][l])
    return matrix[lena][lenb]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))