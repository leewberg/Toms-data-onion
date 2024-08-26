import base64
import math as m
import generalFunctions as gF
from time import time

l = open("ASCII85layertext/layer1.txt", "r", encoding="UTF-8") #det man får når man har dekryptert det på nettsiden
layerOne = l.read()
decrypt = base64.a85decode(layerOne, adobe=True)
#print(decrypt)
binary =  []
for b in decrypt:
    binary.append('{:0>8b}'.format((b)))
#print(len(binary))
#print((binary[0]))

start = time()

for x in binary:
    j = binary.index(x)
    temp = ""
    i=0
    while i < len(x):
        if i%2!= 0:
            if x[i] == "1":
                temp = temp + ("0")
            elif x[i]=="0":
                temp = temp +("1")
        else:
            temp = temp + (x[i])
        i+=1
    binary[j] = temp

#print(binary[0])
slutt = time()
print(f"dette tok {slutt-start} sekunder")
#tar ca 5-12 min

for j in range (len(binary)):
    last = binary[j][-1]
    adding = (binary[j][:-1])
    if last == "1":
        binary[j] = "1{}".format(adding)
    elif last == "0":
        binary[j] = "0{}".format(adding)
#print(binary)


for i in range(len(binary)):
    temp = 0
    for j in range(len(binary[i])-1, -1, -1):
        now = binary[i][j]
        temp+=int(now)*2**(7-j)
    binary[i] = temp
#print(binary[0])


bro = ""
for i in range (len(binary)):
    bro = bro + chr(binary[i])
#print(bro)


for i in range (len(binary)):
    binary[i] = int(binary[i])