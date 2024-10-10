from random import choices
class Closet:
    CLOTHES = ('T-shirt', 'Sweater', 'Pants', 'Shoes', 'Jacket', 'Hat', 'Scarf')

    def __init__(self, count: int, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'осталось вещей в шкафу {self.count}:\n{names}'

    def __rshift__(self, other): #метод отбросит лишние вещи количество, которое нужно убрать указано в 24 строке
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, choices(self.storeroom, k=self.count))

cl = Closet(10)
print(cl)
for _ in range(4):
    cl = cl >> 3
    print(cl)


