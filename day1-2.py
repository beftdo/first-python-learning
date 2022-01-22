#데크 무슨 말인지 모르겠음.

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palindrome('a')
""" palindrome('racecar')
palindrome('')
palindrome('radar')
palindrome('halibut') """