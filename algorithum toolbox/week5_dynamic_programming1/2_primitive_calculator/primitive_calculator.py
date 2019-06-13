# Uses python3
import sys

def op_fun(n):
    a = set([n+1,n*2,n*3])
    return list(a)
def optimal_sequence(n):
    if n>1:
        i=0
        val = op_fun(1)
        while n!=i:
            if n not in val:
                super_array = []
                for j in val:
                    sub_array = op_fun(j)
                    super_array = super_array + sub_array
                super_array = set(super_array)
                super_array = list(super_array)
                val= super_array
                
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)

for x in sequence:
    print(x, end=' ')



a = set([1,1,1])
list(a)