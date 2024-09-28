const Stack = require("./stack.js");

var stack = new Stack();
console.log("isEmpty: ", stack.isEmpty());
stack.push(12);
stack.push(23);
stack.push(55);
console.log("isEmpty: ", stack.isEmpty());
console.log("size: ", stack.size());
stack.print();
// peak
// there is a problem if you run this code - to be fixed later!!
