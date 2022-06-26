from random import shuffle

chars = ['A', 'T', 'G', 'C']
n = int(input())
s = str()


def guess(char: str):
    query = s + char
    print(query, flush=True)
    return input() == 'YES'


while len(s) < n:
    shuffle(chars)
    for c in chars[:-1]:
        if guess(c):
            s += c
            break
    else:
        s += chars[-1]
