'use strict';

let DoublyLinked = require('../doubly-linked');
let chai = require('chai');
let expect = chai.expect;

describe('Functions that test DoublyLinked class methods.', function() {

  it('Test newly created DoublyLinked has null values for head and tail.', function() {
    let dll = new DoublyLinked();
    expect(dll.head.data).to.be.null;
    expect(dll.tail.data).to.be.null;
  });

  it('Test push method on empty DLL resets head to new node.', function() {
    let dll = new DoublyLinked();
    dll.push(5);
    expect(dll.head.data).to.equal(5);
  });

  it('Test push method on empty DLL resets tail to new node.', function() {
    let dll = new DoublyLinked();
    dll.push(5);
    expect(dll.tail.data).to.equal(5);
  });

  it('Test push method with two pushes resets head and tail.', function() {
    let dll = new DoublyLinked();
    dll.push(111);
    dll.push(999);
    expect(dll.head.data).to.equal(999);
    expect(dll.tail.data).to.equal(111);
  });

  it('Test push method properly assigns prevNode pointer.', function() {
    let dll = new DoublyLinked();
    dll.push(111);
    dll.push(999);
    expect(dll.tail.prevNode).to.equal(999);
  });

  it('Test push method properly assigns nextNode pointer.', function() {
    let dll = new DoublyLinked();
    dll.push(111);
    dll.push(999);
    expect(dll.head.nextNode).to.equal(111);
  });

  it('Test pop method removes head of DLL.', function() {
    let dll = new DoublyLinked();
    dll.push(10);
    dll.pop();
    expect(dll.head).to.be.null;
  });

  it('Test pop method returns value of popped node.', function() {
    let dll = new DoublyLinked();
    dll.push(10);
    expect(dll.pop()).to.equal(10);
  });

  it('Test pop method reduces size of DLL.', function() {
    let dll = new DoublyLinked();
    dll.push(10);
    dll.push(40);
    dll.push(50);
    dll.pop();
    expect(dll.size()).to.equal(2);
  });

  it('Test pop method resets head pointer.', function() {
    let dll = new DoublyLinked();
    dll.push(999);
    dll.push(111);
    expect(dll.head.data).to.equal(111);
    dll.pop()
    expect(dll.head.data).to.equal(999);
  });

  it('Test pop method throws error if list is empty.', function() {
    let dll = new DoublyLinked();
    expect(dll.pop).to.throw('Cannot pop from an empty list.');
  });

  it('Test remove method throws error if list empty.', function() {
    let dll = new DoublyLinked();
    expect(dll.remove(10)).to.throw('Input value not in Doubly Linked List.');
  });

  it('Test remove method throws error if given value not in list.', function() {
    let dll = new DoublyLinked();
    dll.push(500);
    dll.push(1000);
    expect(dll.remove(9)).to.throw('Input value not in Doubly Linked List.');
  });

  it('Test remove method reduces size of list.', function() {
    let dll = new DoublyLinked();
    dll.push(500);
    dll.remove(500);
    expect(dll._counter).to.equal(0);
  });

  it('Test remove method resets prevNode and nextNode pointers.', function() {
    let dll = new DoublyLinked();
    dll.push(101);
    dll.push(202);
    dll.push(303);
    dll.remove(202);
    expect(dll.head.nextNode.data).to.equal(303);
    expect(dll.tail.prevNode.data).to.equal(101);
  });

  it('Test shift method returns value in tail of list.', function() {
    let dll = new DoublyLinked();
    dll.push(101);
    dll.push(909);
    expect(dll.shift()).to.equal(909);
  });

  it('Test shift method removes tail of list.', function() {
    let dll = new DoublyLinked();
    dll.push(101);
    expect(dll.tail.data).to.equal(101);
    dll.shift();
    expect(dll.tail).to.be.null;
  });

  it('Test shift method removes head of list if list size is 1.', function() {
    let dll = new DoublyLinked();
    dll.push(101);
    expect(dll.head.data).to.equal(101);
    dll.shift();
    expect(dll.head).to.be.null;
  });

  it('Test shift method throws error if list is empty.', function() {
    let dll = new DoublyLinked()
    expect(dll.shift()).to.throw('Cannot shift on empty list.');
  });

  it('Test shift method reduces list size.', function() {
    let dll = new DoublyLinked();
    dll.push(101);
    dll.shift();
    expect(dll._counter).to.equal(0);
  });

  it('Test append method resets tail of list.', function() {
    let dll = new DoublyLinked();
    dll.push(1);
    dll.push(2);
    expect(dll.tail.data).to.equal(2);
    dll.append(3);
    expect(dll.tail.data).to.equal(3);
  });

  it('Test append method increases list size.', function() {
    let dll = new DoublyLinked();
    dll.push(1);
    dll.append(2);
    expect(dll._counter).to.equal(2);
  });

});
