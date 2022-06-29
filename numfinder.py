import time
startTime = time.time()
add,sub,mult,devi = [],[],[],[]
for x in range(10,1000):
    for y in range(1,100):
        if len(str(x)+str(y)+str(x+y)) == 6:
            add.append(str(x)+"+"+str(y)+"="+str(x+y))
        if len(str(x)+str(y)+str(x-y)) == 6:
            sub.append(str(x)+"-"+str(y)+"="+str(x+-y))
        if len(str(x)+str(y)+str(x*y)) == 6:
            mult.append(str(x)+"*"+str(y)+"="+str(x*y))
        if len(str(x)+str(y)+(str(x/y).split(".")[0])) == 6 and x%y == 0:
            devi.append(str(x)+"/"+str(y)+"="+(str(x/y).split(".")[0]))
print("Found "+str(len(add)+len(sub)+len(mult)+len(devi))+" sums in "+str(time.time()-startTime)+" Seconds")
print("Addition sums found : "+str(len(add)))
print("Subtract sums found : "+str(len(sub)))
print("Multiplication sums found : "+str(len(mult)))
print("Division sums found : "+str(len(devi)))

additionfile = open("addition.txt","a")
for i in add: additionfile.write(i+"\n")
subtractfile = open("subtract.txt","a")
for i in sub: subtractfile.write(i+"\n")
multiplyfile = open("multiply.txt","a")
for i in mult: multiplyfile.write(i+"\n")
dividefile = open("divide.txt","a")
for i in devi: dividefile.write(i+"\n")
additionfile.close()
subtractfile.close()
multiplyfile.close()
dividefile.close()
