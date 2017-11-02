"""Graph data structure."""


class G(object):
    """Class that creates instance of doubly linked list."""

    def __init__(self):
        """Initialize Graph instance."""
        self.all_edges = []
        self.all_nodes = []


    def nodes(self):
        """Returns a list of all nodes."""
        return self.all_nodes


     def edges(self):
        """Returns a list of all edges."""
        return self.all_edges


    def add_node(self, val):
        """Add new node to graph."""
        self.all_nodes.push(Node(val))
        

    def add_edge(self, val1, val2):
        """Add new node to graph."""
        if val1 not in self.all_nodes:
            self.all_nodes.add_node(val1)
        if val2 not in self.all_nodes:
            self.all_nodes.add_node(val2)
        for edge in range(len(self.all_edges) - 1):
            if self.all_edges[edge] == (val1, val2):
                self.all_edges[edge] = (val1, val2)


    def del_node(self, val):
        """Remove given node from graph."""
        if val in self.all_nodes:
            self.all_nodes.remove(val)
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
        pass

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
