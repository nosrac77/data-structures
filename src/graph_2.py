"""Graph data structure."""


class G(object):
    """Class that creates instance of a graph."""

    def __init__(self):
        """Init graph instance."""
        self.graph = {}

    def nodes(self):
        """Return a list of all nodes."""
        return list(self.graph.keys())

    def edges(self):
        """Return a list of tuples showing the relations."""
        edges = []
        for key, vals in self.graph.items():
            for val in vals:
                edges.append((key, val))
        return edges

    def add_node(self, *args):
        """Add a new node or nodes."""
        for data in args:
            self.graph.setdefault(data, [])

    def add_edge(self, val1, val2):
        """Add a new edge between 2 nodes."""
        self.add_node(val1, val2)
        edge_head = self.graph[val1]
        edge_head.append(val2)

    def del_node(self, data):
        """Delete a node in the graph."""
        if data in self.nodes():
            del self.graph[data]
            for key in self.graph:
                if data in self.graph[key]:
                    self.graph[key].remove(data)
        else:
            raise IndexError('Node not in graph.')

    def del_edge(self, val1, val2):
        """Delete an edge."""
        for connected_edge in self.graph[val1]:
            if val2 == connected_edge:
                return self.graph[val1].remove(connected_edge)
        raise KeyError('Edge not in graph.')

    def has_node(self, data):
        """Check if a node is in graph."""
        return data in self.graph

    def neighbors(self, data):
        """Return all the nodes the data is pointing to."""
        if data in self.graph:
            return self.graph[data]
        IndexError('Node not in graph.')

    def adjacent(self, val1, val2):
        """Return if val1 and val2 have connecting edge."""
        if val1 not in self.nodes() or val2 not in self.nodes():
            raise IndexError('Node not in graph.')
        return val1 in self.graph[val2] or val2 in self.graph[val1]

    def breadth_first_traversal(self, val):
        """."""
        if val not in self.graph:
            return [val]
        node_edges = {}
        node_edges.append(self.graph[val])
