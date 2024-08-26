import base64
import math as m
import generalFunctions as gF

layer = 0

m = open("ASCII85layertext/layer0.txt", "r", encoding="UTF-8")
tekst = m.read()
decrypt = base64.a85decode(tekst, adobe=True).decode('UTF-8')

gF.savePayload(decrypt, layer+1)