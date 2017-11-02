"""Graph data structure."""


class G(object):
    """Class that creates instance of a graph."""

    def __init__(self):
        """Initialize Graph instance."""
        self.all_edges = []
        self.all_nodes = []

    def nodes(self):
        """Return a list of all nodes."""
        node_vals = []
        for node in self.all_nodes:
            node_vals.append(node.data)
        return node_vals

    def edges(self):
        """Return a list of all edges."""
        return self.all_edges

    def add_node(self, val):
        """Add new node to graph."""
        self.all_nodes.append(Node(val))

    def add_edge(self, val1, val2):
        """Add new node to graph."""
        if Node(val1) not in self.all_nodes:
            self.add_node(val1)
        if Node(val2) not in self.all_nodes:
            self.add_node(val2)
        for edge in self.all_edges:
            if edge == (val1, val2):
                edge = (val1, val2)
        self.all_edges.append((val1, val2))

    def del_node(self, val):
        """Remove given node from graph."""
        for node in self.all_nodes:
            if node.data == val:
                self.all_nodes.remove(node)
                for edge in self.all_edges:
                    if val in edge:
                        self.del_edge(edge[0], edge[1])
                break
        else:
            raise IndexError('This node is not in the graph.')

    def del_edge(self, val1, val2):
        """Remove given edge from graph."""
        if (val1, val2) in self.all_edges:
            self.all_edges.remove((val1, val2))
        else:
            raise IndexError('This edge is not in the graph.')

    def has_node(self, val):
        """Return Boolean: is "val" node in graph."""
        return Node(val) in self.all_nodes

    def neighbors(self, val):
        """Return list of all nodes connection to val by edges."""
        nodeborhood = []
        if val not in self.nodes():
            raise IndexError('Node not in the graph.')
        for edge in self.all_edges:
            if edge[0] == val:
                nodeborhood.append(edge[1])
        return nodeborhood

    def adjacent(self, val1, val2):
        """Return whether val1 and val2 have a connecting edge."""
        if Node(val1) not in self.all_nodes or Node(val2) not in self.all_nodes:
            return False
        for edge in self.all_edges:
            if edge == (val1, val2) or edge == (val2, val1):
                return True
        return False


class Node(object):
    """Graph Node class."""

    def __init__(self, val):
        """Initialize Node class instance for Graph."""
        self.data = val

if __name__ == '__main__':
    g = G()
