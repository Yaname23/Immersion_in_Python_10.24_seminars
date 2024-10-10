a = [i for i in range(1_000_000)]
b = (i for i in range(1_000_000))

print(a.__sizeof__())
print(b.__sizeof__())