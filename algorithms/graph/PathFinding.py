""" PATHFIDING MODULE
# Description:
    This is python(3.6) implementation of A* pathfiding algorithm.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/05/25
# Reference:
    * http://theory.stanford.edu/~amitp/GameProgramming
    * https://en.wikipedia.org/wiki/A*_search_algorithm
    * https://www.youtube.com/watch?v=KNXfSOx4eEE
"""
from queue import PriorityQueue

class PathFinding():
    
    def __init__(self, graph, algorithm='a-star'):
        """ Path Finder
        Parameters
        ----------
        graph: GridMap
            The graph object with movement cost and neighbor functions.
        algorithm: string, optional
            The algorithm to find the path from start to goal.
        """
        self.graph = graph
        self.algorithm = algorithm

    def get_path(self, start, goal):
        """ Get Path List
        Parameters
        ----------
        start: tuple
            The starting vertice on the grid map.
        goal: tuple
            The targeting vertice on the grid map. 
        """
        if self.algorithm == 'a-star':
            return self.__a_star_algorithm(start, goal)
        else:
            raise ValueError('- algorithm not supported -')

    def __heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)
    
    def __a_star_algorithm(self, start, goal):
        start = tuple(start)
        goal = tuple(goal)
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()
            
            if current == goal:
                return self.__reconstruct_path(came_from, start, goal)
            
            for next_ in self.graph.neighbors(current):
                new_cost = cost_so_far[current] + self.graph.getCost(current, next_)
                if next_ not in cost_so_far or new_cost < cost_so_far[next_]:
                    cost_so_far[next_] = new_cost
                    priority = new_cost + self.__heuristic(goal, next_)
                    frontier.put(next_, priority)
                    came_from[next_] = current                         
        # Return None when there is no path                         
        return None
    
    def __reconstruct_path(self, came_from, start, goal):
        start = tuple(start)
        goal = tuple(goal)
        
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
    #    path.append(start) # optional
        path.reverse() # optional
        return path