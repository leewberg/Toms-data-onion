import base64

def decrpytASCII85(text):
    return base64.a85decode(text, adobe=True)

def toInt(text):
    for i in range(len(text)):
        temp = 0
        for j in range(len(text[i])-1, -1, -1):
            now = text[i][j]
            temp+=int(now)*2**(7-j)
        text[i] = temp
    return text

def toSingleInt(val):
    temp = 0
    length = len(val)-1
    for j in range(length, -1, -1):
        now = val[j]
        temp+=int(now)*2**(length-j)
    val = temp
    return val


def toBinary (tekst):
    binary =  []
    for b in tekst:
        binary.append('{:0>8b}'.format((b)))
    return binary

def saveToFile(data:str, filepath:str) -> None:
    f = open(filepath, "w")
    f.write(data)
    f.close()
    return None

def savePayload(payload:str, layernumber:int) -> None:
    pl = ""
    instruction = payload[0]
    plStart = 0
    for i in range(2, len(payload)):
        if payload[i-1] == "<" and payload[i] == "~":
            plStart = i - 1
            break
    
    instruction = payload[:plStart]
    print(instruction)

    pl = payload[plStart:]
    saveToFile(pl, "ASCII85layertext/layer"+str(layernumber)+".txt")