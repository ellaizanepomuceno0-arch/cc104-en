import time

arr = list(range(1_000_000))

start = time.time()
x = arr[500_000]  # Constant-time access
end = time.time()

print("O(1) access time:", end - start, "seconds")


target = 999_999

start = time.time()
found = target in arr  # Linear search
end = time.time()

print("O(n) search time:", end - start, "seconds")
