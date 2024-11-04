# using a hashtable as memory for storing and lookup of intermediate result
memory = {}

# get the nth fibonacci number using recursion
def _fibo_using_recursion(n, memory):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memory:
        return memory[n]
    prev2 = _fibo_using_recursion(n-2, memory)
    memory[n-2] = prev2
    prev1 = _fibo_using_recursion(n-1, memory)
    memory[n-1] = prev1
    return prev2 + prev1

# get the nth fibonacci number using loop
def _fibo_using_loop(n, memory):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memory:
        return memory[n]
    a = 0
    b = 1
    fibo = 0
    i = 2
    while i <= n:
        fibo = a + b
        memory[i] = fibo
        a = b
        b = fibo
        i += 1
    return fibo

def fibo(n):
    return _fibo_using_loop(n, memory)
