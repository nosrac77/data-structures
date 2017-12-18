'use strict';

class LinkedList {
  constructor(iterable=[]) {
    this.head = null;
    this._counter = 0;
    if(iterable.length > 0){
      iterable.forEach(x => this.push(x));
    }
  }

  push(val) {
    this.head = new Node(val, this.head);
    this._counter ++;
  }

  pop() {
    if(this.head === null) {
      throw 'Cannot pop from empty list.';
    }
    let output = this.head.data;
    this.head = this.head.next;
    this._counter --;
    return output;
  }

  size() {
    return this._counter;
  }

  search(val) {
    let currentNode = this.head;
    while (currentNode !== null) {
      if (currentNode.data === val) {
        return currentNode;
      }
      currentNode = currentNode.next;
    }
    throw 'No node in LL containing val.';
  }

  remove(val){
    if (this.size() === 0) {
      throw 'Cannot use remove on empty List.'
    }
    if (this.head.data === val) {
      this.head = this.head.next;
      this._counter --;
      return;
    }
    let currentNode = this.head.next;
    let prevNode = this.head;
    let nodeRemoved = false;
    while (currentNode !== null && nodeRemoved === false) {
      if (currentNode.data === val) {
        prevNode.next = currentNode.next;
        currentNode.next = null;
        nodeRemoved = true;
        break;
      }
      prevNode = currentNode;
      currentNode = currentNode.next;
    }
    if (nodeRemoved === false) {
      throw 'Value given not in Linked List.';
    }
  }

  display(){
    let currentNode = this.head;
    let listDisplay = [];
    while (currentNode !== null) {
      listDisplay.push(currentNode.data);
      currentNode = currentNode.next;
    }
    return listDisplay.join(', ');
  }
}

class Node {
  constructor(data, next=null){
    this.data = data
    this.next = next
  }
}

module.exports = {LinkedList, Node};
if(require.main === module){
  var linkedList = new LinkedList([1, 2, 3, 4]);
  console.log(linkedList.display());
  console.log(linkedList.size());
  console.log(linkedList.remove(6));
}
