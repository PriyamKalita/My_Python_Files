# DICTIONARY AND ITS FUNCTION  EXPLAINED
# dictionary is nothing but key values pairs
# in python one type of data structure is call dictionary

d1 = ()
d2 = []
d3 = {}

print(type(d1))
print(type(d2))
print(type(d3))

d4 = {"Harry":"burger","rohan":"fish","skillf":"roti"}
print(d4)
print(d4["Harry"])
print(d4["rohan"])
print(d4["skillf"])

d5 = {"Harry":"burger","rohan":"fish","skillf":"roti" ,
      "SHUBHAM":{"B":"MAGGIE","L":"ROTI","D":"CHICKEN"}}
print(d5["SHUBHAM"])
print(d5["SHUBHAM"]["B"])

d6 = {"Harry":"burger","rohan":"fish","skillf":"roti" ,
      "SHUBHAM":{"B":"MAGGIE","L":"ROTI","D":"CHICKEN"}}
d6["ANKIT"] = "JUNK FOOD"

d6[565] ="kebabs"
print(d6)

del d6[565]        # def function used to remove  from  dictionary
print(d6)

d6 = {"Harry":"burger","rohan":"fish","skillf":"roti" ,
      "SHUBHAM": {"B": "MAGGIE", "L": "ROTI", "D": "CHICKEN"}}
print(d6.keys())
print(d6.items())












