import DuetWebAPI as DWA
import json

# Test cases

D100 = DWA.DuetWebAPI('http://192.168.7.100')
D101 = DWA.DuetWebAPI('http://192.168.7.101')
D127 = DWA.DuetWebAPI('http://127.0.0.1')

print("Printer Type D100 is ",D100.printerType())
print("Printer Type D101 is ",D101.printerType())
print("Printer Type D127 is ",D127.printerType())

print("D100 coordiates are",D100.getCoords())

d=D101.getCoords()
print("D101 coordiates are",d)
print("D101 X axis is ",d['X'])



D101.gCode("G91 G1 X0.5 G90")
