import Driver
class Policy:
    def __init__(self,vehicleYear,driver):
        self.requestDate = None
        self.policyType = "AUTO"
        self.vehicleYear = vehicleYear
        self.price = None
        self.priceDiscount = None
        self.driver = driver


    def __str__(self):
        ret = "vehicleYear: "+str(self.vehicleYear)+"\ndriver: \n"+str(self.driver)
        return ret






"""
a = Driver.Driver("Nahuel",26,0,5,200)
p=Policy(1990,a)
print(p)"""
