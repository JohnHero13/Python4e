import re #uses the package

hand = open('regex_sum_124880.txt') #opens the file
numlist = list() #creates an empty list

#Go trough every single line and extract the numbers
for line in hand:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    if len(number) < 1 : continue
    for n in number:
        num=float(n)
        numlist.append(num)

sum = sum(numlist)
sum = int(sum)
print(sum)
