def my_func(data) -> float:
    res = sum(data) / len(data)
    return  res

print(my_func([2, 5.5, 15, 8.0, 13.74]))

print('-----------------------')

a: int | float = 42
b: float = float(input("введите число: "))
a = a / b
print(a)
print('-----------------------')
