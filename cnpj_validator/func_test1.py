def ftest (a,b):
    c=[]
    for i, j in zip(a, b):
        c.append(i * j)
    d = sum(c)
    if (11 - (d % 11)) > 9:
        digit1 = 0
        return digit1
    else:
        digit1 = (11 - (d % 11))
        return digit1


