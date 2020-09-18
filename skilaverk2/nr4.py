def þversumma(m):
    if m <= 9:
        return m
    else:
        return int(str(m)[0]) + þversumma(int(str(m)[1:]))
print(þversumma(1206))