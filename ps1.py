def printIndex(str, s):
    flag = False;
    for i in range(len(str)):
        if (str[i:i + len(s)] == s):             #taking index of list
            print(i, end=" ");
            flag = True;
            x = list(str)
            x.insert((i + 3), "0")
            print(x)


bin1 = input("enter binary data:")  # Driver code taking input binary data as string
a = list(bin1)                    #converting string into list
print(a)
b = a.count("1")                  #counting for number of ones
print(b)
if (b % 2 == 0):                  #checking for odd and even parity
    a.append(1)

else:
    a.append(0)
print(a)
bin2 = "010"
printIndex(bin1, bin2)               #stuffing 0 after each 010
p = a.append("0101")
print(p)
