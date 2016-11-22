class driver:
    def __init__(self,package,driverName,age,numberOfAccidents,numberOfTickets,creditScore):
        self.package = package
        self.driverName = driverName
        self.age = age
        self.ssn = None
        self.dlNumber = None
        self.numberOfAccidents = numberOfAccidents
        self.numberOfTickets = numberOfTickets
        self.creditScore = creditScore


    def __str__(self):
        ret = "driverName: "+str(self.driverName)+"\nage: "+str(self.age)+"\nnumberOfAccidents: "+str(self.numberOfAccidents)+"\nnumberOfTickets: "+str(self.numberOfTickets)+"\ncreditScore: "+str(self.creditScore)
        return ret

    def getXML(self):
        ret = "<"+str(self.package)+">"
        ret += "\n\t<driverName>"+str(self.driverName)+"</driverName>"
        ret += "\n\t<age>"+str(self.age)+"</age>"
        ret += "\n\t<numberOfAccidents>"+str(self.numberOfAccidents)+"</numberOfAccidents>"
        ret += "\n\t<numberOfTickets>"+str(self.numberOfTickets)+"</numberOfTickets>"
        ret += "\n\t<creditScore>"+str(self.creditScore)+"</creditScore>"
        ret += "\n</"+str(self.package)+">"
        return ret    
