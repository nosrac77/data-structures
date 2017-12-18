'use strict';

const linkedList = require('./linked-list');

class Stack {
  constructor(iterable=[]) {
    this.list = new linkedList.LinkedList();
    this.list._counter = 0
    if(iterable.length > 0){
      iterable.forEach(x => this.push(x));
    }
  }

  push(val) {
    this.linked.push(val);
  }

  pop() {
    if (this.list.size() === 0) {
      throw 'Cannot pop from an empty Stack.'
    } else {
      return this.list.pop();
    }
  }

  size() {
    return this.linked.size();
  }
}

module.exports = Stack;
