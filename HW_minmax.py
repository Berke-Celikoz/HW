def minmax(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    mid = a + b + c - min(l) - max(l)
    return print("Min:", min(l), "Mid:", mid, "Max:", max(l))
