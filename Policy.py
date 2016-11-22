class policy:
    def __init__(self,package,vehicleYear):
        self.package = package
        self.requestDate = None
        self.policyType = "AUTO"
        self.vehicleYear = vehicleYear
        self.price = None
        self.priceDiscount = None


    def __str__(self):
        ret = "vehicleYear: "+str(self.vehicleYear)
        return ret

    def getXML(self):
        ret = "<"+str(self.package)+">"
        ret += "\n<vehicleYear>"+str(self.vehicleYear)+"</vehicleYear>"
        ret += "\n<policyType>"+str(self.policyType)+"</policyType>"
        ret += "\n</"+str(self.package)+">"
        return ret
