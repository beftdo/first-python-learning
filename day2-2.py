#깔끔하게 출력하기 : pprint()
from collections import OrderedDict
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wiseguy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuck nyuk!'),
])
pprint(quotes)

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

#임의값 얻기
from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))
print(choice(range(100)))
print(choice('alphabet'))

print("---------------------------------------------------------------------")

from random import sample
print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
print(sample(['a', 'one', 'and-a', 'two'], 2))
print(sample(range(100), 4))
print(sample('alphabet' ,7))

print("---------------------------------------------------------------------")
from random import randint
print(randint(38,74))
from random import randrange
print(randrange(38, 74))
print(randrange(38, 74, 10))
from random import random
print(random())