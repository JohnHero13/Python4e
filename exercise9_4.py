fname = input('Enter file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From '):
        continue
    sender = words[1]
    counts[sender] = counts.get(sender, 0) +1


bigcount = None
bigsender = None
for sender,count in counts.items():
    if bigcount is None or count > bigcount:
        bigsender = sender
        bigcount = count

print(bigsender, bigcount)
