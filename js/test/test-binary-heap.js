'use strict';

let MaxHeap = require('../binary-heap');
let chai = require('chai');
let expect = chai.expect;

describe('Functions that test Priority class methods.', function() {

  it('Test heap property is an array.', function() {
    let maxheap = new MaxHeap();
    expect(maxheap.heap).to.be.an('array');
  });

  it('Test heap property is an empty array by default if no value given during creation.', function() {
    let maxheap = new MaxHeap();
    expect(maxheap.heap).to.deep.equal([]);
  });

  it('Test newly created MaxHeap has a heap property.', function() {
    let maxheap = new MaxHeap();
    expect(maxheap).to.have.own.property('heap');
  });

  it('Test iterable given to MaxHeap is sorted in descending order upon creation.', function() {
    let maxheap = new MaxHeap([1, 2, 3]);
    expect(maxheap.heap).to.deep.equal([3, 2, 1]);
  });

  it('Test iterable given to MaxHeap is not sorted in ascending order upon creation.', function() {
    let maxheap = new MaxHeap([1, 2, 3]);
    expect(maxheap.heap).to.not.deep.equal([1, 2, 3]);
  });

  it('Test push method of MaxHeap adds length to heap array.', function() {
    let maxheap = new MaxHeap();
    maxheap.push(1);
    expect(maxheap.heap.length).to.equal(1);
  });

  it('Test push method of MaxHeap adds given value to heap.', function() {
    let maxheap = new MaxHeap();
    maxheap.push(1);
    expect(maxheap.heap[0]).to.equal(1);
  });

  it('Test push method of MaxHeap adds length to heap array given multiple pushes.', function() {
    let maxheap = new MaxHeap();
    maxheap.push(1);
    maxheap.push(2);
    maxheap.push(3);
    expect(maxheap.heap.length).to.equal(3);
  });

  it('Test push method of MaxHeap maintains Max Heap order given multiple pushes.', function() {
    let maxheap = new MaxHeap();
    maxheap.push(1);
    maxheap.push(2);
    maxheap.push(3);
    expect(maxheap.heap).to.deep.equal([3, 1, 2]);
  });

  it('Test pop method of MaxHeap throws error if heap is empty.', function() {
    let maxheap = new MaxHeap();
    expect(maxheap.pop).to.throw(Error);
  });

  it('Test pop method of MaxHeap removes head of Max Heap.', function() {
    let maxheap = new MaxHeap([3, 2, 1]);
    expect(maxheap.pop()).to.equal(3);
  });

  it('Test pop method of MaxHeap shortens length of heap.', function() {
    let maxheap = new MaxHeap([3, 2, 1]);
    maxheap.pop();
    expect(maxheap.heap.length).to.equal(2);
  });

  it('Test pop method of MaxHeap maintains Max Heap order.', function() {
    let maxheap = new MaxHeap();
    maxheap.push(100);
    maxheap.push(10);
    maxheap.push(90);
    maxheap.push(30);
    maxheap.push(20);
    maxheap.push(95);
    maxheap.pop();
    expect(maxheap.heap).to.deep.equal([95, 90, 10, 20, 30]);
  });

  it('Test findChildren method of MaxHeap returns array.', function() {
    let maxheap = new MaxHeap([3, 2, 1]);
    expect(maxheap.findChildren(0)).to.be.an('array');
  });

  it('Test findChildren method of MaxHeap returns array containing two children values of given node index.', function() {
    let maxheap = new MaxHeap([3, 2, 1]);
    expect(maxheap.findChildren(0)).to.deep.equal([2, 1]);
  });

  it('Test findParent method of MaxHeap returns index of parent value in heap given child node index.', function() {
    let maxheap = new MaxHeap([3, 2, 1]);
    expect(maxheap.findParent(2)).to.equal(0);
  });

  it('Test bubbleUp method properly sorts last value up the heap and continuously switches with parent until parent is not less than value.', function() {
    let maxheap = new MaxHeap();
    maxheap.heap = [50, 20, 10, 25, 60];
    expect(maxheap.bubbleUp()).to.deep.equal([60, 50, 10, 25, 20]);
  });

  it('Test sortDown method properly sorts down the heap, continuously switching parent nodes with their biggest child until node has no children.', function() {
    let maxheap = new MaxHeap();
    maxheap.heap = [1, 2, 3, 4, 5];
    maxheap.sortDown();
    expect(maxheap.heap).to.deep.equal([3, 5, 1, 4, 2]);
  });

  it('Test that using sortDown and bubbleUp methods together fully sorts the heap, maintaining Max Heap properties.', function() {
    let maxheap = new MaxHeap();
    maxheap.heap = [1, 2, 3, 4, 5];
    maxheap.bubbleUp();
    maxheap.sortDown();
    expect(maxheap.heap).to.deep.equal([5, 4, 3, 1, 2]);
  });


});
