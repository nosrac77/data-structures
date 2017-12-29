'use strict';

let DoublyLinked = require('./doubly-linked')

class Deque {
  constructor() {
    this.deque = new DoublyLinked();
  }

  append(val) {
    this.deque.append(val);
  }

  appendLeft(val) {
    this.deque.push(val);
  }

  pop() {
    if (this.deque._counter == 0) {
      throw new Error('Cannot pop from empty deque.');
    }
    return this.deque.shift();
  }

  popLeft() {
    if (this.deque._counter == 0) {
      throw new Error('Cannot pop from empty deque.');
    }
    return this.deque.pop();
  }

  peek() {
    if(this.deque._counter == 0){
      return null;
    }
    return this.deque.tail.data;
  }

  peekLeft(){
    if (this.deque._counter == 0) {
      return null;
    }
    return this.deque.head.data;
  }

  size() {
    return this.deque._counter;
  }
}

module.exports = Deque