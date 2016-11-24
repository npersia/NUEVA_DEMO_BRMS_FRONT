import xml.etree.ElementTree as ET
import Driver
import Policy
import Rejection
a="""
<org.kie.server.api.model.ServiceResponse>
    <type>SUCCESS</type>
    <msg>Container serverContainer successfully called.</msg>
    <result class="execution-results">
        <result identifier="driver">
            <query-results>
                <identifiers>
                    <identifier>driver</identifier>
                </identifiers>
                <row>
                    <identifier id="driver">
                        <org.acme.insurance.Driver>
                            <driverName>Nahuel</driverName>
                            <age>24</age>
                            <price>8450</price>
                            <numberOfAccidents>0</numberOfAccidents>
                            <numberOfTickets>0</numberOfTickets>
                            <creditScore>500</creditScore>
                        </org.acme.insurance.Driver>
                        <fact-handle external-form="0:1:264607785:264607785:1:DEFAULT:NON_TRAIT:org.acme.insurance.Driver"/>
                    </identifier>
                    <identifier id="driver">
                        <org.acme.insurance.Driver>
                            <driverName>Juan</driverName>
                            <age>30</age>
                            <price>50</price>
                            <numberOfAccidents>10</numberOfAccidents>
                            <numberOfTickets>20</numberOfTickets>
                            <creditScore>600</creditScore>
                        </org.acme.insurance.Driver>
                        <fact-handle external-form="0:1:264607785:264607785:1:DEFAULT:NON_TRAIT:org.acme.insurance.Driver"/>
                    </identifier>

                </row>
            </query-results>
        </result>
        <result identifier="rejection">
            <query-results>
                <identifiers/>
            </query-results>
        </result>
        <result identifier="policy">
            <query-results>
                <identifiers>
                    <identifier>policy</identifier>
                </identifiers>
                <row>
                    <identifier id="policy">
                        <org.acme.insurance.Policy>
                            <policyType>AUTO</policyType>
                            <vehicleYear>2009</vehicleYear>
                            <price>450</price>
                            <priceDiscount>10</priceDiscount>
                            <priceSurcharge>100</priceSurcharge>
                        </org.acme.insurance.Policy>
                        <fact-handle external-form="0:2:1699658574:1699658574:7:DEFAULT:NON_TRAIT:org.acme.insurance.Policy"/>
                    </identifier>
                    <identifier id="policy">
                        <org.acme.insurance.Policy>
                            <policyType>AUTO</policyType>
                            <vehicleYear>2009</vehicleYear>
                            <price>8450</price>
                            <priceDiscount>10</priceDiscount>
                            <priceSurcharge>100</priceSurcharge>
                        </org.acme.insurance.Policy>
                        <fact-handle external-form="0:2:1699658574:1699658574:7:DEFAULT:NON_TRAIT:org.acme.insurance.Policy"/>
                    </identifier>

                </row>
            </query-results>
        </result>
    </result>
</org.kie.server.api.model.ServiceResponse>
"""


root = ET.fromstring(a)
#print(root.findall(".//*[@class='execution-results']//*[@identifier='policy']//*/price"))
b=root.findall(".//*[@id='policy']")
#print(len(b))
#c=b[0].findall(".//*/price")

for c in b:
    for i in c.findall(".//*/price"):
        print(i.text)


x=root.findall(".//*[@id='rejection']")
#print(len(x))
#print(x)

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





ejemplo=response(a)
for i in ejemplo.drivers:
    print(i)
for i in ejemplo.policies:
    print(i)
for i in ejemplo.rejections:
    print(i)

