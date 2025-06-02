const fs = require("fs")

let input = fs.readFileSync(0).toString()

let arr = input.split(" ").map(Number)

let product = arr.reduce((acc, val) => acc * val, 1);

console.log(product)