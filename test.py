import random
def sumGenerator():

    sumList = [0,0,0,0]
    
    additionfile = open("addition.txt","r")
    lines = additionfile.readlines()
    print(len(lines))
    sumList[0] = lines[random.randint(0, len(lines))][:-2]
    additionfile.close()

    dividefile = open("divide.txt","r")
    lines = dividefile.readlines()
    print(len(lines))
    sumList[1] = lines[random.randint(0, len(lines))][:-2]
    dividefile.close()

    subtractfile = open("subtract.txt","r")
    lines = subtractfile.readlines()
    print(len(lines))
    sumList[2] = lines[random.randint(0, len(lines))][:-2]
    subtractfile.close()

    multiplyfile = open("multiply.txt","r")
    lines = multiplyfile.readlines()
    print(len(lines))
    sumList[3] = lines[random.randint(0, len(lines))][:-2]
    multiplyfile.close()

    print(sumList)
sumGenerator()
                      
