'use strict';

class Node {
  constructor(val, priority, nextNode=null, prevNode=null) {
    this.priority = priority;
    this.data = val;
    this.nextNode = nextNode;
    this.prevNode = prevNode;
  }
}

class Priority {
  constructor() {
    this._counter = 0;
    this.priorities = [];
    this.head = null;
    this.tail = null;
  }

  insert(val, priority=0) {
    if (priority < 0) {
      throw new Error('Lowest priority is 0.')
    }
    this.priorities.push(priority);
    if (!this.head) {
      let currentNode = new Node(val, priority);
      this.head = currentNode;
      this.tail = this.head;
      this._counter ++;
    } else {
      let currentNode = new Node(val, priority, null, this.tail);
      this.tail.nextNode = currentNode;
      this.tail = currentNode;
      this._counter ++;
    }
  }

  pop() {
    if (!this.head) {
      throw new Error('Input priority not in Priority Queue.');
    }
    let maxPriority = this.priorities.reduce(function(a, b) {
      return Math.max(a, b);
    });
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.priority == maxPriority) {
        let val = currentNode.data;
        if (currentNode === this.head && this._counter == 1) {
          this.head = null;
          this.tail = null;
          this._counter --;
          return val;
        } else if (!currentNode.prevNode) {
          currentNode.nextNode.prevNode = null;
          this.head = null;
          this._counter --;
          return val;
        } else if (!currentNode.nextNode) {
          currentNode.prevNode.nextNode = null;
          this.tail = null;
          this._counter --;
          return val;
        }
        currentNode.prevNode.nextNode = currentNode.nextNode;
        currentNode.nextNode.prevNode = currentNode.prevNode;
        this._counter --;
        this.priorities.splice(this.priorities.indexOf(val), 1);
        return val;
      }
      currentNode = currentNode.nextNode;
    }
  }

  peek() {
    if (!this.head) {
      throw new Error('Priority Queue is empty.');
    }
    let maxPriority = this.priorities.reduce(function(a, b) {
      return Math.max(a, b);
    });
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.priority == maxPriority) {
        let val = currentNode.data;
        return val;
      }
      currentNode = currentNode.nextNode;
    }
  }

}

module.exports = Priority
