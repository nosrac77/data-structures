'use strict';

let DoublyLinked = require('./doubly-linked');

class Queue {
  constructor() {
    this.que = new DoublyLinked();
  }

  enqueue(val) {
    this.que.append(val);
  }

  dequeue() {
    if (this.que._counter == 0) {
      return null;
    }
    return this.que.pop();
  }

  peek() {
    if (this.que._counter == 0) {
      return null;
    }
    return this.que.head.data;
  }

  size() {
    return this.que._counter;
  }
}

module.exports = Queue;
