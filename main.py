# Przykład 1
# def recursive_sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return recursive_sum(a-1, b+1)
#
#
# print(recursive_sum(4, 6))


# Przykład 2

# def factorial(a):
#     if a == 0:
#         return 1
#     else:
#         return a * factorial(a-1)
#
# print(factorial(5))


# Zadania 1

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(7))