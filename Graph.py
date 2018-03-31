import pprint
import time


class DirectedGraph:
    def __init__(self, fileName):
        self.fileName = fileName
        # one node has the next form: 1:{inbound: {2:45,3:22,4:12}, outbound:{5:45,2:45,3:23}}
        self.nodes = {}
        self.readFromFile()

    def readFromFile(self):
        start = time.time()
        file = open(self.fileName, "r")
        firstLine = file.readline()[:-1].split(" ")
        nrOfNodes = int(firstLine[0])
        nrOfEdges = int(firstLine[1])
        for i in range(nrOfNodes):
            self.nodes[str(i)] = {"inbound": {}, "outbound": {}}
        for i in range(nrOfEdges):
            currentLine = file.readline()[:-1].split(" ")
            _from = currentLine[0]
            _to = currentLine[1]
            _cost = currentLine[2]
            self.nodes[_from]["outbound"][_to] = _cost
            self.nodes[_to]["inbound"][_from] = _cost
        stop = time.time()
        print("Loaded file {0} in {1} seconds".format(self.fileName, stop - start))

    def getNumberOfVertices(self):
        return len(self.nodes)

    def checkIfEdge(self, _from, _to):
        if _from in self.nodes and _to in self.nodes[_from]["outbound"]:
            return (_from, _to)
        return None

    def getInDegree(self, node):
        if node in self.nodes:
            return len(self.nodes[node]["inbound"])
        return None

    def getOutDegree(self, node):
        if node in self.nodes:
            return len(self.nodes[node]["outbound"])
        return None

    def getInbound(self, node):
        # return a dict which is an iterable so it has an iterator on it
        if node in self.nodes:
            return self.nodes[node]["inbound"]
        return None

    def getOutbound(self, node):
        if node in self.nodes:
            return self.nodes[node]["outbound"]
        return None

    def getCost(self, _from, _to):
        if _from in self.nodes and _to in self.nodes[_from]:
            return self.nodes[_from]["outbound"][_to]
        return None

    def setCost(self, _from, _to, newCost):
        if self.getCost(_from, _to) is not None:
            self.nodes[_from]["outbound"][_to] = newCost
            self.nodes[_to]["inbound"][_from] = newCost

    def addNode(self, node):
        if node in self.nodes:
            raise Exception("Node already exists")
        self.nodes[node] = {"inbound": {}, "outbound": {}}

    def removeNode(self, node):
        if node in self.nodes:
            del self.nodes[node]

    def addEdge(self, _from, _to, cost):
        if _from in self.nodes and _to in self.nodes:
            if _to not in self.nodes[_from]["outbound"]:
                self.nodes[_from]["outbound"][_to] = cost
                self.nodes[_to]["inbound"][_from] = cost
            else:
                raise Exception("There is already an edge between {0} and {1}".format(_from, _to))
        elif _to not in self.nodes:
            raise Exception("Outbound node {0} does not exist".format(_to))
        elif _from not in self.nodes:
            raise Exception("Inbound node {0} does not exist".format(_from))

    def removeEdge(self, _from, _to):
        if _from in self.nodes and _to in self.nodes and _to in self.nodes[_from]["outbound"]:
            del self.nodes[_from]["outbound"][_to]
            del self.nodes[_to]["inbound"][_from]


if __name__ == '__main__':
    a = DirectedGraph("graph1k.txt")
