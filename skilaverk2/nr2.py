def summa(m):
    if m == 0:
        return 0
    else:
        return summa(m-1)+m**2
print(summa(5))