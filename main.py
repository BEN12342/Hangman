import math

def ft(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * ft(n-1)

def St2(n,k):
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    else:
        return St2(n-1, k-1) + k * St2(n-1,k)

def St1(n,k):
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    else:
        return St1(n-1,k-1) + (n-1)*St1(n-1,k)

def bell_number(n):
    ITERATIONS = 10000 
    return (1/math.e) * sum([(k**n)/(math.factorial(k)) for k in range(ITERATIONS) ])

if __name__ == '__main__':
    print(St1(20,1))