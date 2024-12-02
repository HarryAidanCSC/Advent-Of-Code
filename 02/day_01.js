const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'input.txt');
const lines = fs.readFileSync(filePath, "utf8")
    .split("\n")
    .filter(line => line.trim() !== "")
    .map(line => line.split(" "))
    .map(innerArray => innerArray.map(Number));

// Part One
let p1 = 0;
for (let line of lines) {
    let prevVal = null, valid = true, prevDir = null;
    for (let val of line) {
        if (prevVal !== null) {
            let diff = Math.abs(prevVal - val);
            if (diff < 1 || diff > 3) {
                valid = false;
                break;
            }
            let dir = prevVal - val;
            if (prevDir !== null) {
                if (prevDir > 0 && dir < 0) {
                    valid = false;
                    break;
                } else if (prevDir < 0 && dir > 0) {
                    valid = false;
                    break;
                }
            }
            prevDir = dir;
        }
        prevVal = val;
    }
    if (valid) {
        p1 += 1;
}
}
console.log(p1);

// Part Two
