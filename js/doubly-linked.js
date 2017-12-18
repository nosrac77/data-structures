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
      this.tail = this.head;
    }
    this.head = this.head.nextNode
    if (this.head) {
      this.head.prevNode = null;
    }
    this._counter --;
    return output
  }

  remove(val) {
    if (!this.head) {
      throw new Error('Input value not in Doubly Linked List.');
    }
    let currentNode = this.head;
    while (currentNode) {
      if (this._counter === 1 && this.head.data == val) {
        currentNode = null;
        this.tail = null;
        this._counter --;
        break;
      }
      if (currentNode === this.tail) {
        this.tail = this.tail.prevNode;
        currentNode.prevNode.nextNode = null;
        this._counter --;
        return val;
      }
      if (currentNode.data == val) {
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
    return this.remove(this.tail.data);
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