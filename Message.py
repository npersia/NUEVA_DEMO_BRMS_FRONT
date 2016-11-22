import Driver
import Policy



class message:
    def __init__(self):
        self.lookup = lookup#nombre de la kiesesion
        self.driver = driver
        self.policy = policy
        self.max_fireallrules = max_fireallrules

    def getXML(self):

        ret = "<<batch-execution  lookup="+str(self.lookup)+">"

        
        ret = "<"+str(self.package)+">"
        ret += "\n\t<driverName>"+str(self.driverName)+"</driverName>"
        ret += "\n\t<age>"+str(self.age)+"</age>"
        ret += "\n\t<numberOfAccidents>"+str(self.numberOfAccidents)+"</numberOfAccidents>"
        ret += "\n\t<numberOfTickets>"+str(self.numberOfTickets)+"</numberOfTickets>"
        ret += "\n\t<creditScore>"+str(self.creditScore)+"</creditScore>"
        ret += "\n</"+str(self.package)+">"
        return ret 
