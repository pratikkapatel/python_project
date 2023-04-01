#yield is a temporary pause to the execution methods
def hello1():
    return 'hi'

def hello2():
    print("browser launch")
    yield 'hi1'
    print("browser close")
    yield 'hi2'


print(hello1())
print(hello2())

for cur in hello2():
    print(cur)