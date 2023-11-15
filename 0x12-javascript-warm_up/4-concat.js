#!/usr/bin/node
// Use const to create constants
const arg1 = process.argv[2];
const arg2 = process.argv[3];
// Check if both arguments are provided
if (arg1 && arg2) {
	console.log(process.argv[2] + ' is ' + process.argv[3]); // Print output
} else {
	console.log("Please provide two arguments");
}
