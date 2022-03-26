//stack implmentation Array Implementation
// last in last out
// pop() removes the the last element of the stack
// size() gives the size of the stack
// push() adds stuff to the array
// peek() gets the top data element of the stack without removing it
// isEmpty() check if the stack is empty

class CustomStack {
  constructor(arg) {
    this.data = [];
  }
  pop() {
    return this.data.pop();
  }
  push(element) {
    this.data.push(element);
  }
  peek() {
    let lastindex = this.size() - 1;
    return this.data[lastindex];
  }

  size() {
    return this.data.length;
  }
  isEmpty() {
    if (this.size() > 0) {
      return false;
    }
    return true;
  }
}

// test my method isEmpty(): 2 execution paths
// empty case
const names = new CustomStack();
console.log(names.isEmpty());

// with somestuff in it
const colors = new CustomStack();
colors.push("red");
console.log("colors: ", colors);
console.log(colors.isEmpty());

// testing size
colors.push("yellow");
colors.push("black");
colors.push("blown");
console.log("size:", colors.size());

// testing pop
//size:", colors.size());
console.log("pop twice");
colors.pop();
colors.pop();
console.log("size:", colors.size());

// testing peek
console.log("Peek element:", colors.peek());
