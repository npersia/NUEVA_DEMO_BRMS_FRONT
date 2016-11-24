import Policy

p = Policy.policy()
p.newXmlObj("org.acme.insurance.Policy",2009)
print(p)
print(p.getXML())
