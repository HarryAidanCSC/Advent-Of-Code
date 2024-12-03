const fs = require('fs');
const path = require('path');
const data = fs.readFileSync(path.join(__dirname, 'input.txt'), "utf8").trim()

// Part One
const regex = /mul\(\d{1,3},\d{1,3}\)/g;
const matches = data.match(regex);

let p1 = 0
for(let i of matches){
    const [x,y] = i.match(/\d+/g).map(Number)
    p1 += x * y
}

console.log(p1)

// Part Two
const p2Regex = /mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)/g;
const p2Matches = data.match(p2Regex)

let p2 = 0, enable = true
for(let i of p2Matches){
    if (i === 'do()'){
        enable = true
    } else if (i === "don't()"){
        enable = false 
    } else {
        if (enable){
        const [x,y] = i.match(/\d+/g).map(Number)
        p2 += x * y
        }
    }
}

console.log(p2)