'use strict';

const linkedList = require('./linked-list');

class Stack {
  constructor(iterable=[]) {
    this.list = new linkedList.LinkedList();
    this._counter = this.list._counter;
    if(iterable.length > 0){
      iterable.forEach(x => this.push(x));
    }
  }

  push(val) {
    this.list.push(val);
  }

  pop() {
    if (this.list.size() === 0) {
      throw new Error('Cannot pop from an empty Stack.');
    } else {
      return this.list.pop();
    }
  }

  size() {
    return this.list.size();
  }
}

module.exports = Stack;
