'use strict';

class MaxHeap {
  constructor(iterable=[]) {
    this.heap = iterable.sort(function(a, b){return b - a;});
  }

  findChildren(idx) {
    return [this.heap[idx * 2 + 1], this.heap[idx * 2 + 2]];
  }

  findParent(idx) {
    if (idx % 2 === 0) {
      var parentIdx = idx / 2 - 1;
    } else if (idx % 2 === 1) {
      var parentIdx = (idx - 1) / 2;
    }
    return parentIdx;
  }

  bubbleUp() {
    let currIdx = this.heap.length - 1;
    let parentIdx = this.findParent(currIdx);
    while (this.heap[currIdx] > this.heap[parentIdx]) {
      var parentVal = this.heap[parentIdx];
      this.heap[parentIdx] = this.heap[currIdx];
      this.heap[currIdx] = parentVal;
      currIdx = this.findParent(currIdx);
      parentIdx = this.findParent(currIdx);
    }
    if (this.heap[currIdx] > this.heap[0]) {
      let headVal = this.heap[0];
      this.heap[0] = this.heap[currIdx];
      this.heap[currIdx] = headVal;
    }
    return this.heap;
  }

  sortDown() {
    if (this.heap.length === 3) {
      let firstChild = this.heap[1];
      let secondChild = this.heap[2];
      let biggestChild = Math.max(firstChild, secondChild);
      if (biggestChild > this.heap[0]) {
        this.heap[this.heap.indexOf(biggestChild)] = this.heap[0];
        this.heap[0] = biggestChild;
      }
    } else if (this.heap.length > 4) {
      for (var i = 0; i <= Math.floor((this.heap.length / 2)) - 1; i++) {
        let firstChild = this.findChildren(i)[0];
        let secondChild = this.findChildren(i)[1];
        if (this.heap[i] < firstChild || this.heap[i] < secondChild) {
          let higherVal = Math.max(firstChild, secondChild);
          let lowerVal = this.heap[i];
          this.heap[this.heap.indexOf(higherVal)] = lowerVal;
          this.heap[i] = higherVal;
        }
      }
    }
  }

  push(val) {
    this.heap.push(val);
    this.bubbleUp();
  }

  pop() {
    if (this.heap.length === 0) {
      throw new Error('Cannot pop from an empty list.');
    } else if (this.heap.length === 1) {
      return this.heap.pop();
    } else if (this.heap.length === 2) {
      return this.heap.shift();
    } else if (this.heap.length === 3) {
      let headVal = this.heap[0];
      this.heap.shift();
      if (this.heap[0] < this.heap[1]) {
        let oldHead = this.heap[0];
        this.heap[0] = this.heap[1];
        this.heap[1] = oldHead;
      }
      return headVal;
    }
    let headVal = this.heap[0];
    this.heap.shift();
    this.sortDown();
    this.bubbleUp();
    return headVal;
  }
}

module.exports = MaxHeap
