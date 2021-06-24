

def outer():
    x = 1
    def inner():
        nonlocal x
        print(f'x находится в функции outer: {x}')
        x += 1
        print(f'x находится в функции inner: {x}')

    return inner

foo = outer()
for i in range(5):
    print(f'{i + 1}')
    foo()
    print('\n')