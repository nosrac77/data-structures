'use strict';

let Q = require('../queue');
let chai = require('chai');
let expect = chai.expect;

describe('Tests for queue data structure.', function() {

  it('Test that enqueue method adds value.', function() {
    let que = new Q();
    que.enqueue(10);
    expect(que.que.head.data).to.equal(10);
  });

  it('Test that enqueue method does not change head if que has head.', function() {
    let que = new Q();
    que.enqueue(10);
    que.enqueue(20);
    expect(que.que.head.data).to.equal(10);
  });

  it('Test that enqueue method resets tail.', function() {
    let que = new Q();
    que.enqueue(10);
    que.enqueue(20);
    expect(que.que.tail.data).to.equal(20);
    que.enqueue(30);
    expect(que.que.tail.data).to.equal(30);
  });

  it('Test that enqueue method increases size of que.', function() {
    let que = new Q();
    que.enqueue(10);
    que.enqueue(20);
    que.enqueue(30);
    expect(que.size()).to.equal(3);
  });

  it('Test dequeue method returns value of removed node.', function() {
    let que = new Q();
    que.enqueue(3);
    expect(que.dequeue()).to.equal(3);
  });

  it('Test dequeue method removes from head of que.', function() {
    let que = new Q();
    que.enqueue(10);
    que.enqueue(20);
    expect(que.dequeue()).to.equal(10);
  });

  it('Test dequeue method removes from head of que.', function() {
    let que = new Q();
    que.enqueue(10);
    que.enqueue(20);
    que.dequeue();
    expect(que.size()).to.equal(1);
  });

  it('Test dequeue method returns null if que is empty.', function() {
    let que = new Q();
    expect(que.dequeue()).to.be.null;
  });

  it('Test peek method only returns head node val.', function() {
    let que = new Q();
    que.enqueue(111);
    que.enqueue(333);
    expect(que.peek()).to.equal(111);
    que.enqueue(555);
    expect(que.peek()).to.equal(111);
  });

  it('Test peek method returns head node val.', function() {
    let que = new Q();
    que.enqueue(111);
    expect(que.peek()).to.equal(111);
  });

  it('Test peek method returns null when que is empty.', function() {
    let que = new Q()
    expect(que.peek()).to.be.null;
  });

  it('Test size method returns total size of que.', function(){
    let que = new Q()
    que.enqueue(1);
    que.enqueue(2);
    que.enqueue(3);
    expect(que.size()).to.equal(3);
  });

});
