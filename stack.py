top = -1


def push(x):
    global a, top
    top = top + 1
    a.append(x)


def pop():
    global top
    a.pop(top)
    top = top - 1


def topa():
    print(a[top])


def isEmpty():
    if top == -1:
        return True
    else:
        return False


a = []

push(5)
push(56)
for i in range(top+1):
    print(a[i])

pop()
push(8)
push(96)

for i in range(top+1):
    print(a[i])


topa()
