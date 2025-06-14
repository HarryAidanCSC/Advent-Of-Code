const fs = require("fs");

const filePath =
  "C:/Users/hxzzm/OneDrive/Documents/Git/Advent-of-Code-2023/practice/input.txt";
const data = fs.readFileSync(filePath, "utf8");
const lines = data.split("\n");

// Part One

let p1 = 0;
let prev = Infinity;

lines.forEach(function (line) {
  let int = parseInt(line);
  if (int > prev) {
    p1 += 1;
  }
  prev = int;
});

console.log(p1);

// Part Two
let window = [];
let p2 = 0;
let previous = null;

lines.forEach(function (line) {
  let val = parseInt(line);
  if (window.length == 3) {
    previous = window.shift();
    if (val > previous) {
      p2 += 1;
    }
  }
  window.push(val);
});

console.log(p2);
