a=100
def show():
    global a
    a=10
    print(a)
    global b
    b=100
    print(b)
print("hai")
show()
print(b)
print(a)
print("bye")