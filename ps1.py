bin1 = input("enter binary data:")        # Driver code
a = list(bin1)
print (a)
b = a.count("1")
print (b)
if(b%2==0):
    a.append(1)

else:
    a.append(0)
print (a)






