fname = input("Enter file name: ")
fh = open(fname)
count=0
number2=0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count= count+1
    pos = line.find(':')
    number = line[pos+2:]
    number1 = float(number)
    number2 = number2 + number1

average = number2/count
print('Average spam confidence: ', average)
