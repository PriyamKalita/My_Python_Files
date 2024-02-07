#ARGS AND KWARGS
#def function_name_print(a,b,c,d):
#    print(a,b,c,d)


def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nnow i would like tointroduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")

# function_name_print("harry","rohan","skillf","hammad","shivam")

har = ["harry","rohan","skillf","hammad","shivam", "the programmer" ,]
normal = "i am a normal argument and the students are :"
kw = {"rohan":"monitor","harry":"fitness instructor","the programmer":"coordinator","shivam":"cook",}
funargs(normal, *har, **kw)