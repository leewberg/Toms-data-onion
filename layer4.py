import generalFunctions as gF
layerFour = open("ASCII85layertext/layer4.txt", "r", encoding="UTF-8").read()
decrypt = gF.decrpytASCII85(layerFour)
binary = gF.toBinary(decrypt)
print(binary[20:28])

def checkOverflow(values, selLen):
    if len(values) > selLen:
        if values[0] == "0":
            values = values[1:]
        elif values[0] == "1":
            carry = values [0]
            values = values[1:]
            addTwoBins(carry, values, selLen)
    return values

def addTwoBins(bin1, bin2, selLen:int):
    tempBin = str(bin(int(bin1, 2) + int(bin2, 2)))
    tempBin = tempBin[2:]
    tempBin = checkOverflow(tempBin, selLen)
    if len(tempBin) < selLen and selLen == 8:
        tempBin = '{:0>8}'.format((tempBin))
    elif len(tempBin) < selLen and selLen == 16:
        tempBin = '{:0>16}'.format((tempBin))
    return tempBin

def flipAll(binary):
    result = ""
    for i in range (len(binary)):
        if binary[i] =="0":
            result += "1"
        elif binary[i] == "1":
            result += "0"
    return result

def calcUDP (allUDP):
    currUDPCheck = allUDP[6] + allUDP[7]
    udpToBeAdded = []
    for i in range (0, 6, 2):
        udpToBeAdded.append(allUDP[i]+allUDP[i+1])
    tempBin = udpToBeAdded[0]
    for i in range(1, 3):
        newTempBin = addTwoBins(tempBin, udpToBeAdded[i], 16)
        tempBin = newTempBin
    if flipAll(tempBin) == currUDPCheck:
        return "riktig"
    else:
        return "feil"

def calcIPv4(allIP):
    currIPCheck = allIP[10] + allIP[11]
    valsToBeCalculated = []
    for i in range (0, 20, 2):
        valsToBeCalculated.append(allIP[i] + allIP[i+1])
    valsToBeCalculated[5] = "0000000000000000"
    tempBin = valsToBeCalculated[0]
    for i in range(1,10):
        newTempBin = addTwoBins(tempBin, valsToBeCalculated[i], 16)
        tempBin = newTempBin
    tempBin = flipAll(tempBin)
    if tempBin == currIPCheck:
        return "riktig"
    else:
        return "feil"
    
def findIPPorts(ipv4Data:list):
    """
    functions that finds the current source- and destiation IP-ports given the current IPV4 data. returns a tuple containing first the source IP-adress, and then the destitation IP-adress
    """
    sourceIP = str(gF.toSingleInt(ipv4Data[12])) +"."+str(gF.toSingleInt(ipv4Data[13])) +"." +str(gF.toSingleInt(ipv4Data[14])) +"." +str(gF.toSingleInt(ipv4Data[15]))
    
    destIP = str(gF.toSingleInt(ipv4Data[16]))+"."+str(gF.toSingleInt(ipv4Data[17]))+"."+str(gF.toSingleInt(ipv4Data[18]))+"."+str(gF.toSingleInt(ipv4Data[19]))
    return sourceIP, destIP

def isValidByte(liste):
    ipv4 = liste[:20]
    udp = liste[20:28]
    try:
        length = gF.toSingleInt(ipv4[2] + ipv4[3])-28
        mandUDPChecksum = (udp[6]+udp[7]) #må sjekkes
        currUDPCheck = (udp[6]+udp[7]) #må sjekkes  

        #sjekkUDPChecksum = calculateRightUDPChecksum(udp) <- denne skal erstatte curr og mand UDPcheck, ettersom den kommer til å returnere True når checksumen er riktig og kan da brukes direkte
        checkIPV4 = calcIPv4(ipv4)
        currDestport = gF.toSingleInt(udp[2]+udp[3])
        currSourceIP, currDestIP = findIPPorts(ipv4)
        #currSourceIP = str(gF.toSingleInt(ipv4[12])) +"."+str(gF.toSingleInt(ipv4[13])) +"." +str(gF.toSingleInt(ipv4[14])) +"." +str(gF.toSingleInt(ipv4[15]))
        #currDestIP = str(gF.toSingleInt(ipv4[16]))+"."+str(gF.toSingleInt(ipv4[17]))+"."+str(gF.toSingleInt(ipv4[18]))+"."+str(gF.toSingleInt(ipv4[19]))
    except:
        length = mandUDPChecksum = currUDPCheck =  currDestport = currSourceIP = currDestIP = checkIPV4 = 0
    mandDestport = 42069
    mandDestIP = "10.1.1.200"
    mandSourceIP = "10.1.1.10"
    if mandUDPChecksum == currUDPCheck and  checkIPV4 == "riktig" and currDestport == mandDestport and currDestIP == mandDestIP and currSourceIP == mandSourceIP: 
        svar = "riktig"
    else:
        svar = "galt"    
    return (svar, length)


lengde = len(binary)
finalList = []
antallGangerKjort = 0

for i in range(lengde):
    (svar, leng) = isValidByte(binary)
    if svar == "riktig":
        for j in range (28):
            binary.pop(0)
        for j in range(leng):
            finalList.append(binary[0])
            binary.pop(0)
    else:
        try:
            for j in range(28+leng):
                binary.pop(0)
        except:
            for j in range (len(binary)):
                binary.pop(0)
    lengde = len(binary)
    antallGangerKjort+=1

finalList = gF.toInt(finalList)

bro = ""
for i in range (len(finalList)):
    bro = bro + chr(finalList[i])
print(bro)
