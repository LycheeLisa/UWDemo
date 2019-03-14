import pandas as pd


class Cluster():

    def __init__(self, cluster):
        self.cluster = cluster
        self.clusterMat = self.readFile()
        self.clusterInfo = self.clusterMat[cluster]

    def readFile(self):
        data = pd.read_csv("static/data/graphics_files.txt", delimiter="\t", encoding="cp1252", header=None)
        data = data.values.tolist()
        return data

    def update(self, cluster):
        self.cluster = cluster
        self.clusterInfo = self.clusterMat[cluster]

    def getInfo(self):
        return self.clusterInfo

    def getNum(self):
        return self.cluster

    def getClusName(self):
        return self.clusterInfo[1]

    def getPic(self):
        return self.clusterInfo[4]

    def getProfName(self):
        return self.clusterInfo[5]

    def getFaculty(self):
        return self.clusterInfo[6]

    def getProgram(self):
        return self.clusterInfo[7]

    def getQuote(self):
        return self.clusterInfo[8]

    def getStats(self):
        stats = [int(self.clusterInfo[x]) for x in range(9,13)]
        return stats

    def getAbout(self):
        return self.clusterInfo[13]

    def getNeeds(self):
        needs = [str(self.clusterInfo[x]) for x in range(14,18)]
        return needs
