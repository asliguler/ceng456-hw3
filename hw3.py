import sys

if len(sys.argv) != 3:
    print("Not enough arguments")
else:
    mainFunc(sys.argv[0], int(sys.argv[1]), int(sys.argv[2]))

def mainFunc(fileName, d, s):
    seqresDict = {}
    atomListDict = {}
    findSeqresAndAtoms(fileName, seqresDict, atomListDict)
    computePairWiseDistances(seqresDict, atomListDict)

class seqres:
    def __init__(self, serNum, chainID, numRes, resName):
        self.serNum = serNum
        self.chainID = chainID
        self.numRes = numRes
        self.resName = resName
class atom:
    def __init__(self, serial, name, altLoc, resName, chainID, x, y, z):
        self.serial = serial
        self.name = name  # we will use carbon-alpha (CA) atoms
        self.altLoc = altLoc
        self.resName = resName
        self.chainID = chainID
        self.x = x
        self.y = y
        self.z = z

def findSeqresAndAtoms(fileName, seqresDict, atomListDict):
    for line in open(fileName):
        lineId = line[0]
        if lineId == 'SEQRES':
            chainId = line[2]
            if chainId not in seqresDict.keys():
                seqresDict[chainId] = line[4:]
            else:
                seqresDict[chainId] = seqresDict[chainId] + line[4:]
        elif lineId == 'ATOM' and line[2] == 'CA':
            chainId = line[5]
            #atomTemp = atom(int(line[1]), line[2], line[3], line[4], line[5], 
            #                float(line[8]), float(line[9]), float(line[10]))
            if chainId not in atomListDict.keys():
                atomListDict[chainId] = [(float(line[8]), float(line[9]), float(line[10]))]
            else:
                atomListDict[chainId] = atomListDict[chainId] + [(float(line[8]), float(line[9]), float(line[10]))]
            
def computePairWiseDistances(seqresDict, atomListDict):
    i = 0
    j = 0
    for chainKey in seqresDict.keys():
        for i in range(len(atomListDict[chainKey])):
            for j in range(i, len(atomListDict[chainKey])):
                pass
