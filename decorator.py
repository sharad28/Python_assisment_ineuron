def style(fun):
    def inner(a):
        print("*"*30)
        fun(a)
        print("*"*30)

    return inner

@style
def print_name(a):
    print(a)

print_name("sarad")