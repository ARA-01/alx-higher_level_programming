#!/usr/bin/node
const args = process.argv.slice(2).map(number);
const numArgs = args.length;

if (numArgs >= 2) {
	const sortedArgs = args.sort((a, b)) => b - a);
console.log(sortedArgs[1]);
} else {
	console.log(0);
}
