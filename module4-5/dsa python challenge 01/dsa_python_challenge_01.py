#1
# n = 7
# if n > 10 or n == 7:
#     print("correct")
#else:
#     print("incorrect")

#2
# nums = [2, 4, 6, 8]
# print(nums[1] + nums[-1])

#3
# values = [10, 20, 30, 40, 50]
# print(values[1:4])

#4
# stack = []
# stack.append(3)
# stack.append(5)
# stack.pop()
# stack.append(8)
# print(stack)

#5
# from collections import deque
# q = deque([1, 2, 3])
# q.apppend(4)
# q.popleft()
# prinrt(list(q))

#6
# point = (4, 9)
# print(point[0] * point[1])

#7
# scores = {'Ana': 90, 'Ben': 75}
# scores['Ana'] += 5
# print(scores['Ana'])

#8
# a = {1, 2, 2, 3}
# b = {3, 4}
# print(sorted(a | b))

#9
# def f (n):
#     if n == 0: return
#     print(n, end =' ')
#     f(n - 1)
#     f3

#10
# def add_item(items):
#     items.append(9)
# data = [1, 2] 
# add_item(data)
# print(data)   

#11
# def find(a, x):
#     for i, v in enumerate(a):
#         if v == x: return i
#     return -1
# print(find([4, 7, 9, 7], 7))

#12
# def bs(a, x):
#     lo, hi = 0, len(a) - 1
#     while lo <= hi:
#         m = (lo + hi) // 2
#         if a[m] == x: return m
#         if a[m] < x: lo = m + 1
#         else: hi = m - 1
#     return -1
# print(bs([2, 4, 6, 8, 10], 8))

#13
# arr = [5, 2, 4]
# arr.sort()
# print(arr)

#14
# word = ["pear", "fig", "banana"]
# print(sorted(word, key=len))

#15
# count = 0
# for i in range(3):
#     for j in range(2):
#         count += 1
# print(count)

#16
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# a = Node(10)
# b = Node(20)
# a.next = b
# print(a.next.value)        

 #17
# class Node:
#     def __init__(self, v, next=None):
#         self.v, self.next = v, next

# head = Node(1, Node(2, Node(3)))
# head = head.next        
# print(head.v)

#18
# import heapq

# h = [5, 1, 4]
# heapq.heapify(h)
# print(heapq.heappop(h))

#19
# seen = {}
# for x in [2, 3, 2]:
#     seen[x] = seen.get(x, 0) + 1
# print(seen[2])    

#20
# nums = [2, 7, 11]
# target = 9
# seen = set()
# for x in nums:
#     if target - x in seen:
#         print(x)
#         break 
#     seen.add(x)
