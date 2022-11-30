def greting(fn):
    def wrappper():
        print("hello all")
        fn()
        print("see you")
    return wrappper

@greting
def morning():
    print("good morning")


@greting
def  noon():
    print("good afternoon")

morning()
