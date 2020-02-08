def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    j = m - 1
    k = m - 1
    last = {}
    for k in range(m):
        last[P[k]] = k
    while j < n:
        if T[j] == P[k]:
            if k == 0:
                return j
            else:
                j -= 1
                k -= 1
        else:
            i = last.get(T[j], -1)
            j += m - min(k, i + 1)
            k = m - 1

    return -1


def find_kmp(T, P):

    n, m = len(T), len(P)
    if m == 0:
        return 0
    j = 0
    k = 0
    fail = compute_kmp_fail(P)
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            k += 1
            j += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1


def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    k = 0
    j = 1
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            k += 1
            j += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return fail


if __name__ == "__main__":
    P = "aabbbb"
    T = "sdwaaaabbbbbbcc"
    print("find_boyer_moore: ", find_boyer_moore(T, P))
    print("find_kmp: ", find_kmp(T, P))

