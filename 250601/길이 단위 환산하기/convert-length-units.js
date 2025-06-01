function roundOne(num){
    return Math.round(num * 10) / 10
}

const fs = require("fs")

let input = Number(fs.readFileSync(0).toString())

console.log(roundOne(input*30.48).toFixed(1))
