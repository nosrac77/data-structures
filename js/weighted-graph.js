'use strict';

class WeightedGraph {
  constructor() {
    this.graph = {};
    this.weights = {};
  }

  nodes() {
    return Object.keys(this.graph);
  }

  edges() {
    let edgesList = [];
    for (var i = 0; i < Object.keys(this.weights).length; i++) {
      edgesList.push(Object.keys(this.weights)[i].split(''));
    }
    return edgesList;
  }

  addNode() {
    for (var i = 0; i < arguments.length; i++) {
      if (this.graph[arguments[i]]) {
        continue;
      } else {
        this.graph[arguments[i]] = [];
      }
    }
  }

  addEdge(val1, val2, weight) {
    this.addNode(val1);
    this.addNode(val2);
    this.graph[val1].push(val2);
    this.weights[val1 + val2] = weight;
  }

  delNode(data) {
    if (this.graph[data]) {
      delete this.graph[data];
    } else {
      throw new Error('Node not in Graph, yo. Chill.');
    }
    let edgesList = this.edges();
    for (var i = 0; i < edgesList.length; i++) {
      if (edgesList[i][0] == data || edgesList[i][1] == data) {
        var node1 = edgesList[i][0];
        var node2 = edgesList[i][1];
        delete this.weights[node1 + node2];
        return;
      }
    }
  }

  delEdge(val1, val2) {
    let edgesList = this.edges();
    for (var i = 0; i < edgesList.length; i++) {
      if (edgesList[i][0] == val1 && edgesList[i][1] == val2) {
        var node1 = edgesList[i][0];
        var node2 = edgesList[i][1];
        delete this.weights[node1 + node2];
        return;
      }
    }
    throw new Error('Cant delete what isnt there DUDE.');
  }

  hasNode(data) {
    return this.graph[data] ? true : false;
  }

  neighbors(data) {
    if (this.graph[data]) {
      return this.graph[data];
    } else {
      throw new Error('Nope.');
    }
  }

  adjacent(val1, val2) {
    if (this.weights[val1 + val2]) {
      return true;
    } else {
      throw new Error('No connection bro.');
    }
  }
}

// def breadth_first_traversal(self, val):
//       """Breadth first graph traversal."""
//       if val not in self.graph.keys():
//           raise KeyError
//       if self.graph[val] == []:
//           return [val]
//       return_list = [val]
//       for edges in return_list:
//           for edge in self.graph[edges]:
//               if edge not in return_list:
//                   return_list.append(edge)
//       return return_list
//
//   def depth_first_traversal(self, val):
//       """Depth first graph traversal."""
//       if val not in self.graph.keys():
//           raise KeyError
//       if self.graph[val] == []:
//           return [val]
//       return_list = []
//       other_list = [val]
//       while other_list:
//           node = other_list[0]
//           if node not in return_list:
//               return_list.append(node)
//               del other_list[0]
//               for edge in reversed(self.graph[node]):
//                   if edge not in return_list and edge not in other_list:
//                       other_list.insert(0, edge)
//       return return_list

module.exports = WeightedGraph
