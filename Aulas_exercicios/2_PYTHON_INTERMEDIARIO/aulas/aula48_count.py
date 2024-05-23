#Count é um contador infinito , um interador sem fim (itertools)
# pode definir quando comeca
# é um iterator

from itertools import count


c1 = count(start=2, step=2)
# r1 = range(8, 100, 8)

# print('c1', hasattr(c1, '__iter__'))
# print('c1', hasattr(c1, '__next__'))
# print('r1', hasattr(r1, '__iter__'))
# print('r1', hasattr(r1, '__next__'))
# print()

print('COUNT')
for i in c1:
    if i >= 100:
        break

    print(i)
