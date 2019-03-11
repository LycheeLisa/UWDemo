import csv


class Cluster(FlaskForm):

    def __init__(self, cluster):
    self.fileName = fileName
    self.cluster = cluster
    self.clusterMat = readFile()
    self.clusterInfo = clusterMat[cluster]

    def readFile(self):
        f = open("static/data/graphics_files.txt", "rb")
        reader = csv.reader(f, delimiter = "\t")
        data = list(reader)
        f.close()
        return data
    def getClusterInfo(self):
        return self.clusterInfo
