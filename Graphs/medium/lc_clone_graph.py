
# https://leetcode.com/problems/clone-graph/
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        new = {}
        visited = {}

        q = deque()
        q.appendleft(node)

        while q:
            n = q.pop()

            if n.val not in visited:
                visited[n.val] = True

                if n.val not in new:
                    new[n.val] = Node(n.val)

                for nb in n.neighbors:
                    if nb.val not in new:
                        new[nb.val] = Node(nb.val)
                    new[n.val].neighbors.append(new[nb.val])
                    q.appendleft(nb)

        return new[node.val]

# Runtime: BFS visits all node and edges at least once O(N + E) where N is the number of nodes and E the number of Edges
# (For each node n check all possible neighbors e)
# Space: O(N) for visited and O(W) for the queue where w is the 'width' of the graph, so O(N) overall as N >= W


# Note: Problem can be solved via DFS also but we need a visited aslo to prevent going in cycles :)

class DfsSolution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited = {}

        def dfs(node):
            # Base Case 1:
            if not node:
                return node

            # Base Case 2:
            # This is the crucial part to prevent infinite recursion in case of cycles
            # We have cloned the node already, return it
            if node in visited:
                return visited[node]

            # Recursive Case (No clone yet)
            clone_node = Node(node.val, [])
            visited[node] = clone_node

            if node.neighbors:
                for n in node.neighbors:
                    # trust that the recursion works and returns the clone of a node
                    clone_node.neighbors.append(dfs(n))

            return clone_node

        return dfs(node)


# Runtime: DFS visits all node and edges at least once O(N + E) where N is the number of nodes and E the number of Edges
# (For each node n check all possible neighbors e)
# Space: O(N) for visited and O(H) where h is the 'height' of the graph for the recursion stack, so O(N) overall as N >= H
