function roundTwo(num) {
    return Math.round(num * 100) / 100
}

const fs = require("fs")

let input = Number(fs.readFileSync(0).toString())

console.log(roundTwo(input + 1.5).toFixed(2))
