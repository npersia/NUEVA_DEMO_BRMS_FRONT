import Driver



a = Driver.driver()
a.newXmlObj("org.acme.insurance.Driver","Nahuel",19,0,0,500)
print(a)
print()
print(a.getXML())
