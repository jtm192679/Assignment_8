def printIndex(str, s):
    flag = False;
    for i in range(len(str)):
        if (str[i:i + len(s)] == s):
            print(i, end=" ");
            flag = True;
            x = list(str)
            x.insert((i+3),"0")


        if (flag == False):
            #print("NONE");
        print(x)

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
bin2 = "010"
printIndex(bin1,bin2)
p= a.append("0101")
print (p)







