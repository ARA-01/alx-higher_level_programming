#!/usr/bin/node

// Use const to create constants
const arg = process.argv[2];

//Check if an argument is provided
if (arg) {
	console.log(arg); // Print the first argument
} else {
	console.log("No argument"); // Print "No argument" if no arguments are provided
}
