import Driver
import Policy



class message:
    def __init__(self,lookup,max_fireallrules,driver,policy):
        self.lookup = lookup#nombre de la kiesesion
        self.driver = driver
        self.policy = policy
        self.max_fireallrules = max_fireallrules

    def getXML(self):

        ret = "<batch-execution lookup='"+str(self.lookup)+"'>"
        ret += "\n<insert-elements return-object='false'>"
        ret += "\n"
        ret += str(self.driver.getXML())
        ret += "\n"
        ret += str(self.policy.getXML())
        ret += "\n</insert-elements>"
        ret += "\n<fire-all-rules max='"+str(self.max_fireallrules)+"'/>"
        ret += "\n<query out-identifier='policy' name='getPolicy'/>"
        ret += "\n<query out-identifier='driver' name='getDriver'/>"
        ret += "\n<query out-identifier='rejection' name='getRejection'/>"
        ret += "\n</batch-execution>"
        return ret
