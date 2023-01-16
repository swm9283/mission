#mission
#5.6
list = ["duck","gourd","spitz"]
for i in list:
    k=i.title()
    print("%sy Mc%sface" % (k,k))


#5.7
list = ["duck","gourd","spitz"]
for i in list:
    print("{k}y Mc{k}face".format(k=i.title()))