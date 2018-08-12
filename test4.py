def computepay(h,r):
    if h<41:
        return h*r
    elif h>40:
    	return (h-40)*1.5*r+40*r
hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
p = computepay(h,r)
print("Pay",p)
