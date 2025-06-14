const fs = require("fs");

const filePath =
  "C:/Users/hxzzm/OneDrive/Documents/Git/Advent-of-Code-2023/practice/2022/2/input.txt";
const data = fs.readFileSync(filePath, "utf8");
const lines = data.split("\n").filter(line => line.trim() !== ""); 

// Part One
let p1x = 0
let p1y = 0
const p1Map = {
    'up': -1,
    'down' : 1
}

let s = "", int = 0
lines.forEach(function(line){
    [s, int] = line.split(" ")
    int = parseInt(int)
    if (s === "up" || s === "down"){
        p1y += int * p1Map[s];
    } else {
        p1x += int
    }
});

console.log(p1y * p1x)

// Part Two
let p2x = 0, p2y = 0, p2a = 0;

lines.forEach(function(line){
    [s, int] = line.split(" ")
    int = parseInt(int)
    if (s === "up" || s === "down"){
        p2a += int * p1Map[s];
    } else {
        p2x += int;
        p2y += p2a * int;
    }
});

console.log(p2x * p2y);