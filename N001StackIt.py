def StackIt(payload):
    import datetime
    import json
    import os
    import N004Utilities

    class Kilnini:
        stackpath = ""

        def loadkilnini (self, jini):
            self.__dict__ = json.loads(jini)

        def getkilnini (self, nconfig):
            fconfig = open(nconfig,"r")
            sconfig = fconfig.readline()
            kini.loadkilnini(sconfig)

    class Brickfiles:
        #FIX rewrite to call lastbrick as an attribute
        lastbrick = "ss"

        def getlastbrick(self):
            #RISK will bomb if any non-.brk files exist
            brkfiles = []
            brkfiles = os.listdir(kini.stackpath)
            brkfiles.sort(reverse=True)
            lastbrick = brkfiles[0]
            return lastbrick

        def getbrickcontent(self,nbrk):
            fbrk = open(nbrk,"r")
            sbrk = fbrk.readline()
            return sbrk

    def msghas(msg):
        #import hashlib
        from hashlib import sha512
        m = sha512()
        msgstr = str(msg)
        m.update(msgstr.encode('utf-16'))
        h = m.hexdigest()
        return h

    def writefile(filepath, filename, filecontent):
        file = open(filepath + "\\" + filename, "w")
        file.writelines(filecontent)
        file.close()
        return "1"

    
    #
    # Read config.ini
    kini = Kilnini()
    kini.getkilnini("config.ini")

    #
    # Read existing files, find last brick, and hash content
    bricks = Brickfiles()
    bpname = bricks.getlastbrick()
    thelastbrk = kini.stackpath + "\\" + bpname
    thelastbrkcontent = bricks.getbrickcontent(thelastbrk)
    bphash = msghas(thelastbrkcontent)


    #
    # Create kitchen attributes and header subassembly

    btime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    bfname = btime.replace("-","") + ".nbk"

    bhdr = '"BlockHeader": {'
    bhdr += '"BlockDateTime": "'+btime+'"'
    bhdr += ',"PrevBlockFile": "'+bpname+'"'
    bhdr += ',"PrevBlockHash": "'+bphash+'"'
    bhdr += ',"KilnOwner": "'+kini.whoami+'"'
    bhdr += ',"KilnVersion": "'+kini.kilnversion+'"'
    bhdr += '}'

    #
    # Prep payload subassembly
    bpayld = '"BlockContent": {'
    bpayld += payload
    bpayld += '}'

    #
    # Assemble the subassemblies
    bcontent = '{'+bhdr+', '+bpayld+'}'

    #
    # Write file
    writefile(kini.stackpath,bfname,bcontent)
    return bfname

    

