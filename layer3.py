import base64
import generalFunctions as gF

layerThree = open("ASCII85layertext/layer3.txt", "r", encoding="UTF-8").read()
decrypt = base64.a85decode(layerThree, adobe=True)

layer = 3
binary =  []

for b in decrypt:
    binary.append('{:0>8b}'.format((b)))


for i in range(len(binary)):
    temp = 0
    for j in range(len(binary[i])-1, -1, -1):
        now = binary[i][j]
        temp+=int(now)*2**(7-j)
    binary[i] = temp
#print(binary)

#the key i 32 bytes long
#we know that the key will start with this:
start = "==[ Layer 4/6: "
startValues = []
for x in range(len(start)):
    startValues.append(ord(start[x])) #we use ord to convert between ASCII and integers

key = []
for i in range(32):
    key.append(0)

for j in range(len(startValues)):
    key[j] = (startValues[j] ^ binary[j])

#we manually find the correct values for the keys based on what we know needs to be there
key[len(binary)%32-1] = binary[len(binary)-1] ^ ord(">")
key[len(binary)%32-2] = binary[len(binary)-2] ^ ord("~")
key[59%32] = binary[59] ^ ord("\n")
key[60%32] = binary[60] ^ ord("\n")
key[29] = binary[29] ^ ord("c")
key[27] = binary[27] ^ ord("f")
key[62%32] = binary[62] ^ ord("W")
key[63%32] = binary[63] ^ ord("h")

firstLine = "="*28
for i in range(32,59):
    key[i%32] = ord(firstLine[i%len(firstLine)]) ^ binary[i]


payload=""
for k in range(len(binary)):
    payload = payload +(chr(key[k%32] ^ binary[k]))

gF.savePayload(payload, layer + 1)