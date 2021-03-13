const CustomStack = require("./stack")

function isParenthesisValid(validationstring) {
  var stack = new CustomStack()
  for (let pos = 0; pos < validationstring.length; pos++) {
    var currentChar = validationstring.charAt(pos)
    console.log(currentChar)
    if (currentChar == "(") {
      stack.push(currentChar)
    } else if (currentChar == ")") {
      if (stack.isEmpty()) {
        return false
      }
      stack.pop()
    }
  }
  return stack.isEmpty()
}

console.log(
  isParenthesisValid("((((()))))") // valid
)

console.log(
  isParenthesisValid("((((())") // invalid
)

console.log(
  isParenthesisValid("((") // invalid
)

console.log(
  isParenthesisValid("()()") // valid
)

// > Time complexity
// This algorithm process a string character by character. Hence the time
// complexity is O(n) where n is the length of the string
