def intolist(listi, tala):
    if len(listi)==0:
        listi.append(tala)
        return True
    for i in range(0,len(listi)-1):
        if tala <= listi[i]:
            listi.insert(i, tala)
            return True
    else:
        listi.append(tala)
        return True
pp=[2,3,3,5,6,7,9,10]
print(intolist(pp, 11))
print(pp)