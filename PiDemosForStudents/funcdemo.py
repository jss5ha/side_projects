
def goodDiv(num1, num2):
    if (num1/num2==0):
        return float(num1)/float(num2)
    elif (num1%num2!=0):
        return float(num1)/float(num2)
    else:
        return num1/num2
print 1/2
print 4/3
print 6/3
print goodDiv(1,2)
print goodDiv(4,3)
print goodDiv(6,3)

mynum = goodDiv(8,6)
print goodDiv(goodDiv(4,3),goodDiv(2,1))
print goodDiv(mynum, goodDiv(7,5))
