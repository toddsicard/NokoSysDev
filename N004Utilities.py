import json
import os


class Kilnini():
    stackpath = ""

    def loadkilnini (self, jini):
        self.__dict__ = json.loads(jini)

    def getkilnini (self, nconfig):
        fconfig = open(nconfig,"r")
        sconfig = fconfig.readline()
        kini.loadkilnini(sconfig)
