'use strict';

let Stack = require('../stack');
let chai = require('chai');
let expect = chai.expect;

describe('Functions that test JS Stack implementation.', function() {

  it('Test if push method adds new item to stack.', function() {
    let stack = new Stack();
    stack.push(1);
    expect(stack.list.head.data).to.equal(1);
  });

  it('Test if push method adds size to stack.', function() {
    let stack = new Stack();
    stack.push(500);
    expect(stack.list.size()).to.equal(1);
  });

  it('Test if push method resets head.', function() {
    let stack = new Stack();
    stack.push(10);
    expect(stack.list.head.data).to.equal(10);
    stack.push(20);
    stack.push(30);
    expect(stack.list.head.data).to.equal(30);
  });

  it('Test if pop method reduces size of stack.', function() {
    let stack = new Stack();
    stack.push(500);
    expect(stack.list.size()).to.equal(1);
    stack.pop()
    expect(stack.list.size()).to.equal(0);
  });

  it('Test if pop method removes head of stack and resets head to next value in stack.', function() {
    let stack = new Stack();
    stack.push(5);
    stack.push(10);
    stack.pop();
    expect(stack.list.head.data).to.equal(5);
  });

  it('Test if pop method returns value of removed node.', function() {
    let stack = new Stack();
    stack.push(5);
    expect(stack.pop()).to.equal(5);
  });

  it('Test if pop method throws error if stack is empty.', function() {
    let stack = new Stack();
    expect(stack.pop()).to.equal('Cannot pop from an empty Stack.');
  });

  it('Test if size method returns size of stack.', function() {
    let stack = new Stack();
    expect(stack.size()).to.equal(0);
  });
});
