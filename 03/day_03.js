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