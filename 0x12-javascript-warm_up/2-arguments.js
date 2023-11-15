#!/usr/bin/node

// Use const to create constants
const args = process.argv.slice(2);
const numArgs = args.length;

//Check the number of arguments and print the corresponding message
if (numArgs === 0) {
	console.log("No argument");
} else if (numArgs === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
