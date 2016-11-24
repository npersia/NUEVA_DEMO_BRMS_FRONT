import xml.etree.ElementTree as ET
import Driver
import Policy
import Rejection




class response:
    def __init__(self,msj):
        self.root = ET.fromstring(msj)
        self.policies = self.generatePolicies(self.root.findall(".//*[@id='policy']"))
        self.drivers = self.generateDrivers(self.root.findall(".//*[@id='driver']"))
        self.rejections = self.generateRejections(self.root.findall(".//*[@id='rejection']"))
       
    def generateDrivers(self,drivers):
        ret = []
        for d in drivers:
            aDriver = Driver.driver()
            try:            
                aDriver.driverName = d.findall(".//*/driverName")[0].text
            except:
                aDriver.driverName = None
            try:
                aDriver.age = d.findall(".//*/age")[0].text
            except:
                aDriver.age = None
            try:
                aDriver.ssn = d.findall(".//*/ssn")[0].text
            except:
                aDriver.ssn = None
            try:
                aDriver.dlNumber = d.findall(".//*/dlNumber")[0].text
            except:
                aDriver.dlNumber = None
            try:
                aDriver.numberOfAccidents = d.findall(".//*/numberOfAccidents")[0].text
            except:
                aDriver.numberOfAccidents = None
            try:
                aDriver.numberOfTickets = d.findall(".//*/numberOfTickets")[0].text
            except:
                aDriver.numberOfTickets = None
            try:
                aDriver.creditScore = d.findall(".//*/creditScore")[0].text
            except:
                aDriver.creditScore = None



            ret.append(aDriver)
        return ret


    def generatePolicies(self,policies):
        ret = []
        for p in policies:
            aPolicy = Policy.policy()
            try:
                aPolicy.requestDate = p.findall(".//*/requestDate")[0].text
            except:
                aPolicy.requestDate = None
            try:
                aPolicy.policyType = p.findall(".//*/policyType")[0].text
            except:
                aPolicy.policyType = None
            try:
                aPolicy.vehicleYear = p.findall(".//*/vehicleYear")[0].text
            except:
                aPolicy.vehicleYear = None
            try:
                aPolicy.price = p.findall(".//*/price")[0].text
            except:
                aPolicy.price = None
            try:
                aPolicy.priceDiscount = p.findall(".//*/priceDiscount")[0].text
            except:
                aPolicy.price = None
            ret.append(aPolicy)
        return ret

    def generateRejections(self,rejections):
        ret = []
        for r in rejections:
            aRejection = Rejection.rejection()
            try:
                aRejection.reason= p.findall(".//*/reason")[0].text
            except:
                aRejection.reason = None
            ret.append(aRejection)
        return ret

