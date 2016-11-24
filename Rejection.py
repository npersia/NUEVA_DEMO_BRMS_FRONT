class Rejection:
    def __init__(self):
        self.reason = None


    def newXmlObj(self,reason):
        self.reason = reason


    def __str__(self):
        ret = ''
        if self.reason != None:
            ret += "reason: "+str(self.reason)
        return ret
