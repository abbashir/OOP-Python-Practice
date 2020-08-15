# same interface
def Add(a, b, c=0):
    print(a + b + c)

# different object
Add(10, 20)
Add(10, 20, 30)
