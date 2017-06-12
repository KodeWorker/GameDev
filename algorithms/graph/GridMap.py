""" GRID MAP MODULE
# Description:
    This is basic 2-D GridMap object for path-finding and visibility algorithms.
# Dependencies: Networkx, Numpy
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/06/09
"""
from networkx import Graph
import numpy as np

class GridMap(Graph):    
    def __init__(self, width, height, mtype='bounded'):
        """ GridMap Graph
            It is implemented with graph object(netwokx.Graph).
            Easy to do the graph manipulation, but the overall cost is slightly higher.            
        Parameters
        ----------
        width: int
            Width of the grid.
        height: int
            Height of the grid.
        mtype: string, optional
        
        Attributes
        ---------
        V: list
            A list of all vertices in the grid.
        E: list
            A list of all edges in the grid.
        """
        super().__init__()
        self.width = width
        self.height = height
        self.mtype = mtype
        self.__initGrid()
    
    def __initGrid(self):
        self.V = [(x, y) for x in range(self.width) for y in range(self.height)]
        if self.mtype == 'bounded' or  self.mtype == 'boundless':
            self.E = self.__genGridEdge()
            self.add_edges_from(self.E)            
        else:
            raise ValueError('- mtype not supported -')
        for keys in self.node.keys():
            self.node[keys]['cost'] = 1            
            self.node[keys]['sight'] = 1
            self.node[keys]['vision'] = 0
    
    def __genGridEdge(self):
        Edge = []
        for i in range(len(self.V)):            
            # It checks only the neighboring vertices and performs better when number of grids is huge
            V_ = [(self.V[i][0]-1, self.V[i][1]-1), (self.V[i][0], self.V[i][1]-1), (self.V[i][0]+1, self.V[i][1]-1),\
                  (self.V[i][0]-1, self.V[i][1]),                                   (self.V[i][0]+1, self.V[i][1]),\
                  (self.V[i][0]-1, self.V[i][1]+1), (self.V[i][0], self.V[i][1]+1), (self.V[i][0]+1, self.V[i][1]+1)]
            
            for j in range(len(V_)):
                if self.mtype == 'bounded' \
                and (V_[j][0] >= 0 and V_[j][0] < self.width) \
                and (V_[j][1] >= 0 and V_[j][1] < self.height):
                    Edge.append((self.V[i], V_[j]))
                
                elif self.mtype == 'boundless':
                    (x, y) = V_[j]  
                    
                    # boundless setting on x-asix
                    if V_[j][0] < 0 :
                        x = V_[j][0] + self.width
                    elif V_[j][0] >= self.width:
                        x = V_[j][0] - self.width
                    # boundless setting on y-asix
                    if V_[j][1] < 0:
                        y = V_[j][1] + self.height
                    elif V_[j][1] >= self.height:
                        y = V_[j][1] - self.height
                        
                    Edge.append((self.V[i], (x, y)))
        return Edge
    
    def setCost(self, cNode, nNode, value):
        self.node[nNode]['cost'] = value
    
    def getCost(self, cNode, nNode):
        """ Cost of Path
        Parameters
        ----------
        cNode: tuple
            Current vertice on the grid (origin).
        nNode: tuple
            Next vertice on the grid (target).
        """
        
#        if cNode in self.V:
#            if nNode in self.edge[cNode].keys():
#                if 'cost' in self.edge[cNode][nNode].keys():
#                    cost = self.edge[cNode][nNode]['cost']
#                else:
#                    cost = 1
#            else:
#                raise ValueError('- next node is not in the neighbors -')
#        else:
#            raise ValueError('- current node is not in the graph -')        
        return self.node[nNode]['cost']
            
    def setSight(self, node, value):
        self.node[node]['sight'] = value
    
    def getSight(self, node):
        return self.node[node]['sight']
    
    def setVision(self, node, value):
        self.node[node]['vision'] = value
    
    def getVision(self, node):
        return self.node[node]['vision']
    
class gridMap():
    def __init__(self, width, height, mtype='bounded'):
        """ GridMap Graph
            Primitive structure implemented with numpy array.
            This graph costs lower init. time but slightly higher search cost.
            The vertices in the grid cannot be removed, it can be manipulated with "cost" in the grid.
        Parameters
        ----------
        width: int
            Width of the grid.
        height: int
            Height of the grid.
        mtype: string, optional
        
        Attributes
        ---------
        grid: numpy.array
            Stores a dictionary in each grid.
        """
        self.width = width
        self.height = height
        self.mtype = mtype
        self.__initGrid()
        
    def __initGrid(self):
        
        if self.mtype == 'bounded' or  self.mtype == 'boundless':
            self.grid = np.empty([self.width, self.height], dtype=dict)
            
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    self.grid[i, j] = {'cost': 1, 'sight': 1, 'vision': 0}
            
        else:
            raise ValueError('- mtype not supported -')
    
    def neighbors(self, pos):
        """ Get Neighbors
        Parameters
        ----------
        pos: tuple
            The position on the grid for neighbor searching.
        """
        N = [(pos[0]-1, pos[1]-1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]-1), \
             (pos[0]-1, pos[1]),                       (pos[0]+1, pos[1]), \
             (pos[0]-1, pos[1]+1), (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1)]
        
        neighbor = []
        if self.mtype == 'bounded':
            for n in N:
                if (n[0] >= 0 and n[0] < self.width) and (n[1] >= 0 and n[1] < self.height):
                    neighbor.append(n)
        elif self.mtype == 'boundless':
            for n in N:
                (x, y) = n
                    
                # boundless setting on x-asix
                if n[0] < 0 :
                    x = n[0] + self.width
                elif n[0] >= self.width:
                    x = n[0] - self.width
                # boundless setting on y-asix
                if n[1] < 0:
                    y = n[1] + self.height
                elif n[1] >= self.height:
                    y = n[1] - self.height
                    
                neighbor.append((x, y))
                    
        return neighbor
    
    def setCost(self, cNode, nNode, value):
        self.grid[nNode[0], nNode[1]]['cost'] = value
    
    def getCost(self, cNode, nNode):
        return self.grid[nNode[0], nNode[1]]['cost']
    
    def setSight(self, node, value):
        self.grid[node[0], node[1]]['sight'] = value
    
    def getSight(self, node):
        return self.grid[node[0], node[1]]['sight']
    
    def setVision(self, node, value):
        self.grid[node[0], node[1]]['vision'] = value
    
    def getVision(self, node):
        return self.grid[node[0], node[1]]['vision']