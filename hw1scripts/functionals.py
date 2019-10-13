#1-)MAP AND LAMBDA FUNCTION
cube = lambda x: x**3

def fibonacci(n):
    if n == 0 :
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibonaccilist=[0,1]
        for i in range(n):
#iteratively append fibonacci list.
            fibonaccilist.append(fibonaccilist[i]+fibonaccilist[i+1])
            if len(fibonaccilist)==n:
                return fibonaccilist




if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))