def runa(m):
    if m == 0:
        return 0
    else:
        runa(m-1)
        print((m*(m+1))//2)

runa(10)