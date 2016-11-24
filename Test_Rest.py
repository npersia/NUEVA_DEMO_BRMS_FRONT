import Rest
xml = """
<batch-execution  lookup="prueba">
<insert-elements  return-object="true">
<org.acme.insurance.Driver>
<numberOfAccidents>3</numberOfAccidents>
<numberOfTickets>0</numberOfTickets>
<age>12</age>
</org.acme.insurance.Driver>   

<org.acme.insurance.Policy>
<policyType>AUTO</policyType>
</org.acme.insurance.Policy>

</insert-elements>


<fire-all-rules max="10"/>

<query out-identifier="policy" name="getPolicy"/>
<query out-identifier="driver" name="getDriver"/>
<query out-identifier="rejection" name="getRejection"/>


</batch-execution>


"""
headers = {'Content-Type': 'application/xml','Authorization': 'Basic a2llc2VydmVyOmtpZXNlcnZlcjEh','X-KIE-ContentType':'xstream','Accept':'application/xml'} # set what your server accepts
direccion = 'http://localhost:8080/kie-server/services/rest/server/containers/instances/serverContainer'

r = Rest.rest(headers,direccion)
print(r.post(xml))

