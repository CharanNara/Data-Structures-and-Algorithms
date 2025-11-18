"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # given first node 1
        # we need to traverse the graph from 1 to end using DFS or BFS
        # if we do dfs -> then we keep creating copies every time we visit new node and make sure to connect the new copies
        visited = {}
        
        def dfs(root):
            # if none return none
            if root is None:
                return None

            # #if already visited return new copy
            # if root in visited:
            #     return visited[root]
            # create new copy
            new_copy = Node(root.val)
            visited[root] = new_copy

            for nei in root.neighbors:
                if nei not in visited:
                    new_copy.neighbors.append(dfs(nei))
                else:
                    new_copy.neighbors.append(visited[nei])

            return new_copy
        
        return dfs(node)


"""
Given a reference of node and we need to make a deep copy and return that new graph
a copy means - the instance of the node should be new also the neighbor instances should be new with new connections
It's like creating an exact copy of graph and the node copies position stay the same


Alright,
Given neighbor list -> [[2,4],[1,3],[2,4],[1,3]]
                 node     1      2     3     4

            
for 1 -> neighbors are 2,4
for 2 -> neighbors are 1,3
for 3 -> neighbors are 2,4
for 4 -> neighbors are 1,3


1 - 2
|   |
4 - 3

create new copies of 1, 2, 3, 4

and maintain the same neighbors

"""