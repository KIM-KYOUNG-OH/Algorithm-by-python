class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:    return node
        deq = deque([node])
        nodes = {node.val: Node(node.val)}

        while deq:
            poped = deq.popleft()
            cur = nodes[poped.val]

            for neigh in poped.neighbors:
                if neigh.val not in nodes:
                    nodes[neigh.val] = Node(neigh.val)
                    deq.append(neigh)

                cur.neighbors.append(nodes[neigh.val])

        return nodes[node.val]