//stack implmentation Array Implementation
// last in last out
// pop() removes the the last element of the stack
// size() gives the size of the stack
// push() adds stuff to the array
// peek() gets the top data element of the stack without removing it
// isEmpty() check if the stack is empty

class CustomStack {
  constructor(array) {
    this.data = []
    if (array) this.data = array
  }
  pop() {
    return this.data.pop()
  }
  push(element) {
    this.data.push(element)
  }
  peek() {
    let lastindex = this.size() - 1

    return this.data[lastindex]
  }

  size() {
    return this.data.length
  }
  isEmpty() {
    if (this.size() > 0) {
      return false
    }
    return true
  }
  getBuffer() {
    return this.data.slice()
  }
}

module.exports = CustomStack
// test my method isEmpty(): 2 execution paths
// empty case
const names = new CustomStack()
console.log(names.isEmpty())

// with somestuff in it
const colors = new CustomStack()
colors.push("red")
console.log("colors: ", colors)
console.log(colors.isEmpty())

// testing size
colors.push("yellow")
colors.push("black")
colors.push("blown")
console.log("size:", colors.size())

// testing pop
//size:", colors.size());
console.log("pop twice")
colors.pop()
colors.pop()
console.log("size:", colors.size())

// testing peek
console.log("Peek element:", colors.peek())

// Searching
const stackSearch = (stack, element) => {
  var buffer = stack.getBuffer()
  var bufferstack = new CustomStack(buffer)

  while (!bufferstack.isEmpty()) {
    if (bufferstack.pop() == element) return true
  }

  return false
}

let arry = [1, 2, 3, 1]
const mystack = new CustomStack(arry)

let value = stackSearch(mystack, 3)
console.log("The values is present  ", value)

// access
const stackAccessNthTopNode = (stack, x) => {
  var buffer = stack.getBuffer()
  if (x <= 0) throw "error"

  var bufferstack = new CustomStack(buffer)

  while (--x !== 0) {
    bufferstack.pop()
  }
  return bufferstack.pop()
}

let third = stackAccessNthTopNode(mystack, 2)
console.log("The third value is ", third)
