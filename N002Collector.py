class PayloadCollector():
    def __init__(self):
        self.msgs = []

    def newmsg(self, nmsg):
        self.msgs.append(nmsg)

    def allmsgs(self):
        return "[" + ", ".join( str(x) for x in self.msgs) + "]"

