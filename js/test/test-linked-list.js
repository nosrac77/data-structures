'use strict';

let linkedList = require('../linked-list');
let chai = require('chai');
let expect = chai.expect;

describe('Functions to test Linked List.', function() {

  it('Tests new node correctly takes in given values and maintains default values.', function() {
    let testNode = new linkedList.Node(5);
    expect(testNode.data).to.equal(5);
    expect(testNode.next).to.equal(null);
  });

  it('Tests linked list can take iterable upon init.', function() {
    let testList = new linkedList.LinkedList([1, 2, 3, 4, 5]);
    expect(testList.size()).to.equal(5);
  })

  it('Test if push method adds new item to linked list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    expect(testList.head.data).to.equal(1);
  });

  it('Test if push method adds new item head, retains last head.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    testList.push(2);
    expect(testList.head.data).to.equal(2);
    expect(testList.head.next.data).to.equal(1);
  });

  it('Test if push increases size of Linked List.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    expect(testList.size()).to.equal(1);
  });

  it('Tests if pop method returns the removed value.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    expect(testList.pop()).to.equal(1);
  });

  it('Tests if pop method resets head if val given is head val.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(2);
    testList.push(1);
    testList.pop();
    expect(testList.head.data).to.equal(2);
  });

  it('Tests if pop method throws error if list is empty.', function() {
    let testList = new linkedList.LinkedList();
    expect(testList.pop).to.throw(Error);
  });

  it('Tests if size method returns correct size of linked list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    testList.push(10);
    testList.push(100);
    expect(testList.size()).to.equal(3);
  });

  it('Tests search method throws error if node containing val not in list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    expect(testList.search).to.throw(Error);
  });

  it('Tests search method returns Node if in linked list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    testList.push(2);
    testList.push(3);
    expect(testList.search(1)).to.be.an.instanceof(linkedList.Node);
  });

  it('Tests remove method throws error if list is empty.', function() {
    let testList = new linkedList.LinkedList();
    expect(testList.remove).to.throw(Error);
  });

  it('Tests remove method throws error if val not in list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1)
    expect(testList.remove).to.throw(Error);
  });

  it('Tests remove method resets head if removing head node.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(15);
    testList.push(30);
    testList.remove(30);
    expect(testList.head.data).to.equal(15);
  });

  it('Tests remove method removes correct node from list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    testList.push(2);
    testList.remove(1);
    expect(testList.head.next).to.be.null;
  });

  it('Tests remove method reduces size of list.', function() {
    let testList = new linkedList.LinkedList();
    testList.push(1);
    testList.push(2);
    testList.remove(1);
    expect(testList.size()).to.equal(1);
  });

  it('Tests display method correctly displays linked list.', function() {
    let testList = new linkedList.LinkedList();
    for (var i = 1; i < 6; i++) {testList.push(i);}
    expect(testList.display()).to.be.string('5, 4, 3, 2, 1');
  });

});
