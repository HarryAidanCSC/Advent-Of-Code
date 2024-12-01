const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'input.txt');
const data = fs.readFileSync(filePath, "utf8");
const lines = data.split("\n").filter(line => line.trim() !== ""); 

// Part One
const lhs = [], rhs = []
lines.forEach(function(line){
    const [x, y] = line.split('   '); 
    lhs.push(Number(x))
    rhs.push(Number(y))
    console.log(line)
})

rhs.sort()
lhs.sort()
console.log(rhs)

let p1 = 0
for(let i = 0; i < rhs.length; i++){
    p1 += Math.abs(lhs[i] - rhs[i])
}
console.log(p1)

// Part Two
let dict = {}
for (let o of lhs){
    if (dict[o]){
        dict[o]++;
    } else {
    dict[o] = 1
}
}

let p2 = 0

for (let o of rhs){
    if (dict[o]){
        p2 += dict[o] * o
    }
}
console.log(p2)
