name = input('Enter the file name: ')
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = dict()


for line in fhand :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5].split(":")
    counts[time[0]] = counts.get(time[0],0) + 1

lst= list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)
for hour,count in lst:
    print(hour, count)
