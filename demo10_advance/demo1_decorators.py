def my_prop(func):
    res = func()
    res = str(res).split(" ")[0]
    return res


# the method already available
@my_prop
def get_name():
    return "balaji dinakaran"


# decorate the already available method
# get_name=my_prop(get_name)
# print(get_name)

print(get_name)