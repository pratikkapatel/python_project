# create a decorator function
def my_prop1(func):
    return func()


# the method already available
@my_prop1
def get_name():
    return "balaji dinakaran"


# decorate the already available method
# get_name=my_prop(get_name)
# print(get_name)

print(get_name)