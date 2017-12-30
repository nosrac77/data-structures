'use strict';

let Graph = require('../graph');
let chai = require('chai');
let expect = chai.expect;

describe('Functions that test Graph class methods.', function() {

  it('Test graph property is an object.', function() {
    let graph = new Graph();
    expect(graph.graph).to.be.an('object');
  });

  it('Test weights property is an object.', function() {
    let graph = new Graph();
    expect(graph.weights).to.be.an('object');
  });

  it('Test addNode method of Graph adds given value to graph object.', function() {
    let graph = new Graph();
    graph.addNode('a');
    expect(graph.graph.a).to.be.an('array');
  });

});
