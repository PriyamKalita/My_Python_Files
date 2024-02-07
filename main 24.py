# SCOPE,GLOBAL VARIABLES AND GLOBAL KEYWORD

                 #global variables














x = 89

def asus():
    x = 20
    def dell():
        global x
        x = 88
    print("before calling dell()", x)
    dell()
    print("after calling  dell()", x)

asus()
print(x)







