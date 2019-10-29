# SH-I

def ham_dist(s1, s2):

    assert len(s1) == len(s2)

    dist = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    return dist

a = 'AAAAAA'
b = 'AAAABB'

try:

    print(ham_dist(a, b))

except AssertionError:

    pass
