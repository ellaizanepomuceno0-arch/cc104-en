import time

def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_formula(n):
    return n * (n + 1) // 2


n = 10_000_000

start = time.time()
sum_iterative(n)
end = time.time()
print("Iterative:", end - start, "seconds")

start = time.time()
sum_formula(n)
end = time.time()
print("Formula:", end - start, "seconds")
