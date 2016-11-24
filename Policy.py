class policy:
    def __init__(self):
        self.package = None
        self.requestDate = None
        self.policyType = None
        self.vehicleYear = None
        self.price = None
        self.priceDiscount = None

    def newXmlObj(self,package,vehicleYear):
        self.package = package
        self.policyType = "AUTO"
        self.vehicleYear = vehicleYear


    def __str__(self):
        ret = ''
        if self.package != None:
            ret += "\npackage: "+str(self.package)
        if self.requestDate != None:
            ret += "\nrequestDate: "+str(self.requestDate)
        if self.policyType != None:
            ret += "\npolicyType: "+str(self.policyType)
        if self.vehicleYear != None:
            ret += "\nvehicleYear: "+str(self.vehicleYear)
        if self.price != None:
            ret += "\nprice: "+str(self.price)
        if self.priceDiscount != None:
            ret += "\npriceDiscount: "+str(self.priceDiscount)
        return ret

    def getXML(self):

        ret = ''
        if self.package != None:
            ret += "\n<"+str(self.package)+">"
        if self.requestDate != None:
            ret += "\n<requestDate>"+str(self.requestDate)+"</requestDate>"
        if self.policyType != None:
            ret += "\n<policyType>"+str(self.policyType)+"</policyType>"
        if self.vehicleYear != None:
            ret += "\n<vehicleYear>"+str(self.vehicleYear)+"</vehicleYear>"
        if self.price != None:
            ret += "\n<price>"+str(self.price)+"</price>"
        if self.priceDiscount != None:
            ret += "\n<priceDiscount>"+str(self.priceDiscount)+"</priceDiscount>"
        if self.package != None:
            ret += "\n</"+str(self.package)+">"
        return ret
