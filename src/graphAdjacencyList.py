""" graphAdjacencyList.py

Module implementing adjacency list representation of undirected
simple graphs.

Supplemental Material for the Lecture Notes "Networks - A brief Introduction
using a Paradigmatic Combinatorial Optimization Problem" at the international
summer school "Modern Computational Science 10 - Energy of the Future" held
in Oldenburg, September 3-14, 2018

Author: O. Melchert
Date: 2018-09-11
"""

def fetchWeightedGraph(fileName):
    '''read edge-list from specified file

    Input:
    fileName        - path to file containing edge-list

    Returns: (G)
    G               - directed graph
    '''
    G=UGraphWeighted()
    file = open(fileName,"r")
    for line in file:
        stuff = line.split()
        if len(stuff)>1 and line[0]!='#':
            G.addEdge(int(stuff[0]),int(stuff[1]),float(stuff[2]))
    file.close()
    return G


class UGraph(object):
	"""adjacency-list representation of an undirected simple graph
	"""
	def __init__(self):
		"""default constructor for a new instance of class myGraph"""
		self._nNodes=0
		self._nEdges=0
		self._adjList={}

	@property
	def V(self):
		"""returns node set of the graph"""
		return self._adjList.keys()

	@property
	def nNodes(self):
		"""returns number of nodes in the graph"""
		return self._nNodes

	@property
	def nEdges(self):
		"""returns number of edges in the graph"""
		return self._nEdges

	def adjList(self,node):
		"""returns adjacency list of node"""
		return self._adjList[node]

	def deg(self,node):
		"""returns degree of node"""
		return len(self._adjList[node])

	def addNode(self,node):
		"""add node to graph and create empty adjacency list
		if node is new"""
		if node not in self.V:
			self._adjList[node]=[]
			self._nNodes += 1

	def addEdge(self,fromNode,toNode):
		"""add edge to the graph and update adjacency lists
		of its terminal nodes. If terminal nodes do not
		exist, create them first"""
		flag=0
		self.addNode(fromNode)
		self.addNode(toNode)
		if (fromNode != toNode) and (toNode not in self.adjList(fromNode)):
			self._adjList[fromNode].append(toNode)
			self._adjList[toNode].append(fromNode)
			self._nEdges += 1
			flag=1
		return flag

	__addEdge=addEdge



class UGraphWeighted(UGraph):
    def __init__(self):
        UGraph.__init__(self)
        self._wgt={}

    @property
    def E(self): return self._wgt.keys()

    def wgt(self,edg):
        """return the weight of the edge {fromNod,toNode}"""
        sortedEdge = (min(edg),max(edg))
        return self._wgt[sortedEdge]

    def setWgt(self,e,wgt):
        """set the weight of the edge {fromNod,toNode}"""
        fromNode,toNode = e
        if toNode in self.adjList(fromNode):
            sortedEdge = (min(fromNode,toNode),max(fromNode,toNode))
            self._wgt[sortedEdge]=wgt

    def addEdge(self,fromNode,toNode,wgt=1):
        """add weighted edge to the graph and update adjacency lists
        of its terminal nodes. If terminal nodes do not
        exist, create them first"""
        if self._UGraph__addEdge(fromNode,toNode):
            self.setWgt((fromNode,toNode),wgt)

# EOF: graphAdjacencyList.py
