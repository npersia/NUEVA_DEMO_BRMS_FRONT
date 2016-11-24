import Message
import Driver
import Policy

#kiesesion
#maxima cantidad de ejecuciones
#driver
#policy
m = Message.message("prueba",\
                    10,\
                    Driver.driver().newXmlObj("org.acme.insurance.Driver","Nahuel",19,0,0,500),\
                    Policy.policy().newXmlObj("org.acme.insurance.Policy",2009)\
)


print(m.getXML())
