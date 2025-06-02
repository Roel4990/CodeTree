const fs = require("fs")

let input = fs.readFileSync(0).toString().trim()

let arr = input.split(" ")

console.log(arr.reverse().join(" "))