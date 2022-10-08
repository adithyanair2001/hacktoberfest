def findthereverseword(a):
    ans = a.split()
    print(ans)
    re = [i[::-1] for i in ans]
    p=' '.join(ans)
    print(p)


a = input()
findthereverseword(a)