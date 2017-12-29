'use strict';

class DoublyLinked {
  constructor() {
    this._counter = 0
    this.head = null
    this.tail = null
  }

  push(val) {
    let newNode = new Node(val);
    this._counter ++;
    if (this.head === null) {
      this.head = newNode;
      this.tail = this.head
    } else {
      this.head.prevNode = newNode;
      newNode.nextNode = this.head;
      this.head = newNode;
    }
  }

  pop() {
    if (this._counter == 0) {
      throw new Error('Cannot pop from an empty list.');
    }
    let output = this.head.data;
    if (this.head.nextNode === null) {
      this.tail = null;
      this.head = null;
      this._counter --;
      return output;
    } else if (this.head.nextNode.nextNode === null) {
      this.head.nextNode = null;
      this.tail.prevNode = null;
      this.head = this.tail;
      this.tail = this.head;
      this._counter --;
      return output;
    }
    this.head = this.head.nextNode
    if (this.head) {
      this.head.prevNode = null;
    }
    this._counter --;
    return output;
  }

  remove(val) {
    if (!this.head) {
      throw new Error('Input value not in Doubly Linked List.');
    }
    if (this.head.data == val) {
      return this.pop();
    }
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.data == val) {
        if (currentNode === this.tail) {
          this.tail = this.tail.prevNode;
          this.tail.nextNode.prevNode = null;
          this.tail.nextNode = null;
          this._counter --;
          return val;
        }
        currentNode.prevNode.nextNode = currentNode.nextNode;
        currentNode.nextNode.prevNode = currentNode.prevNode;
        this._counter --;
        return val;
      }
      if (currentNode.nextNode === null) {
        throw new Error('Input value not in Doubly Linked List.');
      }
      currentNode = currentNode.nextNode;
    }
  }

  shift() {
    if (this._counter == 0) {
      throw new Error('Cannot shift on empty list.');
    }
    if (this._counter == 1) {
      return this.pop()
    }
    let output = this.tail.data;
    this.tail = this.tail.prevNode;
    this.tail.nextNode.prevNode = null;
    this.tail.nextNode = null;
    this._counter --;
    return output;
  }

  append(val) {
    if (!this.head) {
      this.push(val);
      return
    }
    let currentNode = new Node(val, null, this.tail);
    this.tail.nextNode = currentNode;
    this.tail = currentNode;
    this._counter ++;
  }
}

class Node {
  constructor(data, nextNode=null, prevNode=null) {
    this.data = data
    this.nextNode = nextNode;
    this.prevNode = prevNode
  }
}

module.exports = DoublyLinked;
