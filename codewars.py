def fun(s):
    n = []
    for x in s:
        if x.isupper():
            n.append(s.index(x))
    return n


print(fun("breakCamelCase"))
