#!/usr/bin/node

const args = process.argv.slice(2); // Get all arguments except the first two (node path)
const myVar = args.length;

if (myVar === 0) {
  console.log(0);
} else if (myVar === 1) {
  console.log(0);
} else {
  const intArgs = args.map(arg => parseInt(arg)); // Convert all arguments to integers
  const sortedArgs = intArgs.sort((a, b) => b - a); // Sort arguments in descending order
  console.log(sortedArgs[1]); // Print the second largest integer
}
