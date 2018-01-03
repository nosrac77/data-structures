'use strict';

let WeightedGraph = require('../weighted-graph');
let chai = require('chai');
let expect = chai.expect;

describe('Functions that test WeightedGraph class methods.', function() {

  it('Test graph property is an object.', function() {
    let graph = new WeightedGraph();
    expect(graph.graph).to.be.an('object');
  });

  it('Test weights property is an object.', function() {
    let graph = new WeightedGraph();
    expect(graph.weights).to.be.an('object');
  });

  it('Test addNode method of WeightedGraph assigns value of empty array to new node in graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a');
    expect(graph.graph.a).to.be.an('array');
  });

  it('Test addNode method of WeightedGraph adds node value to graph as key in graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a');
    expect(Object.keys(graph.graph)).to.deep.equal([ 'a' ]);
  });

  it('Test addNode method of WeightedGraph does not add node value to graph as key in graph if given value is already in graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a');
    graph.addNode('a');
    expect(Object.keys(graph.graph)).to.deep.equal([ 'a' ]);
  });

  it('Test addNode method of WeightedGraph adds multiple values to graph as keys in graph if given multiple arguments.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a', 'b', 'c');
    expect(Object.keys(graph.graph)).to.deep.equal([ 'a', 'b', 'c' ]);
  });

  it('Test addNode method of WeightedGraph does not add multiple values to graph as keys in graph if given multiple same arguments.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a', 'a', 'a');
    expect(Object.keys(graph.graph)).to.deep.equal([ 'a' ]);
  });

  it('Test addEdge method of WeightedGraph adds first value as key in graph and second value as item in first value array in graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(Object.keys(graph.graph)[0]).to.equal('a');
    expect(graph.graph.a).to.deep.equal([ 'b' ]);
  });

  it('Test addEdge method of WeightedGraph adds given values as keys in graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(Object.keys(graph.graph)).to.deep.equal([ 'a', 'b' ]);
  });

  it('Test addEdge method of WeightedGraph does not add first value as item in second value array in graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(Object.keys(graph.graph.b)).to.not.equal('a');
  });

  it('Test addEdge method of WeightedGraph adds empty array for second value in graph object.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(Object.keys(graph.graph.b)).to.be.an('array');
  });

  it('Test nodes method of WeightedGraph returns array representation of nodes in graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a', 'b', 'c');
    expect(graph.nodes()).to.deep.equal([ 'a', 'b', 'c' ]);
  });

  it('Test nodes method of WeightedGraph returns empty array if no nodes in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.nodes()).to.deep.equal([]);
  });

  it('Test nodes method of WeightedGraph returns array representation of nodes in graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a');
    expect(graph.nodes()).to.be.an('array');
  });

  it('Test edges method of WeightedGraph returns array containing other arrays as a representation of the edges in the graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(graph.edges()).to.deep.equal([ ['a', 'b'] ]);
  });

  it('Test edges method of WeightedGraph returns empty array if no edges in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.edges()).to.deep.equal([]);
  });

  it('Test edges method of WeightedGraph returns array representation of edges in graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(graph.edges()).to.be.an('array');
  });

  it('Test delNode method of WeightedGraph deletes node with given value from graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a');
    expect(graph.nodes()).to.deep.equal([ 'a' ]);
    graph.delNode('a');
    expect(graph.nodes()).to.deep.equal([]);
  });

  it('Test delNode method of WeightedGraph deletes edges tied to node with given value from graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(graph.edges()).to.deep.equal([ [ 'a', 'b' ] ]);
    graph.delNode('a');
    expect(graph.edges()).to.deep.equal([]);
  });

  it('Test delNode method of WeightedGraph throws error if given value not in any node in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.delNode.bind(graph, 'a')).to.throw('Node not in Graph, yo. Chill.');
  });

  it('Test delEdge method of WeightedGraph deletes edge of two given node values.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(graph.edges()).to.deep.equal([ [ 'a', 'b' ] ]);
    graph.delEdge('a', 'b');
    expect(graph.edges()).to.deep.equal([]);
  });

  it('Test delEdge method of WeightedGraph does not delete nodes from graph, only their edges.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(graph.nodes()).to.deep.equal([ 'a', 'b' ]);
    graph.delEdge('a', 'b');
    expect(graph.nodes()).to.deep.equal([ 'a', 'b' ]);
  });

  it('Test delEdge method of WeightedGraph throws error if given edge not in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.delEdge.bind(graph, ('a', 'b'))).to.throw('Cant delete what isnt there DUDE.');
  });

  it('Test hasNode method of WeightedGraph returns true if node containing given value is in graph.', function() {
    let graph = new WeightedGraph();
    graph.addNode('a');
    expect(graph.hasNode('a')).to.equal(true);
  });

  it('Test hasNode method of WeightedGraph returns false if node containing given value is not in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.hasNode('a')).to.equal(false);
  });

  it('Test neighbors method of WeightedGraph returns array of all nodes connected to node with given value.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    graph.addEdge('a', 'c');
    graph.addEdge('a', 'd');
    expect(graph.neighbors('a')).to.deep.equal([ 'b', 'c', 'd' ]);
  });

  it('Test neighbors method of WeightedGraph throws error if node containing given value not in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.neighbors.bind(graph, 'a')).to.throw('Nope.');
  });

  it('Test adjacent method of WeightedGraph returns true if edge with given values in graph.', function() {
    let graph = new WeightedGraph();
    graph.addEdge('a', 'b');
    expect(graph.adjacent('a', 'b')).to.equal(true);
  });

  it('Test adjacent method of WeightedGraph throws error if edge with given values not in graph.', function() {
    let graph = new WeightedGraph();
    expect(graph.adjacent.bind(graph, ('a', 'b'))).to.throw('No connection bro.');
  });

});
