import base64
import generalFunctions as gF

l = open("ASCII85layertext/layer2.txt", "r", encoding="UTF-8")
layerTwo = l.read()
decrypt = base64.a85decode(layerTwo, adobe=True)
binary =  []

layer = 2

for b in decrypt:
    binary.append('{:0>8b}'.format((b)))

i=0
while i < (len(binary)):
    length = len(binary)
    temp = binary[i]
    numOnes = temp[:7].count("1")

    #remove invalid bytes
    if numOnes%2!=0 and temp[-1]!="1":
        binary.pop(i)
        i -=1
    elif numOnes%2 == 0 and temp[-1] == "1":
        binary.pop(i)
        i-=1
    i+=1

binaryLongString=""
for x in binary:
    for y in range (7):
        binaryLongString+=x[y]

binaryReListed = []
for k in range (0, len(binaryLongString), 8):
    tempBin = binaryLongString[k:k+8]
    binaryReListed.append(tempBin)

for i in range(len(binaryReListed)):
    temp = 0
    for j in range(len(binaryReListed[i])-1, -1, -1):
        now = binaryReListed[i][j]
        temp+=int(now)*2**(7-j)
    binaryReListed[i] = temp

payload = ""
for i in range (len(binaryReListed)):
    payload = payload + chr(binaryReListed[i])

gF.savePayload(payload, layer+1)