#im angry

#these are if statements 

condition = True
chicken = False
var1 = 12

if condition == True:
    print "condition is true"
    if chicken == True:
        print "chicken is true"
    else: 
        print "chicken isnt true"

if condition and var1 < 5:
    print "condition is true and var1 is smaller than 5"
elif condition and var1 >5:
    print "condition is true and var1 is bigger than 5"
else:
    print "condition is false OR var1 is exactly 5"

if condition != True:
    print "condition is false"
else:
    print "condition is true"

#loops

#there are 2 kinds of loops
#for loops and while loops

for x in range (0,4):
    print x

y = 0
while condition:
    print "vim is bad"
    y +=1
    if y > 5:
        condition = False

print "those are control structure"
