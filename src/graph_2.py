"""Graph data structure."""


class G(object):
    """Class that creates instance of a graph."""

    def __init__(self):
        """Init graph instance."""
        self.graph = {}
        self.weights = {}

    def nodes(self):
        """Return a list of all nodes."""
        return list(self.graph.keys())

    def edges(self):
        """Return a list of tuples showing the relations."""
        return list(self.weights.keys())

    def add_node(self, *args):
        """Add a new node or nodes."""
        for data in args:
            self.graph.setdefault(data, [])

    def add_edge(self, val1, val2, weight):
        """Add a new edge between 2 nodes."""
        self.add_node(val1, val2)
        edge_head = self.graph[val1]
        edge_head.append(val2)
        self.weights[(val1, val2)] = weight

    def del_node(self, data):
        """Delete a node in the graph."""
        if data in self.nodes():
            del self.graph[data]
            to_delete = []
            for key in self.weights.keys():
                if key[0] == data or key[1] == data:
                    to_delete.append(key)
            del self.weights[to_delete]
            for key in self.graph:
                if data in self.graph[key]:
                    self.graph[key].remove(data)
        else:
            raise KeyError('Node not in graph.')

    def del_edge(self, val1, val2):
        """Delete an edge."""
        for connected_edge in self.graph[val1]:
            if val2 == connected_edge:
                del self.weight[(val1, val2)]
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
        """Breadth first graph traversal."""
        if val not in self.graph.keys():
            raise KeyError
        if self.graph[val] == []:
            return [val]
        return_list = [val]
        for edges in return_list:
            return_list.extend(self.graph[edges])
        return return_list

    def depth_first_traversal(self, val):
        """Depth first graph traversal."""
        if self.graph[val] == []:
            return [val]
        return_list = []
        other_list = [val]
        while other_list:
            node = other_list[0]
            if node not in return_list:
                return_list.append(node)
                del other_list[0]
                for edge in reversed(self.graph[node]):
                    if edge not in return_list and edge not in other_list:
                        other_list.insert(0, edge)
        return return_list
