import json
import os

class Kilnini:
    stackpath = ""

    def loadkilnini (self, jini):
        self.__dict__ = json.loads(jini)

    def getkilnini (self, nconfig):
        fconfig = open(nconfig,"r")
        sconfig = fconfig.readline()
        kini.loadkilnini(sconfig)

#class readfiles:
#FIX rewrite to call lastbrick as an attribute
kini = Kilnini()
kini.getkilnini("config.ini")


lastbrick = "ss"

brkfiles = []
brkfiles = os.listdir(kini.stackpath)
brkfiles.sort(reverse=True)
    
blocksall = '[{"BlockTop": "True"}'
for nbrk in brkfiles:
    fbrk = open(kini.stackpath+"\\"+nbrk,"r")
    blocksall += ','+fbrk.readline()
blocksall += "]"

print(blocksall)
        
