#just a comment to see if git is working correctly
lists = [i**2 for i in range(100) if not i%2]

# print(lists)

even = lambda x: x%2 == 0

even_numbers = list(filter(even, range(100)))

print(even_numbers)


squares = lambda x: pow(x, 2)

square_numbers = list(map(squares, range(100)))

print(square_numbers)

import numpy as np

arr = np.random.random((4, 5))
