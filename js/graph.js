'use strict';

class Graph {
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

  addEdge(val1, val2) {
    this.addNode(val1);
    this.addNode(val2);
    this.graph[val1].push(val2);
    this.weights[val1 + val2] = 'weight';
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

module.exports = Graph
