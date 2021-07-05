Z = input()
S = Z
N = K = 0

N = Z.find('not')
K = Z.find('poor')

if N >= 0 and K >= 0:
    S = S.replace(S[N:K+4], 'good')
    print(S)
