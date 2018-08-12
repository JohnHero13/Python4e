fname = input("Enter file name ")
fh = open(fname)
lst = list()
for line in fh :
    line = line.rstrip()
    piece = line.split()
    for word in piece :
        if word in lst : continue
        lst.append(word)


lst.sort()
print(lst)
