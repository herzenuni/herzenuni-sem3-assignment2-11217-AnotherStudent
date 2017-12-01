# https://ru.wikipedia.org/wiki/Алгоритм_Евклида
def gcd(a, b):
    assert(type(a) == int)
    assert(type(b) == int)

    if(b != 0):
        return gcd(b, a % b)
    else:
        return a

def user_experiance():
    print('Number a:')
    a = int(input())
    print('Number b:')
    b = int(input())

    c = gcd(a, b)

    print('gcd:', c)

if __name__ == '__main__':
    user_experiance()


