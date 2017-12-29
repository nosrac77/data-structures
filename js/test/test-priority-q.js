'use strict';

let Pq = require('../priority-q');
let chai = require('chai');
let expect = chai.expect;

describe('Functions that test Priority class methods.', function() {

  it('Test newly created PQ has default values.', function() {
    let pq = new Pq();
    expect(pq.head).to.be.null;
    expect(pq.tail).to.be.null;
    expect(pq._counter).to.equal(0);
  });

  it('Test insert method adds value to Pq.', function() {
    let pq = new Pq();
    pq.insert(1);
    expect(pq.head.data).to.equal(1);
  });

  it('Test insert method adds value to back of Pq.', function() {
    let pq = new Pq();
    pq.insert(1);
    pq.insert(2);
    pq.insert(3);
    expect(pq.head.data).to.equal(1);
  });

  it('Test insert method adds value and priority to back of Pq.', function() {
    let pq = new Pq();
    pq.insert(1, 100);
    expect(pq.head.priority).to.equal(100);
  });

  it('Test insert method increases size of Pq.', function() {
    let pq = new Pq();
    pq.insert(1);
    expect(pq._counter).to.equal(1);
  });

  it('Test insert method throws error if priority lower zero.', function() {
    let pq = new Pq();
    expect(pq.insert).to.throw(Error);
  });

  it('Test pop method removes value from Pq.', function() {
    let pq = new Pq();
    pq.insert(1);
    expect(pq.pop()).to.equal(1);
  });

  it('Test pop method removes head of Pq.', function() {
    let pq = new Pq();
    pq.insert(1);
    pq.insert(2);
    pq.insert(3);
    expect(pq.pop()).to.equal(1);
  });

  it('Test pop method reduces size of Pq.', function() {
    let pq = new Pq();
    pq.insert(1);
    pq.insert(2);
    pq.insert(3);
    pq.pop();
    expect(pq._counter).to.equal(2);
  });

  it('Test pop method removes highest priority value in Pq.', function() {
    let pq = new Pq();
    pq.insert(1, 20);
    pq.insert(2, 40);
    pq.insert(3, 600);
    expect(pq.pop()).to.equal(3);
  });

  it('Test pop method throws error if Pq is empty.', function() {
    let pq = new Pq();
    expect(pq.pop).to.throw(Error);
  });

  it('Test peek method returns val of head if all values have same priority.', function() {
    let pq = new Pq();
    pq.insert(1);
    pq.insert(2);
    pq.insert(3);
    expect(pq.peek()).to.equal(1);
  });

  it('Test peek method returns highest priority value item in Pq.', function() {
    let pq = new Pq();
    pq.insert(1, 5);
    pq.insert(2, 10);
    pq.insert(3, 6000);
    expect(pq.peek()).to.equal(3);
  });

  it('Test peek method throws error if Pq is empty.', function() {
    let pq = new Pq();
    expect(pq.peek).to.throw(Error);
  });

});
