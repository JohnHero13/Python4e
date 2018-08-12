print('Exercise 6.5')
text = "X-DSPAM-Confidence:    0.8475";

pos = text.find('0')
print(pos)
result1=text[pos:]
result=float(result1)
print(result)
