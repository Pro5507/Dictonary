dict= {"Apple":1, "Mango":1, "Banana":4, "Guava":4}
print(str(dict))
a= 4
count= 0
for key in dict:
    if dict[key]==a:
        count= count+1
print(str(count))