"""Graph data structure."""


class G(object):
    """Class that creates instance of doubly linked list."""

    def __init__(self):
        """Initialize Graph instance."""
        self.all_edges = []
        self.all_nodes = []
        self.graph_dict = {}


    def nodes(self):
        """Returns a list of all nodes."""
        return all_nodes


     def edges(self):
        """Returns a list of all edges."""
        return all_edges


    def add_node(self, val):
        """Add new node to graph."""
        all_nodes.push(val)
        

    def add_edge(self, val1, val2):
        """Add new node to graph."""
        if val1 not in all_nodes:
            self.all_nodes.add_node(val1)
        if val2 not in all_nodes:
            self.all_nodes.add_node(val2)
        for edge in range(len(all_edges) - 1):
            if all_edges[edge] == (val1, val2):
                self.all_edges[edge] = (val1, val2)


    def del_node(self, val):
        """Remove given node from graph."""
       pass


    def del_edge(self, val):
        """Remove given edge from graph."""
       pass


    def has_node(self, val):
        """Return Boolean: is "val" node in graph."""
        pass

    def neighbors(self, val):
        """Return list of all nodes connection to val by edges."""
        pass

    def adjacent(self, val1, val2):
        """Return whether val1 and val2 have a connecting edge."""
        pass


class Node(object):
    """Graph Node class."""

    def __init__(self, val):
        """Initialize Node class instance for Graph."""
        self.data = val

if __name__ == '__main__':
    g = G()
