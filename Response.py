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
        #self.policies = self.root.findall(".//*[@id='policy']")
        self.drivers = self.generateDrivers(self.root.findall(".//*[@id='driver']"))
        #self.rejections = self.root.findall(".//*[@id='rejection']")
       
    def generateDrivers(self,drivers):
        ret = []
        for d in drivers:
            aDriver = Driver.driver("",\
                                d.findall(".//*/driverName")[0].text,\
                                d.findall(".//*/age")[0].text,\
                                d.findall(".//*/numberOfAccidents")[0].text,\
                                d.findall(".//*/numberOfTickets")[0].text,\
                                d.findall(".//*/creditScore")[0].text)
            ret.append(aDriver)
        return ret


    def generatePolicies(self,policies):
        ret = []
        for p in policies:
            aPolicy = Policy.policy("",\
                                d.findall(".//*/driverName")[0].text,\
                                d.findall(".//*/age")[0].text,\
                                d.findall(".//*/numberOfAccidents")[0].text,\
                                d.findall(".//*/numberOfTickets")[0].text,\
                                d.findall(".//*/creditScore")[0].text)
            ret.append(aDriver)
        return ret





ejemplo=response(a)
for i in ejemplo.drivers:
    print(i)
