quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry' : 'Ow!',
    'Curly' : 'Nyuk nyuk!',
}

for stooge in quotes:
    print(stooge)

print("---------------------------------------------------------------------")

from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry' , 'Ow!'),
    ('Curly' , 'Nyuk nyuk!'),
    ])

for stooge in quotes:
    print(stooge)
print("---------------------------------------------------------------------")


def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palindrome('a')
palindrome('racecar')
palindrome('')
palindrome('radar')
palindrome('halibut')