function roundToTwo(num) {
  return Math.round(num * 100) / 100;
}

const fs = require("fs")

let input = Number(fs.readFileSync(0).toString())

console.log(roundToTwo(input).toFixed(2))