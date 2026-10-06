s = "hello world"

print("First char:", s[0])

for c in s:
    print(c, end=" ")

s2 = s + "!!!"
print("\nConcatenated:", s2)

print("Contains 'world'?", "world" in s)
