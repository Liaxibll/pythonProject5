def funck(func):
    def inner(b):
     print('start funck')
     func(b)
     print('end funck')
    return inner

def say(name):
    print('hello', name)

d = funck(say)
d('vasya')












