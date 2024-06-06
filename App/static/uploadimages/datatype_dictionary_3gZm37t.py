s={}
s["colour"]="black"
print(s)
print()

d={"name":"python","s":20,"age":30,"dec":45.5}
print(d)


print(len(d))
print(type(d))
print(d["age"])
d["age"]=40
print(d)

if "age" in d:
    print("yes,ageis one of the key in this dictionary")
else:
    print("not found")
d["color"]="black"
print(d)
d.pop("color")
print(d)

del d["age"]
print(d)

d.clear()
print(d)
del d
d.name(datatype)
print(d)
