from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

User = namedtuple('User', 'name role age')

user = User(name='Bob', role='Coder', age=27)
print(user.name, user.age)

print(type(User))
# defaultdict
# Counter
# deque

x = [1, 2, 3, 4, 5]
print(2 not in x)