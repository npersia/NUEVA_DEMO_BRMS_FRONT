import Driver



a = Driver.driver("org.acme.insurance.Driver","Nahuel",19,0,0,500)
b = Driver.driver("Nahuel",19,0,0,500)
print(a)
print()
print(a.getXML())
print()
print(b)
print()
print(b.getXML())
