def fib(n, dic={}):

    if n <= 2:
        return 1

    if n in dic:
        return dic[n]

    dic[n] = fib(n - 1, dic) + fib(n - 2, dic)

    return dic[n]


print(fib(30))
