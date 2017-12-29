'use strict';

let Deque = require('../deque')
let chai = require('chai')
let expect = chai.expect

describe('Test for deque module.', function() {

  it('Test append method adds value to end of deque.', function(){
    let deque = new Deque()
    deque.append(10);
    deque.append(20);
    expect(deque.deque.tail.data).to.equal(20);
  });

  it('Test that append method does not change head if deque has head.', function() {
    let deque = new Deque();
    deque.append(10);
    deque.append(20);
    expect(deque.deque.head.data).to.equal(10);
  });

  it('Test that append method increases size of deque.', function() {
    let deque = new Deque();
    deque.append(10);
    deque.append(20);
    expect(deque.size()).to.equal(2);
  });

  it('Test appendLeft method adds value to front of deque.', function() {
    let deque = new Deque()
    deque.appendLeft(10);
    deque.appendLeft(20);
    expect(deque.deque.head.data).to.equal(20);
  });

  it('Test that appendLeft method does not change tail if deque has head.', function() {
    let deque = new Deque();
    deque.appendLeft(10);
    deque.appendLeft(20);
    expect(deque.deque.tail.data).to.equal(10);
  });

  it('Test that appendLeft method increases size of deque.', function() {
    let deque = new Deque();
    deque.appendLeft(10);
    deque.appendLeft(20);
    expect(deque.size()).to.equal(2);
  });

  it('Test pop method returns value of removed node.', function() {
    let deque = new Deque()
    deque.appendLeft(121);
    deque.append(232);
    expect(deque.pop()).to.equal(232);
  });

  it('Test pop method removes tail of deque.', function() {
    let deque = new Deque()
    deque.appendLeft(121);
    deque.append(232);
    expect(deque.pop()).to.equal(232);
  });

  it('Test pop method decreases size of deque.', function() {
    let deque = new Deque()
    deque.append(121);
    deque.append(232);
    deque.pop();
    expect(deque.size()).to.equal(1);
  });

  it('Test popLeft method returns value of removed node.', function() {
    let deque = new Deque()
    deque.appendLeft(121);
    deque.append(232);
    expect(deque.popLeft()).to.equal(121);
  });

  it('Test popLeft method removes head of deque.', function() {
    let deque = new Deque()
    deque.appendLeft(121);
    deque.append(232);
    expect(deque.popLeft()).to.equal(121);
  });

  it('Test popLeft method decreases size of deque.', function() {
    let deque = new Deque()
    deque.append(121);
    deque.append(232);
    deque.popLeft();
    expect(deque.size()).to.equal(1);
  });

  it('Test pop method throws error if deque is empty.', function() {
    let deque = new Deque();
    expect(deque.pop).to.throw(Error);
  });

  it('Test popLeft method throws error if deque is empty.', function() {
    let deque = new Deque();
    expect(deque.popLeft).to.throw(Error);
  });

  it('Test peek method returns value of deque tail.', function() {
    let deque = new Deque();
    deque.appendLeft(7);
    deque.append(5);
    expect(deque.peek()).to.equal(5);
  });

  it('Test peekLeft method returns value of deque head.', function() {
    let deque = new Deque();
    deque.appendLeft(7);
    deque.append(5);
    expect(deque.peekLeft()).to.equal(7);
  });

  it('Test peek method returns null if deque is empty.', function() {
    let deque = new Deque();
    expect(deque.peek()).to.be.null;
  });

  it('Test peekLeft method returns null if deque is empty.', function() {
    let deque = new Deque();
    expect(deque.peekLeft()).to.be.null;
  });

  it('Test size method of deque returns deque size.', function() {
    let deque = new Deque();
    deque.appendLeft(1);
    deque.appendLeft(2);
    deque.appendLeft(3);
    expect(deque.size()).to.equal(3);
  });

});
