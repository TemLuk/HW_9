def fun():
    x = ['milk', 'bread']

    def fun2():
        print(x)
        print(id(x))

    return fun2


f = fun()
print(f)
print(f())
print(f.__closure__[0].cell_contents)
a = f.__closure__[0].cell_contents
print(id(a))
a.append('water')
print(f())
