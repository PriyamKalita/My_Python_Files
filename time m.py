""""
import time
initial = time.time()

k = 0
while(k<45):
    print("this is harry")
    k +=1
print("while loop ran in", time.time() - initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("this is harry")
print("for loop ran in",time.time()-initial2,"seconds")"""    #1


""""
import time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)"""      #2

""""
import time
initial = time.time()

k = 0
while(k<45):
    print("this is harry")
    time.sleep(3)
    k +=1
print("while loop ran in", time.time() - initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("this is harry")
print("for loop ran in",time.time()-initial2,"seconds") """   #3


import time

localtime = time.asctime(time.localtime(time.time()))

print(localtime)





