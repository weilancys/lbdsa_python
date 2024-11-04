# using a hashtable as memory for storing and lookup of intermediate result
memory = {}

# get the nth fibonacci number using recursion, n is 1 based
def _fibo_using_recursion(n, memory):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in memory:
        return memory[n]
    prev2 = _fibo_using_recursion(n-2, memory)
    memory[n-2] = prev2
    prev1 = _fibo_using_recursion(n-1, memory)
    memory[n-1] = prev1
    return prev2 + prev1

# get the nth fibonacci number using loop, n is 1 based
def _fibo_using_loop(n, memory):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in memory:
        return memory[n]
    a = 0
    b = 1
    fibo = 0
    for i in range(n-2):
        fibo = a + b
        a = b
        b = fibo
        memory[i+2] = fibo
    return fibo

def fibo(n):
    return _fibo_using_loop(n, memory)

if __name__ == "__main__":
    # n = 20
    # result_recursion = fibo_using_recursion(n, memory)
    # result_loop = fibo_using_loop(n, memory)
    # assert(result_loop == result_recursion)
    # print("result using recursion:", result_recursion)
    # print("result using loop:", result_loop)

    for i in range(1, 101):
        print(_fibo_using_loop(i, memory), end=" ")
    print()
    for i in range(1, 101):
        print(_fibo_using_recursion(i, memory), end=" ")
    print()