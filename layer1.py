import base64
import generalFunctions as gF

layer = 1

l = open("ASCII85layertext/layer1.txt", "r", encoding="UTF-8") 
layerOne = l.read()
decrypt = base64.a85decode(layerOne, adobe=True)

#create a list of every single byte rewritten as a string with a length of 8
binary =  []
for b in decrypt:
    binary.append('{:0>8b}'.format((b)))


#flip every second bit
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


#rotate to the right
for j in range (len(binary)):
    last = binary[j][-1]
    adding = (binary[j][:-1])
    binary[j] = last+adding


for i in range(len(binary)):
    temp = 0
    for j in range(len(binary[i])-1, -1, -1):
        now = binary[i][j]
        temp+=int(now)*2**(7-j)
    binary[i] = temp


payload = ""
for i in range (len(binary)):
    payload = payload + chr(binary[i])

gF.savePayload(payload, layer)