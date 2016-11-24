class driver:
    def __init__(self):
        self.package = None
        self.driverName = None
        self.age = None
        self.ssn = None
        self.dlNumber = None
        self.numberOfAccidents = None
        self.numberOfTickets = None
        self.creditScore = None
 
    def newXmlObj(self,package,driverName,age,numberOfAccidents,numberOfTickets,creditScore):
        self.package = package
        self.driverName = driverName
        self.age = age
        self.numberOfAccidents = numberOfAccidents
        self.numberOfTickets = numberOfTickets
        self.creditScore = creditScore

    def __str__(self):
        ret = ''
        if self.package != None:
            ret += "package: "+str(self.package)
        if self.driverName != None:
            ret += "\ndriverName: "+str(self.driverName)
        if self.age != None:
            ret += "\nage: "+str(self.age)
        if self.ssn != None:
            ret += "\nssn: "+str(self.ssn)
        if self.dlNumber != None:
            ret += "\ndlNumber: "+str(self.dlNumber)
        if self.numberOfAccidents != None:
            ret += "\nnumberOfAccidents: "+str(self.numberOfAccidents)
        if self.numberOfTickets != None:
            ret += "\nnumberOfTickets: "+str(self.numberOfTickets)
        if self.creditScore != None:
            ret += "\ncreditScore: "+str(self.creditScore)
        return ret

    def getXML(self):
        ret = ''
        if self.package != None:
            ret += "<"+str(self.package)+">"
        if self.driverName != None:
            ret += "\n<driverName>"+str(self.driverName)+"</driverName>"
        if self.age != None:
            ret += "\n<age>"+str(self.age)+"</age>"
        if self.ssn != None:
            ret += "\n<ssn>"+str(self.ssn)+"</ssn>"
        if self.dlNumber != None:
            ret += "\n<dlNumber>"+str(self.dlNumber)+"</dlNumber>"
        if self.numberOfAccidents != None:
            ret += "\n<numberOfAccidents>"+str(self.numberOfAccidents)+"</numberOfAccidents>"
        if self.numberOfTickets != None:
            ret += "\n<numberOfTickets>"+str(self.numberOfTickets)+"</numberOfTickets>"
        if self.creditScore != None:
            ret += "\n<creditScore>"+str(self.creditScore)+"</creditScore>"
        if self.package != None:    
            ret += "\n</"+str(self.package)+">"
        return ret    
